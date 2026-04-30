import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from my_action_interfaces.action import MyInterfaces
import time

class MyServer(Node):

    def __init__(self):
        super().__init__('my_server')
        self._action_server = ActionServer(
            self,
            MyInterfaces,
            'ServerTest',
            self.execute_callback)
        
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        
        feedback_msg = MyInterfaces.Feedback()
        feedback_msg.partial_sequence = [0, 1]

        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[1] + feedback_msg.partial_sequence[i-1])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)    
        
        goal_handle.succeed()
        result = MyInterfaces.Result()
        result.sequence = feedback_msg.partial_sequence

        return result
    
def main(args=None):
    rclpy.init(args=args)

    my_server = MyServer()
    rclpy.spin(my_server)

if __name__ == '__main__':
    main()