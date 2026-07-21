from fastapi import FastAPI

from database import Base, engine

from app.routes import aluno_routes
from app.routes import curso_routes
from app.routes import matricula_routes


# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)


# Cria a aplicação
app = FastAPI()


# Rota inicial
@app.get("/")
def inicio():
    return {
        "mensagem": "API de Alunos funcionando!"
    }


# Conecta as rotas organizadas
app.include_router(aluno_routes.router)
app.include_router(curso_routes.router)
app.include_router(matricula_routes.router)