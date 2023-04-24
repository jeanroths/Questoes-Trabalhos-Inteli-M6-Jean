<img src="../assets/logo-inteli.png" alt="Logo do Inteli"/>

# Atividade 1: Turtlesim: simulando um ambiente robótico integrado no ROS

## Enunciado

Crie um script em Python capaz de interagir com o nó de simulação do turtlesim e enviar mensagens nos tópicos que regem a locomoção da tartaruga principal. Utilize este script para reproduzir um desenho de sua autoria. Utilize a estrutura de dados que preferir para representar a “imagem” a ser desenhada. O uso de programação orientada a objetos é obrigatório.

## Padrão de qualidade

Para esta atividade, espera-se a capacidade demonstrável de interagir com o sistema operacional de robôs, criando um nó de comunicação com uma solução pré-existente. A entrega deve ser um vídeo demonstrando o funcionamento do projeto, um texto conciso descrevendo como foi feita a implementação e o link para o repositório público no github onde foi feita a implementação.

Ao terminar esta atividade, espera-se que os estudantes consigam validar suas instalações locais do ambiente de desenvolvimento que será utilizado ao longo do semestre. A nota para esta atividade segue os critérios estabelecidos pelo Inteli e pode ser dividida em: 
- Configuração adequada do ambiente de desenvolvimento ROS;
- Funcionamento correto do script de interação com o turtlesim;
- Explicação coerente e concisa da implementação;
- Congruência entre o que foi escrito e o código disposto no repositório do github;

## Instruções:

### Instalação do WSL

Antes de mais nada, certifique-se que o módulo de Windows do WSL foi habilitado (versões mais novas do Windows já vem com o módulo habilitado). Para isso, abra o PowerShell com privilégios administrativos e execute o seguinte comando:

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

Esse comando faz alterações que requerem a reinicialização do sistema. Reinicie o computador antes de continuar.

Para garantir que a versão do WSL no seu computador é a mais atualizada possível, utilize o comando a seguir:
```powershell
wsl --update
```

A seguir, procure na Microsoft Store por `Ubuntu 22.04`, pois essa é a distribuição adequada para utilizar com o ROS Humble. Para instalá-la, basta clicar no botão "Obter" e aguardar a conclusão da instalação. Ao terminar instalação inicial, um terminal será aberto solicitando que faça as configurações iniciais do seu sistema Ubuntu. ***Não pule esta etapa***, pois é nela que o sistema criará a pasta HOME do seu usuário e o configurará como a conta padrão e pertencente ao grupo de usuários que podem usar o comando `sudo`.

Parabéns! Agora você tem uma versão de Ubuntu instalada dentro do conforto de seu sistema Windows =)

Mas calma, ainda não acabou. Antes de pularmos para a instalação do ROS, vamos rodar alguns comandos que vão garantir que seu Ubuntu está preparado para o desenvolvimento que faremos a seguir.

Primeiro, vamos atualizar o banco de dados de repositórios do apt com:
```bash
sudo apt update
```

A seguir, vamos atualizar todas as aplicações que não estão em sua versão mais nova com:
```bash
sudo apt upgrade
```

Pronto, agora vamos instalar alguns pacotes que vão ser importantes para nosso desenvolvimento. Para começar, vamos instalar um metapacote que agrega as ferramentas necessárias para compilação e desenvolvimento de software. Rode:
```bash
sudo apt install build-essential
```

Agora, vamos garantir que tudo o que vamos precisar de Python está no sistema. Rode:
```bash
sudo apt install python3 python3-pip python3-venv
```

Por fim, vamos instalar algumas outras ferramentas que podem ser úteis. Rode:
```bash
sudo apt install curl software-properties-common
```

Agora sim! Tudo certo para começarmos a instalação do ROS.

### Instalação do ROS2 Humble

Para instalar o ROS, precisamos adicionar novos repositórios ao apt, pois o ROS não se encontra nos repositórios padrão do Ubuntu. Para isso começaremos garantindo que o repositório `universe` está habilitado. Rode:

```bash
sudo apt-add-repository universe
```

A seguir, precisamos baixar uma chave GPG e adicioná-la ao keyring do sistema para poder validar o repositório que vamos adicionar. Rode:
```bash
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

Agora precisamos adicionar o repositório à lista de repositórios. Use:
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

Como fizemos alterações nos repositórios do apt, precisamos atualizar seu banco de dados novamente. Rode:

```
sudo apt update
```

Pronto! Agora estamos finalmente prontos para instalar a nossa distribuição de ROS. Para facilitar nossa vida, vamos escolher a versão do pacote mais completa, assim não precisaremos nos preocupar se os exemplos e pacotes que vamos precisar já estarão instalados ou não. Rode:

```bash
sudo apt install ros-humble-desktop
```

Essa instalação vai demorar alguns minutos, então tenha paciência =)

Falta apenas uma coisa para termos o poder do ROS em nossas mãos: por padrão, o ROS não adiciona automaticamente todos os executáveis e variáveis de ambiente ao nosso sistema, mas existe um script que faz todo esse setup para nós. Como ninguém tem tempo de ficar dando source nesse script toda vez, rodem esse comando para garantir que tudo vai estar configurado sempre que você abrir o terminal do WSL:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

Perfeito! Agora estamos prontos para trabalhar com o ROS2 Humble. Vamos testar?

Abra dois terminais e, para cada um deles vamos rodar um comando. Para o terminal 1:

```bash
ros2 run demo_nodes_cpp talker
```

Para o terminal 2:
```bash
ros2 run demo_nodes_cpp listener
```

Se tudo deu certo, você acabou de ver dois processos totalmente independentes conversando através da interface de comunicação do ROS. Legal, né? Para fechar as instruções necessárias, vamos apenas aprender a rodar nosso exemplo.

### Interagindo com o código de exemplo

Nesse repositório contamos com um [código de exemplo](./exemplo) para que vocês não partam do 0 em seu desenvolvimento. Para conseguir rodá-lo, basta fazer algumas coisinhas. Primeiro, navegar até a pasta do exemplo:

```bash
cd exemplo
```

Aqui você vai encontrar a seguinte estrutura:
```
.
└── exemplo
    ├── exemplo.py
    └── requirements.txt

1 directory, 2 files
```

O arquivo `exemplo.py` é um script utilizando OOP para interagir com o nó de simulação do turtlesim. Já o requirements.txt é o resultado de um comando `pip freeze` dentro de um venv utilizado para criar esse exemplo. Isso significa que ele tem todos os pacotes necessários para rodar o script. Vamos garantir que está tudo instalado com: 

```bash
pip install -r requirements.txt
```

OK! Agora estamos prontos para rodar o exemplo. Primeiro, abra um terminal e rode o comando necessário para inicializar o nó do turtlesim:
```bash
ros2 run turtlesim turtlesim_node
```

A seguir, basta rodar o script em outro terminal. Para isso, primeiro vamos garantir que ele está com permissão para execução:

```bash
chmod +x exemplo.py
```

Ok, agora basta rodar o script como se fosse um executável qualquer em Linux:

```bash
./exemplo.py
```

Pronto! Você já está preparado para começar a desenvolver seu autoestudo. Divirta-se! =D
