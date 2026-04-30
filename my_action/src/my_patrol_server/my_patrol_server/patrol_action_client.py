#!/usr/bin/env python3
import sys
import select
import random

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from geometry_msgs.msg import Pose2D
from my_action_interfaces.action import PatrolTest

class PatrolActionClient(Node):
    def __init__(self):
        super().__init__('patrol_action_client')

        self._client = ActionClient(self, PatrolTest, 'patrol')
        self._goal_handle = None
        self._running = True

        # ENTER 키 감지용 타이머
        self.create_timer(0.1, self.check_keyboard)

    def generate_random_waypoints(self, count=100):
        waypoints = []
        for _ in range(count):
            x = random.uniform(1.0, 10.0)
            y = random.uniform(1.0, 10.0)
            waypoints.append(Pose2D(x=x, y=y, theta=0.0))
        return waypoints

    def send_goal(self):
        if not self._running:
            return

        goal_msg = PatrolTest.Goal()
        goal_msg.waypoints = self.generate_random_waypoints(count=100)
        goal_msg.tolerance = 0.3

        self._client.wait_for_server()
        self.get_logger().info('Sending RANDOM patrol goal')

        send_future = self._client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        send_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        self._goal_handle = future.result()

        if not self._goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        result_future = self._goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)

    def result_callback(self, future):
        if not self._running:
            return

        result = future.result().result
        self.get_logger().info(f'Patrol finished: {result.message}')

        # 순찰이 끝나면 다시 새로운 목표 전송 (무한 루프)
        self.send_goal()

    def check_keyboard(self):
        if self._goal_handle is None:
            return

        # stdin에 데이터가 있는지 확인 (비동기 키 입력 체크)
        if select.select([sys.stdin], [], [], 0)[0]:
            input() # 입력 버퍼 비우기
            self.cancel_goal()

    def cancel_goal(self):
        if self._goal_handle is not None:
            self.get_logger().warn('Canceling patrol (STOP infinite node)')
            self._running = False
            self._goal_handle.cancel_goal_async()
            self._goal_handle = None

    def feedback_callback(self, feedback_msg):
        fb = feedback_msg.feedback
        self.get_logger().info(
            f'waypoint=[{fb.current_index}], '
            f'remaining={fb.remaining_distance:.2f}'
        )

def main():
    rclpy.init()
    node = PatrolActionClient()
    node.send_goal()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()