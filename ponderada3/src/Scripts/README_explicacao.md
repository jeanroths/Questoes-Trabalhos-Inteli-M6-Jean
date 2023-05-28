# Atividade 3: Processamento de imagens e detecção de objetos

## Enunciado

Desenvolva um script em Python capaz de identificar rachaduras em paredes de concreto. Utilize o [dataset](https://universe.roboflow.com/university-bswxt/crack-bphdr/dataset/2) desenvolvido pela Roboflow. Para o desenvolvimento dessa atividade, recomenda-se o uso de um modelo de detecção de objetos pré-treinado, como o [YoLo](https://github.com/ultralytics/ultralytics). É possível ver um exemplo de como desenvolver um script similar [nesse vídeo](https://www.youtube.com/watch?v=vFGxM2KLs10).


## Descrição da solução
A solução implementada no código do Colab tem como objetivo lidar com um problema de detecção de rachaduras em paredes utilizando a biblioteca Ultralytics e o modelo YOLO v8.

Primeiramente, são importadas bibliotecas necessárias como "`os`", "`ultralytics.YOLO`" e "`IPython.display.Image`". A biblioteca `os` é utilizada para manipulação de arquivos e diretórios, enquanto "`ultralytics.YOLO`" é utilizada para a detecção de objetos e "`IPython.display.Image`" é utilizada para exibir imagens no notebook.
Depois disso, é definida uma variável "HOME" com o caminho do diretório atual, um diretório chamado "datasets" é criado e o diretório atual é alterado para "datasets". Após isso, a biblioteca "Roboflow", que é uma plataforma de gerenciamento de dados para treinamento de modelos de visão computacional é instalada e cria-se uma instância da classe Roboflow com uma chave API específica, e logo em seguida é feito o download do dataset de rachaduras em paredes de concreto da Roboflow. 
Na linha de comando "`!yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=10 imgsz=800 plots=True`" é feito o treinamento do modelo YOLO v8 com o dataset de rachaduras em paredes de concreto, com 10 épocas e imagens de tamanho 800x800. O modelo treinado e o resultado é salvo em "`runs/detect/train`". 
Ao final um arquivo binário `best.pt` é gerado e salvo no diretório atual, e é feita a detecção de objetos em imagens de teste com este modelo treinado. 

## Caminho para o código
O código em ipynb "Ponderada_3_EngComp_Jean.ipynb" de detecção de rachaduras em imagens encontra-se na pasta 'src/Scripts' deste repositório.

## Link para o vídeo no Youtube
<a href="https://youtu.be/0QI7AgkxpS0" > Vídeo da detecção de rachaduras </a>