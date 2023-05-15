#importando bibliotecas necessárias
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from turtlesim.msg import Pose as TPose
import math
from collections import deque

MAX_DIFF = 0.1 # variável para verificar se o robô chegou no ponto desejado
#classe para representar a pose do robô
class Pose(TPose):
    def __init__(self, x=0.0, y=0.0, theta=0.0): #construtor da classe
        super().__init__(x=x, y=y, theta=theta)
        
    def __repr__(self):
        return f"(x={self.x:.2f}, y={self.y:.2f}, theta={self.theta:.2f})"
    
    def __add__(self, other): #Sempre que ver '+' executar esse método
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other): #Sempre que ver '-' executar esse método
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __eq__(self, other): #Fazer overload do operador ==
        return abs(self.x - other.x) <= MAX_DIFF and abs(self.y - other.y) <= MAX_DIFF
    
class Rotation(TPose):
    def __init__(self, theta=0.0): #construtor da classe de rotação
        super().__init__(x=0.0, y=0.0, theta=theta)
        self.rotated = False  # variável para verificar se o robô já rotacionou o suficiente
        
    def __repr__(self):
        return f"(theta={self.theta:.2f})"
    
    def __eq__(self, other):
        return abs(self.theta - other.theta) <= 0.05
class MissionControl(deque): # Classe em que os pontos para o robô seguir são passados
    
    def __init__(self): 
        super().__init__()
        # lista de pontos que o robô deve seguir
        self.enqueue(Pose(1.0, -1.0))
        self.enqueue(Pose(-1.0, -1.0))
        self.enqueue(Pose(-1.0, 1.0))
        self.enqueue(Pose(0.0, 0.0))
        self.enqueue(Pose(-2.0, 0.0))


    def enqueue(self, x):
        """Método para adicionar novos pontos ao fim da fila."""
        super().append(x)
    
    def dequeue(self):
        """Método para retirar pontos do começo da fila."""
        return super().popleft()



