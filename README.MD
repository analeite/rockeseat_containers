# Aplicação Python CRUD com MySQL no Docker

Este projeto consiste em uma aplicação simples de linha de comando (CLI) desenvolvida em Python para gerenciamento de tarefas (CRUD). A aplicação e o banco de dados funcionam em ambientes isolados utilizando **Docker** e **Docker Compose**, comunicando-se por meio de uma rede personalizada e com persistência de dados via volumes.

---

## 🏗️ Arquitetura e Containers

O projeto sobe **2 containers** orquestrados pelo Docker Compose:

1. **`python_crud_app`**: Aplicação CLI em Python que oferece a interface do menu e manipula os dados.
2. **`mysql_db`**: Servidor de banco de dados MySQL 8.0 com verificação de saúde (*healthcheck*) para garantir disponibilidade antes da aplicação conectar.

Ambos os containers comunicam-se de forma isolada através de uma rede bridge customizada chamada **`app_custom_network`**.

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
```

---

## ⚙️ Pré-requisitos

Para rodar este projeto na sua máquina, é necessário possuir instalado:

- **Docker Desktop** (com suporte à virtualização ativado no Windows/Linux/macOS).
- **Git** (para clonar o repositório e versionar os arquivos).

---

## 🚀 Passo a Passo de Configuração

### 1. Clonar o repositório e acessar a pasta
Abra o terminal e execute:

```bash
git clone https://github.com/analeite/rockeseat_containers.git
cd rockeseat_containers
```

### 2. Configurar as Variáveis de Ambiente
Crie o arquivo `.env` a partir do arquivo de exemplo `.env.example`:

- **No Windows (PowerShell):**
  ```powershell
  Copy-Item .env.example .env
  ```

- **No Linux/macOS ou Git Bash:**
  ```bash
  cp .env.example .env
  ```

Abra o arquivo `.env` criado e edite os valores das senhas para definir suas credenciais seguras:

```env
MYSQL_ROOT_PASSWORD=sua_senha_root_segura
MYSQL_DATABASE=app_db
MYSQL_USER=app_user
MYSQL_PASSWORD=sua_senha_app_segura

DB_HOST=db
DB_PORT=3306
```

---

## 🛠️ Comandos para Executar e Gerenciar os Containers

### 1. Construir e subir os containers em segundo plano
Suba os containers da aplicação e do banco de dados (a flag `--build` força a reconstrução da imagem Python com as alterações mais recentes):

```bash
docker compose up -d --build
```

### 2. Interagir com a aplicação Python (CLI)
Como a aplicação é executada via terminal de linha de comando, conecte o seu terminal atual ao container para exibir o menu do CRUD:

```bash
docker attach python_crud_app
```
*(Para sair da aplicação, selecione a opção de encerramento dentro do menu ou pressione `Ctrl + C`).*

### 3. Verificar o status e a saúde dos containers
Exiba a lista dos containers em execução e o status de verificação de saúde do MySQL (*healthcheck*):

```bash
docker compose ps
```

### 4. Visualizar os logs dos serviços
Para acompanhar a execução do banco ou da aplicação em tempo real:

```bash
# Exibir logs de todos os containers
docker compose logs -f

# Exibir logs apenas da aplicação Python
docker compose logs -f app

# Exibir logs apenas do servidor MySQL
docker compose logs -f db
```

### 5. Reiniciar os serviços
Para reiniciar os containers sem perder os dados gravados no banco:

```bash
docker compose restart
```

---

## 🧪 Testando a Conexão e Comunicação entre Containers

### 1. Testar a conectividade na rede interna do Docker
Execute um comando dentro do container da aplicação Python para testar se ele enxerga o container do MySQL através do nome da rede `db`:

```bash
docker exec -it python_crud_app ping db -c 3
```

### 2. Testar a persistência de dados no Volume
1. Conecte no app via `docker attach python_crud_app` e crie um novo registro de tarefa.
2. Reinicie os containers executando `docker compose restart`.
3. Conecte-se novamente e liste as tarefas: os registros criados permanecerão salvos no volume `mysql_data`.

---

## 🛑 Comandos para Parar e Remover os Containers

### Parar os containers mantendo os dados do banco salvos
```bash
docker compose down
```

### Remover tudo (containers, redes e os dados do volume do MySQL)
```bash
docker compose down -v
```