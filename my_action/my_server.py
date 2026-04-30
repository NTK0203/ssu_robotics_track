import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from my_action_interfaces.action import MyInterfaces

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
        result = MyInterfaces.Result()
        return result
    
def main(args=None):
    rclpy.init(args=args)

    my_server = MyServer()
    rclpy.spin(my_server)

if __name__ == '__main__':
    main()