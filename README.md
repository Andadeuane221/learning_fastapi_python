# 🚀 learning_fastapi_python

Repositório de aprendizado do **FastAPI** — construindo uma API RESTful completa, moderna e segura com Python, PostgreSQL e SQLAlchemy 2.0.

---

## ✨ Funcionalidades Implementadas

- **CRUD Completo:** Criação, leitura, atualização e exclusão de postagens.
- **Banco de Dados Relacional:** Integração com PostgreSQL utilizando o moderno **SQLAlchemy 2.0**.
- **Autenticação e Segurança:** - Geração e verificação de tokens **JWT** (utilizando `PyJWT`).
  - Hashing seguro de senhas com **Argon2** (utilizando `pwdlib`).
- **Arquitetura Escalável:** Código refatorado e dividido em `routers` (Rotas para Usuários, Posts e Autenticação).
- **Validação de Dados:** Schemas estritos utilizando **Pydantic v2**.

---

## 📋 Pré-requisitos

- **Python 3.14.4** ou superior → [python.org/downloads](https://www.python.org/downloads/)
- **PostgreSQL** instalado e rodando localmente (ou em nuvem).
- **pip** (já incluso no Python 3.4+)

---

## 📁 Estrutura do Projeto

O projeto foi reestruturado para manter a escalabilidade, separando responsabilidades:

```text
learning_fastapi_python/
├── app/
│   ├── routers/         # Rotas da aplicação (Endpoints)
│   │   ├── __init__.py
│   │   ├── auth.py      # Login e autenticação
│   │   ├── post.py      # Operações de CRUD de posts
│   │   └── user.py      # Criação e gestão de usuários
│   ├── __init__.py
│   ├── .env             # Variáveis de ambiente (NÃO VERSIONADO)
│   ├── database.py      # Conexão e engine do SQLAlchemy
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── models.py        # Modelos de tabelas do banco de dados
│   ├── oauth2.py        # Lógica de geração e validação de JWT
│   ├── schemas.py       # Modelos de validação do Pydantic
│   └── utils.py         # Funções utilitárias (ex: hash de senhas)
├── venv/                # Ambiente virtual (não versionado)
├── .gitignore
└── README.md
```

---

## ⚙️ Configuração do Ambiente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/learning_fastapi_python.git
cd learning_fastapi_python
```

### 2. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

### 3. Ative o ambiente virtual

**Linux / macOS:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

> Após ativar, o prompt do terminal mostrará `(.venv)` no início.

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure as Variáveis de Ambiente

Crie um arquivo chamado `.env` dentro da pasta `app/` e adicione as seguintes variáveis com os dados do seu banco PostgreSQL e uma chave secreta para o JWT:

```
DB_HOST=localhost
DB_NAME=fastapi
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui

SECRET_KEY=gere_uma_chave_secreta_longa_e_aleatoria_aqui
```

---

## ▶️ Executando o Servidor

Como a aplicação agora está dentro da pasta `app/`, o comando de execução mudou.

Modo de desenvolvimento (com hot reload)
No terminal, na raiz do projeto (fora da pasta app), execute:

```bash
fastapi dev main.py
```

ou

```bash
python -m fastapi dev
```
(Alternativa usando Uvicorn diretamente: uvicorn app.main:app --reload)

> O servidor reinicia automaticamente a cada alteração nos arquivos — ideal para desenvolvimento.

Você verá uma saída similar a:

```
INFO     Using path main.py
INFO     Resolved absolute path /path/to/main.py
INFO     Searching for package file structure from directories with __init__.py files
INFO     Importing from /path/to/learning_fastapi_python

 ╭─ Python module file ──╮
 │                       │
 │     🐍main.py         │
 │                       │
 ╰───────────────────────╯

INFO     Importing module main
INFO     Found importable FastAPI app

 ╭─ Importable FastAPI app ─╮
 │                           │
 │  from main import app     │
 │                           │
 ╰───────────────────────────╯

INFO     Using import string main:app

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                      │
 │  Serving at: http://127.0.0.1:8000                   │
 │  API docs:   http://127.0.0.1:8000/docs              │
 │                                                      │
 │  Running in development mode, for production use:    │
 │  fastapi run                                         │
 │                                                      │
 ╰──────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/path/to/project']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process using WatchFiles
```

---

### 🛑 Encerrando o Servidor

Pressione `CTRL + C` no terminal para parar o servidor.

---

### 💤 Desativando o Ambiente Virtual

Quando terminar de trabalhar:

```bash
deactivate
```

---

## 📖 Documentação Interativa

O FastAPI gera documentação automática a partir das suas rotas e type hints.

| Interface | URL | Descrição |
|-----------|-----|-----------|
| **Swagger UI** | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) | Documentação interativa — permite testar os endpoints com o Token JWT. |
| **ReDoc** | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) | Documentação alternativa, mais focada em leitura. |

---

## 📦 Dependências Principais (Atualizadas)

| Pacote | Descrição |
|--------|-----------|
| `fastapi` | Framework principal web |
| `sqlalchemy` | ORM para comunicação com o banco de dados (Versão 2.0+) |
| `psycopg` | Driver moderno para conexão com PostgreSQL |
| `pwdlib[argon2]` | Biblioteca atualizada para hash seguro de senhas |
| `PyJWT` | Geração e decodificação moderna de tokens JWT |
| `python-dotenv` | Carregamento seguro de variáveis de ambiente do .env |
| `uvicorn` | Servidor ASGI (instalado junto com `fastapi[standard]`) |
| `pydantic` | Validação de dados via type hints (incluso no FastAPI) |

---

## 🔗 Recursos Úteis

- 📚 [Documentação oficial do FastAPI](https://fastapi.tiangolo.com/)
- 🐍 [Documentação do Python 3.14](https://docs.python.org/3.14/)
- 🌐 [Pydantic Docs](https://docs.pydantic.dev/)
- 🎓 [FastAPI Tutorial — Primeiros Passos](https://fastapi.tiangolo.com/tutorial/first-steps/)
- ▶️ [Python API Development - Comprehensive Course for Beginners](https://youtu.be/0sOvCWFmrtA)

---

## 📝 Licença

Este repositório é para fins de aprendizado. Fique à vontade para usar e modificar.
