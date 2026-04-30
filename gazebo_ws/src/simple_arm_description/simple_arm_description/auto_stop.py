import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray

STOP_THRESHOLD = 0.8  # rad


class AutoStop(Node):
    def __init__(self):
        super().__init__('auto_stop')

        # ① /joint_states 구독자 생성
        self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_cb,
            10
        )

        # ② /effort_controller/commands 퍼블리셔 생성
        self.pub = self.create_publisher(
            Float64MultiArray,
            '/effort_controller/commands',
            10
        )

        # ③ 0.5초마다 현재 joint3 position 출력용 타이머
        self.timer = self.create_timer(0.5, self.log_cb)

        self.joint3_pos = 0.0
        self.stopped = False

    def joint_cb(self, msg):
        # ④ joint3 position 추출
        if 'joint3' in msg.name:
            idx = msg.name.index('joint3')
            self.joint3_pos = msg.position[idx]

        # ⑤ 임계값 초과 시 토크 해제 후 노드 종료
        if not self.stopped and abs(self.joint3_pos) > STOP_THRESHOLD:
            self.stopped = True
            stop_msg = Float64MultiArray()
            stop_msg.data = [0.0, 0.0, 0.0, 0.0]
            # ⑥ 퍼블리시
            self.pub.publish(stop_msg)
            self.get_logger().info(
                f'[AUTO STOP]  joint3 = {self.joint3_pos:.3f} rad 도달 → 전체 토크 해제'
            )
            # ⑦ 노드 종료
            raise SystemExit

    def log_cb(self):
        if not self.stopped:
            self.get_logger().info(f'joint3 현재 위치: {self.joint3_pos:.3f} rad')


def main():
    rclpy.init()
    node = AutoStop()
    try:
        rclpy.spin(node)
    except SystemExit:
        pass
    rclpy.shutdown()


if __name__ == '__main__':
    main()
