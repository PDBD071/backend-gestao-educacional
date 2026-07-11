from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, SessionLocal, engine

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Cria a aplicação
app = FastAPI()


# Abre e fecha a conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rota inicial
@app.get("/")
def inicio():
    return {"mensagem": "API de Alunos funcionando!"}


# ==========================
# CRUD DE ALUNOS
# ==========================

# Criar aluno
@app.post("/alunos", response_model=schemas.AlunoResponse)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    novo_aluno = models.Aluno(
        nome=aluno.nome,
        email=aluno.email
    )

    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)

    return novo_aluno


# Listar alunos
@app.get("/alunos", response_model=list[schemas.AlunoResponse])
def listar_alunos(db: Session = Depends(get_db)):
    return db.query(models.Aluno).all()
@app.get("/alunos/{aluno_id}", response_model=schemas.AlunoResponse)
def buscar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()

    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    return aluno
# Atualizar aluno
@app.put("/alunos/{aluno_id}", response_model=schemas.AlunoResponse)
def atualizar_aluno(
    aluno_id: int,
    aluno: schemas.AlunoCreate,
    db: Session = Depends(get_db)
):
    aluno_db = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()

    if aluno_db is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    aluno_db.nome = aluno.nome
    aluno_db.email = aluno.email

    db.commit()
    db.refresh(aluno_db)

    return aluno_db
# Excluir aluno
@app.delete("/alunos/{aluno_id}")
def excluir_aluno(
    aluno_id: int,
    db: Session = Depends(get_db)
):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()

    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    db.delete(aluno)
    db.commit()

    return {"mensagem": "Aluno excluído com sucesso"}