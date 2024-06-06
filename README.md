# BookStation - Biblioteca
Sistema de gerenciamento de biblioteca.

## Features
* Cadastro de usuário <br>
* Cadastro de livros <br>
* Cadastro de clientes que poderão retirar os empréstimos de livros <br>
* Gerenciamento dos empréstimos <br>
* Sitema de busca individual <br>

## Tecnologias utilizadas:
* [Python 3](https://www.python.org/) - Linguagem de Programação
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Framework Web
* [VirtualEnv](https://virtualenv.pypa.io/en/latest/installation.html) - Ambiente de desenvolvimento isolado
* [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) - Framework de mapeamento objeto-relacional SQL
* [requestsHTTP](https://requests.readthedocs.io/en/latest/) - Framework cliente HTTP para python
* [bcrypt](https://pypi.org/project/bcrypt/) - Hashing de senha
* [mysqlconnector](https://dev.mysql.com/doc/connector-python/en/) - MySQL Connector/ODBC
* [MySQL](https://www.mysql.com/) - Gerenciador de banco de dados

## Modelo utilizado para o Banco de dados:
![image](https://github.com/MatheuzSiq/bookstation/assets/142842132/6ec3d920-0536-4346-b1e7-c7bdd19b84a6)


## Como executar o projeto:

### **1. Instale `Python` na sua máquina, por meio [deste link](https://www.python.org/)**

### **2. Faça um clone [desse repositório](https://github.com/MatheuzSiq/bookstation.git) na sua máquina:**
* Crie uma pasta no seu computador para esse programa, recomendo colocar o nome **BookStation**
* Abra o `git bash` ou `terminal` dentro dessa pasta
* Copie a [URL](https://github.com/MatheuzSiq/bookstation.git) do repositório
* Digite `git clone <URL copiada>` e pressione `enter`

### **3. Instale o virtualEnv e o inicie para criar uma ambiente isolado e instalar as dependencias:**
* Abra o terminal na pasta do projeto e digite o comando `python -m pip install --user virtualenv` (utilize python3 para linux)
* Execute o comando `python -m venv <nome da venv>` para criar um novo ambiente virtual (utilize python3 para linux)
* Logo após é necessário ativar o ambiente por meio do comando `.\<nome da venv>\Scripts\activate` no windows e `source env_name/bin/activate` no Linux

### **4. Instale as dependencias utilizadas no projeto:**
* Com o `venv` criado, fica muito mais facil de instalar as dependencias corretas para a execução do projeto.
* Basta ir no terminal e digitar o seguinte comando com o `venv` ativo: `pip freeze > requirements.txt`, desse modo todas as dependecias seram instaladas corretamente e na versão correta.

## **5. Configurações e adequações:**
* No arquivo `config.py` estão as configurações do banco de dados, esse arquivo tem que ser configurado
  * usuario=`usuario do MySQL`,
  * senha=`Senha do servidor`,
  * servidor=`nome do servidor, normalmente: localhost`,
* Feito isso, dentro do `MySQL` você poderá utilizar o código do arquivo `banco.sql` para criar o banco de dados utilizado pelo projeto
* Tenha em mente que o banco de dados já vem com alguns cadastros para que o projeto já tenha algo a ser mostrado.

## **6. Agora é só rodar o arquivo `main.py` e testar a aplicação.**




























