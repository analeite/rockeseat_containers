# Aplicação Python CRUD com MySQL no Docker

Este projeto consiste em uma aplicação simples de linha de comando (CLI) desenvolvida em Python para gerenciamento de tarefas (CRUD). A aplicação e o banco de dados funcionam em ambientes isolados utilizando **Docker** e **Docker Compose**, comunicando-se por meio de uma rede personalizada e com persistência de dados via volumes.

---

## 🏗️ Arquitetura e Containers

O projeto sobe **2 containers** orquestrados pelo Docker Compose:

1. **`python_crud_app`**: Aplicação CLI em Python que oferece a interface do menu e manipula os dados.
2. **`mysql_db`**: Servidor de banco de dados MySQL 8.0 com saúde checada (*healthcheck*) para garantir disponibilidade antes da aplicação conectar.

ambos os containers comunicam-se de forma isolada através de uma rede bridge customizada chamada **`app_custom_network`**.

---

## 📂 Estrutura do Projeto

```text
.
├── app.py               # Código-fonte da aplicação Python
├── requirements.txt     # Dependências Python (mysql-connector-python)
├── Dockerfile           # Instruções de build da imagem Python
├── docker-compose.yml   # Orquestração dos containers, rede e volumes
├── .env.example         # Modelo para variáveis de ambiente
├── .env                 # Arquivo com as senhas reais (NÃO versionado)
├── .dockerignore        # Impede cópia de arquivos sensíveis na imagem
├── .gitignore           # Impede envio de credenciais para o Git
└── README.md            # Documentação do projeto