import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

PHASES = [
    (5.0,  [0.0, 0.0, 0.0, 0.0]),   # Phase 0: 대기
    (5.0,  [8.0, 0.0, 0.0, 0.0]),   # Phase 1: joint1_z
    (5.0,  [0.0, 8.0, 0.0, 0.0]),   # Phase 2: joint1_y
    (5.0,  [0.0, 0.0, 8.0, 0.0]),   # Phase 3: joint2
    (None, [0.0, 0.0, 0.0, 0.0]),   # Phase 4: 정지 (무한)
]


class ArmSequencer(Node):
    def __init__(self):
        super().__init__('arm_sequencer')
        self.pub = self.create_publisher(
            Float64MultiArray,
            '/effort_controller/commands',
            10
        )
        self.timer = self.create_timer(0.1, self.callback)  # 10 Hz
        self.current_phase = 0
        self.phase_start = self.get_clock().now()

    def callback(self):
        duration, data = PHASES[self.current_phase]

        if duration is not None:
            elapsed = (self.get_clock().now() - self.phase_start).nanoseconds / 1e9
            if elapsed >= duration:
                self.current_phase += 1
                self.phase_start = self.get_clock().now()
                duration, data = PHASES[self.current_phase]

        msg = Float64MultiArray()
        msg.data = data
        self.pub.publish(msg)
        self.get_logger().info(
            f'[Phase {self.current_phase}]  data={data}'
        )


def main():
    rclpy.init()
    node = ArmSequencer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
