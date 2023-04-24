#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(1, self.move_turtle)
        self.twist_msg_ = Twist()
        self.counter_ = 0

    def move_turtle(self):
        self.counter_ += 1
        if self.counter_ == 1:
            self.twist_msg_.linear.x = 3.0
            self.twist_msg_.angular.z = 0.0
        if self.counter_ == 2:
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = 2.0
        if self.counter_ == 3:
             self.twist_msg_.linear.x = 3.0
             self.twist_msg_.angular.z = 0.0
        if self.counter_ == 4:
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 2.2
        if self.counter_ == 5:
             self.twist_msg_.linear.x = 3.1
             self.twist_msg_.angular.z = 0.0
        if self.counter_ == 6:
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 2.05
        if self.counter_ == 7:
             self.twist_msg_.linear.x = 1.35
             self.twist_msg_.angular.z = 0.0
        if self.counter_ == 8:
             self.twist_msg_.linear.x = 0.5
             self.twist_msg_.angular.z = 0.6
        if self.counter_ == 19:
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 0.0
        if self.counter_ == 20:
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 1.31
        if self.counter_ == 21:
             self.twist_msg_.linear.x = 2.8
             self.twist_msg_.angular.z = 0.0    
        if self.counter_ == 22:
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 0.0         
        self.publisher_.publish(self.twist_msg_)

def main(args=None):
        rclpy.init(args=args)
        turtle_controller = TurtleController()
        rclpy.spin(turtle_controller)
        turtle_controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
        main()
