# Atividade 4: Backend para transmissão e armazenamento de imagens

# Enunciado

Desenvolva o software de um backend capaz de receber imagens e armazená-las adequadamente. Não há restrições com relação à tecnologia utilizada.

# Descrição da solução

A solução proposta consiste em desenvolver um software de backend capaz de receber imagens e armazená-las adequadamente, sem restrições quanto à tecnologia utilizada. A solução baseia-se em três códigos principais.

## Backend com FastAPI e integração com o Supabase:

É utilizado o framework FastAPI em Python para criar o backend.
O Supabase é um serviço de armazenamento em nuvem utilizado para armazenar as imagens de forma persistente.
O backend possui três rotas principais:
- Rota GET - `/list`: Retorna a lista de imagens armazenadas no bucket do Supabase. 
- Rota POST - `/upload`: Recebe as imagens capturadas e as salva em uma pasta local no servidor. 
- Rota POST - `/images`: Envia as imagens armazenadas na pasta local para o bucket do Supabase. 
Os arquivos são salvos com nomes únicos usando a função time.time() para evitar conflitos.

## Subscriber ROS:

Um código é fornecido para um subscriber em ROS (Robot Operating System).
Ele recebe frames de um vídeo em tempo real por meio do tópico video_frames.
Converte os frames recebidos em um formato adequado para o envio.
Utiliza uma requisição HTTP POST para enviar os frames para a rota /upload do backend.

## Publisher ROS:

Outro código é fornecido para um publisher em ROS.
Captura frames de um vídeo em tempo real e publica-os no tópico video_frames.
Utiliza o OpenCV para capturar e processar os frames.
Os frames são convertidos em mensagens do tipo sensor_msgs/Image e enviados através do ROS.
<br><br>
Dessa forma, a solução permite a captura de frames de um vídeo em tempo real, o envio desses frames por meio do ROS para o backend em FastAPI e o armazenamento adequado das imagens no Supabase. O uso do ROS possibilita uma integração eficiente entre o processo de captura de imagens e o backend de armazenamento.

## Link para o vídeo no Youtube:
<a href="https://youtu.be/digz1gy-q_k" > Backend para transmissão e armazenamento de imagens </a>
