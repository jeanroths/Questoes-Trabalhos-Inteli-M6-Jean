#!/usr/bin/env python3
# Importando bibliotecas necessárias
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

#Classe TurtleController
class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(1, self.move_turtle)
        self.twist_msg_ = Twist() #mensagens que publicam velocidade linear e angular
        self.counter_ = 0

    def move_turtle(self):
        self.counter_ += 1
        #Movimentação da tartaruga fazendo a primeira linha
        if self.counter_ == 1:
            self.twist_msg_.linear.x = 3.0
            self.twist_msg_.angular.z = 0.0
          #Movimentação da tartaruga fazendo a primeira rotação
        if self.counter_ == 2:
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = 2.0
          #Movimentação da tartaruga fazendo a segunda linha
        if self.counter_ == 3:
             self.twist_msg_.linear.x = 3.0
             self.twist_msg_.angular.z = 0.0
          #Movimentação da tartaruga fazendo a segunda rotação
        if self.counter_ == 4:
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 2.2
          #Movimentação da tartaruga fazendo a terceira linha
        if self.counter_ == 5:
             self.twist_msg_.linear.x = 3.1
             self.twist_msg_.angular.z = 0.0
          #Movimentação da tartaruga fazendo a terceira rotação
        if self.counter_ == 6:
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 2.05
          #Movimentação da tartaruga fazendo o caminho até metade do lado do triângulo
        if self.counter_ == 7:
             self.twist_msg_.linear.x = 1.35
             self.twist_msg_.angular.z = 0.0
          #Movimentação da tartaruga fazendo a circunferência
        if self.counter_ == 8:
             self.twist_msg_.linear.x = 0.5
             self.twist_msg_.angular.z = 0.6
          #Movimentação da tartaruga fazendo parando para fazer a linha do meio
        if self.counter_ == 19:
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 0.0
        if self.counter_ == 20:
          #Movimentação da tartaruga rodando para fazer a linha do meio
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 1.31
        if self.counter_ == 21:
          #Movimentação da tartaruga fazendo a linha do meio
             self.twist_msg_.linear.x = 2.8
             self.twist_msg_.angular.z = 0.0    
        if self.counter_ == 22:
          #Tartaruga parando
             self.twist_msg_.linear.x = 0.0
             self.twist_msg_.angular.z = 0.0         
        self.publisher_.publish(self.twist_msg_)

def main(args=None): #função principal
        rclpy.init(args=args)
        turtle_controller = TurtleController()
        rclpy.spin(turtle_controller)
        turtle_controller.destroy_node()
        rclpy.shutdown()

#Execução do programa
if __name__ == '__main__':
        main()
