# Backend CRUD - Sistema de Gestão Educacional

## Descrição

Este projeto foi desenvolvido como parte do desafio de Backend utilizando **FastAPI** e **SQLite**.

A aplicação permite o cadastro de alunos e cursos, além do gerenciamento de matrículas entre alunos e cursos por meio de uma API REST.

O projeto foi desenvolvido em quatro sprints, contemplando a implementação do CRUD de alunos, relacionamento entre tabelas, regras de negócio e organização do código seguindo uma arquitetura em camadas.

---

## Tecnologias Utilizadas

* Python 3
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
* Pydantic

---

## Estrutura do Projeto

```text
backend-gestao-educacional/
│
├── app/
│   ├── controllers/
│   │   ├── aluno_controller.py
│   │   ├── curso_controller.py
│   │   └── matricula_controller.py
│   │
│   ├── routes/
│   │   ├── aluno_routes.py
│   │   ├── curso_routes.py
│   │   └── matricula_routes.py
│   │
│   ├── services/
│   │   └── aluno_service.py
│   │
│   └── __init__.py
│
├── database.py
├── main.py
├── models.py
├── schemas.py
├── database.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/PDBD071/backend-gestao-educacional.git
```

### 2. Acessar a pasta do projeto

```bash
cd backend-gestao-educacional
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

**Windows**

```bash
venv\Scripts\activate
```

### 5. (Opcional) Atualizar o pip

```bash
python -m pip install --upgrade pip
```

### 6. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 7. Executar a aplicação

```bash
uvicorn main:app --reload
```

### 8. Acessar a documentação da API

Após iniciar a aplicação, acesse no navegador:

```text
http://127.0.0.1:8000/docs
```

---

## Configuração do Banco de Dados

O projeto utiliza o banco de dados **SQLite**.

A conexão é configurada no arquivo `database.py` por meio da variável:

```python
DATABASE_URL = "sqlite:///./database.db"
```

O arquivo `database.db` é criado automaticamente na primeira execução da aplicação.

---

## Endpoints Disponíveis

### Default

* GET /

### Alunos

* GET /alunos/
* POST /alunos/
* GET /alunos/{aluno_id}
* PUT /alunos/{aluno_id}
* DELETE /alunos/{aluno_id}

### Cursos

* GET /cursos/
* POST /cursos/

### Matrículas

* POST /matriculas/
* GET /matriculas/aluno/{aluno_id}/cursos
* GET /matriculas/curso/{curso_id}/alunos

---

## Regras de Negócio

A aplicação implementa as seguintes regras:

* Não permite matrícula duplicada no mesmo curso.
* Não permite matrícula para aluno inexistente.
* Não permite matrícula para curso inexistente.
* Retorna erro **404** para aluno ou curso não encontrado.
* Retorna erro **400** quando o aluno já está matriculado no curso.

---

## Autora

Projeto desenvolvido por **Keli Cristina Silva Martins** para o desafio **Backend – Banco de Dados + CRUD**.
