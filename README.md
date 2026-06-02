# 🚀 learning_fastapi_python

Repositório de aprendizado do **FastAPI** — um framework web moderno, rápido e de alta performance para construir APIs com Python.

---

## 📋 Pré-requisitos

- **Python 3.14.4** ou superior → [python.org/downloads](https://www.python.org/downloads/)
- **pip** (já incluso no Python 3.4+)
- **Git** (opcional, para clonar o repositório)

Verifique sua versão do Python:

```bash
python3 --version
# Python 3.14.4
```

---

## 📁 Estrutura do Projeto

```
learning_fastapi_python/
├── .venv/               # Ambiente virtual (não versionado)
├── main.py              # Ponto de entrada da aplicação
├── requirements.txt     # Dependências do projeto
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
pip install "fastapi[standard]"
```

Ou, se o projeto já tiver um `requirements.txt`:

```bash
pip install -r requirements.txt
```

Para gerar/atualizar o `requirements.txt` com as dependências atuais:

```bash
pip freeze > requirements.txt
```

---

## 🔧 Exemplo Mínimo

Crie um arquivo `main.py` com o seguinte conteúdo:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

---

## ▶️ Executando o Servidor

### Modo de desenvolvimento (com hot reload)

```bash
fastapi dev main.py
```

> O servidor reinicia automaticamente a cada alteração nos arquivos — ideal para desenvolvimento.

### Modo de produção

```bash
fastapi run main.py
```

Você verá uma saída similar a:

```
INFO     Using path main.py
INFO     Resolved absolute path /path/to/main.py
INFO     Searching for package file structure from directories with __init__.py files
INFO     Importing from /path/to/learning_fastapi_python

 ╭─ Python module file ─╮
 │                       │
 │  🐍 main.py           │
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

## 📖 Documentação Interativa

O FastAPI gera documentação automática a partir das suas rotas e type hints.

| Interface | URL | Descrição |
|-----------|-----|-----------|
| **Swagger UI** | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) | Documentação interativa — permite testar endpoints diretamente no browser |
| **ReDoc** | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) | Documentação alternativa, mais legível |
| **OpenAPI JSON** | [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json) | Schema OpenAPI bruto em JSON |

---

## 🛑 Encerrando o Servidor

Pressione `CTRL + C` no terminal para parar o servidor.

---

## 💤 Desativando o Ambiente Virtual

Quando terminar de trabalhar:

```bash
deactivate
```

---

## 📦 Dependências Principais

| Pacote | Descrição |
|--------|-----------|
| `fastapi` | Framework principal |
| `uvicorn` | Servidor ASGI (instalado junto com `fastapi[standard]`) |
| `pydantic` | Validação de dados via type hints (incluso no FastAPI) |

---

## 🔗 Recursos Úteis

- 📚 [Documentação oficial do FastAPI](https://fastapi.tiangolo.com/)
- 🐍 [Documentação do Python 3.14](https://docs.python.org/3.14/)
- 🌐 [Pydantic Docs](https://docs.pydantic.dev/)
- 🎓 [FastAPI Tutorial — Primeiros Passos](https://fastapi.tiangolo.com/tutorial/first-steps/)

---

## 📝 Licença

Este repositório é para fins de aprendizado. Fique à vontade para usar e modificar.
