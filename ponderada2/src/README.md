# Atividade 2: Simulação de robôs móveis com Gazebo

## Enunciado

Crie um pacote em ROS capaz de interagir com uma simulação feita no Gazebo de modo que a plataforma simulada do turtlebot3 seja capaz de mover-se de maneira controlada.
- Interagir com os tópicos e/ou serviços do turtlebot3 de modo a conseguir mandar comandos de velocidade e extrair dados de odometria.
- Conceber uma estrutura de dados capaz de armazenar a série de movimentos que devem ser feitos pelo robô para chegar no objetivo.
- Implementar uma rota pré-estabelecida

## Descrição da solução

Este código é um controlador para um robô turtlebot3 simulado no Gazebo. O objetivo do robô é seguir uma sequência de pontos em uma ordem pré-determinada. O controlador tem três componentes principais: uma classe "Pose" que armazena a posição do robô, uma classe "Rotation" que armazena a rotação do robô e uma classe "BotController" que controla o robô. O controlador recebe uma fila de pontos para seguir e move o robô para cada um deles.

O BotController inicializa um node no ROS, define uma lista de pontos que o robô deve seguir e cria um timer de controle para atualizar as mensagens de comando de velocidade. O controlador também cria um subscriber para receber as informações de odometria do robô e um publisher para enviar as mensagens de comando de velocidade para o robô.

No control_callback, o controlador verifica se a posição atual do robô é a mesma que o ponto de destino e se o robô já girou a quantidade necessária. Se o robô não girou o suficiente, ele calcula a diferença entre a rotação atual do robô e a rotação necessária para chegar ao ponto de destino e publica uma mensagem de comando de velocidade com uma velocidade angular correspondente. Se o robô já girou o suficiente, o controlador verifica se o robô já chegou no ponto de destino. Se ele ainda não chegou, o controlador calcula a distância restante e publica uma mensagem de comando de velocidade com uma velocidade linear correspondente. Se o robô chegou ao ponto de destino, o controlador remove o ponto da fila e define o próximo ponto como o ponto de destino. Se a fila estiver vazia, o robô para.


## Caminho para o código
O código em python "bot_gaz_controller.py" para a movimentação do robô encontra-se na pasta 'src/Scripts' deste repositório.

## Link para o vídeo no Youtube
<a href = "https://youtu.be/0R31V5MNPUU"> Vídeo da simulação do ambiente </a>