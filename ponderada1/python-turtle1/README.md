# Atividade 1: Turtlesim: simulando um ambiente robótico integrado no ROS

## Enunciado

Crie um script em Python capaz de interagir com o nó de simulação do turtlesim e enviar mensagens nos tópicos que regem a locomoção da tartaruga principal. Utilize este script para reproduzir um desenho de sua autoria. Utilize a estrutura de dados que preferir para representar a “imagem” a ser desenhada. O uso de programação orientada a objetos é obrigatório.

## Descrição da solução

Este é um código que controla um robô tartaruga (turtle) em ROS (Robot Operating System). Ele cria um nó (node) chamado "turtle_controller" que publica comandos de movimento para a tartaruga no tópico "/turtle1/cmd_vel". A cada 1 segundo (definido pelo timer), o método "move_turtle" é chamado, que define os comandos de movimento (linear e angular) para a tartaruga.

O código faz a tartaruga seguir um trajeto que forma o desenho das "Relíquias da Morte". A variável "counter_" é usada para determinar qual comando de movimento deve ser executado em cada chamada da função "move_turtle". O valor da velocidade linear (linear.x) e angular (angular.z) são definidos para cada ponto do trajeto, causando a movimentação da tartaruga de acordo com as coordenadas especificadas.

Por fim, o código usa a função "spin" do ROS para manter o nó em execução até que o programa seja encerrado.

## Caminho para o código
O código em python "Turtle1.py" para a movimentação da tartaruga encontra-se na pasta 'venv/Scripts' deste repositório.

## Link para o vídeo no Youtube
<a href = "https://youtu.be/emMkc10NFZc"> Vídeo da simulação do ambiente </a>
