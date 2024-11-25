-- Sistema de Aluguel de Carros (Arquitetura Cliente-Servidor) --

-- Nomes dos Integrantes --
- José Henrique Bruhmuller
- João Pedro Ferreira Sperandio 

-- Arquitetura do Software --
- Cliente-Servidor: O cliente envia solicitações de consulta ou aluguel de veículos, e o servidor responde com as informações solicitadas, interagindo com um banco de dados relacional (MariaDB).

-- Tecnologias Utilizadas --
1. Linguagens:
   - Python 3.10 ou superior
2. Bibliotecas Python:
   - `socket` (para comunicação entre cliente e servidor)
   - `mysql-connector-python` (para integração com o banco de dados MariaDB)
   - `threading` (para execução de múltiplas tarefas simultâneas)
   - `queue` (para gerenciamento de mensagens)
   - `time` (para manipulação de temporizadores)
3. Banco de Dados:
   - MariaDB (via XAMPP)
4. Ambiente de Desenvolvimento:
   - Visual Studio Code (VS Code)

-- Descrição do Software --
Este software é um sistema de aluguel de carros que permite:
1. Consulta de Disponibilidade: O cliente pode verificar se há carros disponíveis para aluguel.
2. Aluguel de Veículos: O cliente pode reservar um carro específico, e o servidor atualiza a disponibilidade no banco de dados.
3. Gerenciamento via Banco de Dados: As informações de veículos são armazenadas em um banco de dados MariaDB.

-- Fluxo Básico --
1. Cliente envia uma mensagem ao servidor solicitando uma operação.
2. O servidor interpreta a mensagem e interage com o banco de dados para fornecer uma resposta.
3. O cliente recebe a resposta do servidor.

-- Protocolo de Comunicação --
1. Estrutura das Mensagens
As mensagens trocadas seguem o formato: `COMANDO|DADOS`.

2. Exemplos de Mensagens
  1. Consulta de Disponibilidade:
     - Cliente → Servidor: `CONSULTA|SUV`
     - Servidor → Cliente: `DISPONÍVEL|SUV` ou `INDISPONÍVEL|SUV`
  2. Solicitação de Aluguel:
     - Cliente → Servidor: `ALUGUEL|SUV`
     - Servidor → Cliente: `CONFIRMADO|SUV` ou `FALHA|SUV`
  3. Encerramento da Conexão:
     - Cliente → Servidor: `ADEUS`


-- Como Configurar e Executar o Sistema --

Pré-requisitos
1. Instalar Python:
   - Faça o download e instale Python 3.10 ou superior de [python.org](https://www.python.org/downloads/).

2. Instalar o XAMPP:
   - Faça o download e instale o XAMPP de [apachefriends.org](https://www.apachefriends.org/).
   - Inicie o MariaDB pelo painel de controle do XAMPP.

3. Configurar o Banco de Dados:
   - Acesse o Shell do XAMPP.
   - Crie o banco de dados e a tabela com o seguinte script SQL:
     ```
     CREATE DATABASE AluguelCarros;

     USE AluguelCarros;

     CREATE TABLE Veiculos (
         id INT AUTO_INCREMENT PRIMARY KEY,
         modelo VARCHAR(50) NOT NULL,
         quantidade INT NOT NULL
     );

     INSERT INTO Veiculos (modelo, quantidade) VALUES
     ('SUV', 2),
     ('Sedan', 3),
     ('Hatch', 1);
     ```

-- Passo a Passo --

1. Instale as Bibliotecas Python:
   No terminal do VS Code, execute:
   ```
      pip install mysql-connector-python
   ```
2. Configure o Código:
   No arquivo conexao_bd.py, insira as credenciais corretas para o banco de dados:
   ```
      "user="root"         # Usuário padrão do MariaDB
      password=""         # Senha padrão no XAMPP (vazia)"
   ```
3. Obtenha os IPs das Máquinas:
  Execute meuIP.py para descobrir os IPs das máquinas.

4. Configure o IP no Arquivo Principal:
  No início do aluguel_carros.py, substitua ip_destino pelo IP da máquina com a qual deseja se conectar.

5. Execute o Sistema:
  Abra dois terminais: um para o servidor e outro para o cliente.
  Execute o comando:
  ```
    python aluguel_carros.py
  ```


-- Reproduzindo o Sistema --

1. Servidor:
  Execute o script aluguel_carros.py na máquina que atuará como servidor.
  O servidor aguarda conexões e gerencia o banco de dados.

2. Cliente:
  Execute o script aluguel_carros.py na máquina cliente.
  O cliente envia solicitações ao servidor para consultar ou alugar veículos.

3. Teste o Sistema:
  Cliente solicita disponibilidade: CONSULTA|SUV.
  Servidor responde: DISPONÍVEL|SUV ou INDISPONÍVEL|SUV.
  Cliente solicita aluguel: ALUGUEL|SUV.
  Servidor confirma: CONFIRMADO|SUV ou indica falha: FALHA|SUV.

4. Encerrando Conexões:
  Digite ADEUS para finalizar a comunicação.