class BotController(Node):
    def __init__(self, control_period=0.05, mission_control=MissionControl()):
        super().__init__("bot_controller")
        self.initiated = False # variável para verificar se a pose foi iniciada
        self.setpoint = Pose() # variável para armazenar o ponto para onde o robô deve ir
        self.pose = Pose() # variável para armazenar a pose atual do robô
        self.theta= Rotation() # variável para armazenar o ângulo do robô
        self.setpoint_rotation = Rotation() # variável para armazenar a rotação para onde o robô deve ir
        self.setpoint_translation = 0.0 # variável para armazenar a distância para onde o robô deve ir
        self.current_rotation = Rotation() # variável para armazenar a rotação atual do robô
        self.queue = mission_control # variável para armazenar a fila de pontos para onde o robô deve ir

        self.origin = Pose() # variável para armazenar a origem do robô

        self.control_timer = self.create_timer( #create_timer
            timer_period_sec=control_period, 
            callback=self.control_callback
        )
        self.subscription = self.create_subscription( #create_subscription
            msg_type=Odometry,
            topic="odom",
            callback=self.pose_callback,
            qos_profile=10
        )
        self.publisher = self.create_publisher( #create_publisher
            msg_type=Twist, 
            topic="cmd_vel", 
            qos_profile=10
        )
    def control_callback(self): 
        if not self.initiated: # se a pose não foi iniciada, não fazer nada e aguardar pela pose
            self.get_logger().info("Aguardando pose...")
            return
        
        msg = Twist()  
        if not self.setpoint_rotation.rotated: # se o robô não rotacionou o suficiente, rotacionar se a rotação atual for diferente da rotação desejada
            if self.current_rotation == self.setpoint_rotation:
                msg.angular.z = 0.0
                self.get_logger().info(f"o robô rodou o necessário")
                self.setpoint_rotation.rotated = True
                print(f"final_rotation: {self.current_rotation}")
            else:
                offset = self.setpoint_rotation.theta - self.current_rotation.theta
                if abs(offset) > 0.05:
                    msg.angular.z = 0.5 if offset > 0 else -0.5
        else:
            if self.pose == self.setpoint: # se o robô chegou no ponto desejado, ir para o próximo ponto
                msg.linear.x = 0.0
                self.get_logger().info(f"o robô chegou ao destino")
                self.publisher.publish(msg)
                self.update_setpoint()
            else:
                offset = self.setpoint_rotation.theta - self.current_rotation.theta # se o robô não chegou no ponto desejado, rotacionar se a rotação atual for diferente da rotação desejada
                if abs(offset) > 0.05:
                    msg.angular.z = 0.5 if offset > 0 else -0.5
                else:
                    msg.angular.z = 0.0 
                self.relative_desloc = Pose(x=self.setpoint.x - self.pose.x, y=self.setpoint.y - self.pose.y) # vetor deslocamento relativo
                self.distance = math.sqrt(self.relative_desloc.x**2 + self.relative_desloc.y**2) # distância entre o robô e o ponto desejado
                print(f"pose: {self.pose}, setpoint: {self.setpoint},.distance: {self.distance}")

                if abs(self.desired - self.current) > 0.1: # se o robô não chegou no ponto desejado, andar se a distância atual for diferente da distância desejada
                    msg.linear.x = 0.5 if self.desired - self.current else -0.5
                else:
                    msg.linear.x = 0.0
                    self.get_logger().info(f"o robô chegou ao destino")
                    self.publisher.publish(msg)
                    self.update_setpoint()


        self.publisher.publish(msg) # publicar mensagem

    def update_setpoint(self): # método para atualizar o ponto desejado
        try:
            print(self.queue)
            self.setpoint = self.queue.dequeue() # retirar o primeiro ponto da fila
            self.get_logger().info(f"Novo setpoint: {self.setpoint}")
            self.get_logger().info(f"o robô chegou em {self.pose}, \
                                   indo para {self.setpoint}")
            self.origin = self.pose # atualizar a origem

            if self.setpoint == Pose(0.0,0.0): # se o ponto desejado for a origem, rotacionar para o ângulo 0
                self.theta = Rotation(theta=0.0) 
            else: # se o ponto desejado não for a origem, rotacionar para o ângulo do ponto desejado
                self.theta= Rotation(theta=math.atan2(self.setpoint.y - self.pose.y, self.setpoint.x - self.pose.x))
                print(f"theta: {self.theta}")

            self.relative_desloc = Pose(x=self.setpoint.x - self.pose.x, y=self.setpoint.y - self.pose.y)
            self.distance = math.sqrt(self.relative_desloc.x**2 + self.relative_desloc.y**2)

            self.desired = math.sqrt(self.relative_desloc.x**2 + self.relative_desloc.y**2) # atualizar a distância desejada

            if self.relative_desloc.x >= 0 and self.relative_desloc.y >=0: # atualizar a rotação desejada em relação ao primeiro quadrante
                self.setpoint_rotation = Rotation(theta=abs(self.theta.theta))
            elif self.relative_desloc.x >=0 and self.relative_desloc.y <= 0: # atualizar a rotação desejada em relação ao segundo quadrante
                self.setpoint_rotation = Rotation(theta=-abs(self.theta.theta))
            elif self.relative_desloc.x <=0 and self.relative_desloc.y <= 0: # atualizar a rotação desejada em relação ao terceiro quadrante
                self.setpoint_rotation = Rotation(theta=-abs(self.theta.theta))
                print(f"setpoint_rotation: {self.setpoint_rotation}")
            else: # atualizar a rotação desejada em relação ao quarto quadrante
                self.setpoint_rotation = Rotation(theta=abs(self.theta.theta))

        except IndexError:
            self.get_logger().info(f"Fim do percurso!") # se a fila estiver vazia, terminar a jornada
            exit()
    def pose_callback(self, msg): # método para atualizar a pose atual
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        ang = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
        self.pose = Pose(x=x, y=y, theta=theta) 
        self.current_rotation = Rotation(theta=self.pose.theta) # atualizar a rotação atual
        self.current = math.sqrt((self.pose.x - self.origin.x)**2 + (self.pose.y - self.origin.y)**2) # atualizar a distância atual

        if not self.initiated: # se o robô não tiver sido iniciado, iniciar
            self.initiated = True
            print(f"pose inicial: {self.pose}")
            self.update_setpoint()
            self.get_logger().info(f"Setpoint: {self.setpoint}")

def main(args=None): # função main
    rclpy.init(args=args)
    tc = BotController()
    rclpy.spin(tc)
    tc.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()