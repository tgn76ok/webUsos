# Projeto Django README
## Introdução

Este projeto é uma aplicação web construída com Django, um framework web Python de alto nível. Ele utiliza Python 3.10 e inclui dependências como ASGIRef, Pillow e SQLParse. O objetivo da aplicação é fornecer uma plataforma robusta e escalável para desenvolvimento web.


### Requisitos
```bash


    Python 3.10
    Django 5.0.6
    Pillow 10.3.0
    ASGIRef 3.8.1
    SQLParse 0.5.0
```
## Instalação
### 1. Clonar o repositório

bash

git clone https://github.com/tgn76ok/webUsos.git
cd webUsos

### 2. Criar um ambiente virtual

É recomendado usar um ambiente virtual para gerenciar as dependências:

```bash
python3.10 -m venv venv
source venv/bin/activate
```
No Windows:

```bash
python3.10 -m venv venv
venv\Scripts\activate
```
### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 1. Configuração do banco de dados

Por padrão, o Django utiliza SQLite, que não requer configuração adicional. Se desejar usar outro banco de dados, atualize a configuração DATABASES em seuprojeto/settings.py.
### 2. Migrar o banco de dados



python manage.py migrate

#### 3. Criar um superusuário


```bash
python manage.py createsuperuser
```
### 4. Coletar arquivos estáticos

```
python manage.py collectstatic
```
## Executando o Projeto

Para iniciar o servidor de desenvolvimento, execute:

```
python manage.py runserver
```

Abra o navegador e navegue para http://127.0.0.1:8000/ para ver a aplicação em execução.
Uso

    Interface de Administração: Visite http://127.0.0.1:8000/admin/ e faça login com as credenciais do superusuário criadas anteriormente.
    Aplicação Principal: Acesse a funcionalidade principal da aplicação através da interface web.

Informações Adicionais
Dependências

   
    Django: O principal framework utilizado para desenvolver a aplicação web.
    Pillow: Biblioteca para tarefas de processamento de imagens.
    

Estrutura de Pastas

    manage.py: Utilitário de linha de comando que permite interagir com este projeto Django.
    seuprojeto/: Diretório do projeto contendo configurações, URLs e configurações WSGI/ASGI.
    nome_app/: Substitua pelo nome do seu aplicativo. Este diretório contém os modelos, visualizações e templates da sua aplicação Django.

Contribuição

Se você deseja contribuir para este projeto, siga estes passos:

    Faça um fork do repositório.
    Crie um novo branch para sua funcionalidade ou correção de bug.
    Faça commit das suas alterações e envie para seu fork.
    Crie um pull request com uma descrição das suas alterações.
