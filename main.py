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

# ==========================
# CRUD DE CURSOS
# ==========================

# Criar curso
@app.post("/cursos", response_model=schemas.CursoResponse)
def criar_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    novo_curso = models.Curso(
        titulo=curso.titulo
    )

    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)

    return novo_curso


# Listar cursos
@app.get("/cursos", response_model=list[schemas.CursoResponse])
def listar_cursos(db: Session = Depends(get_db)):
    return db.query(models.Curso).all()

# ==========================
# MATRÍCULAS - SPRINT 2
# ==========================

# Criar matrícula
@app.post("/matriculas", response_model=schemas.MatriculaResponse)
def criar_matricula(
    matricula: schemas.MatriculaCreate,
    db: Session = Depends(get_db)
):
    nova_matricula = models.Matricula(
        aluno_id=matricula.aluno_id,
        curso_id=matricula.curso_id
    )

    db.add(nova_matricula)
    db.commit()
    db.refresh(nova_matricula)

    return nova_matricula

# Listar cursos de um aluno
@app.get("/alunos/{aluno_id}/cursos", response_model=list[schemas.CursoResponse])
def listar_cursos_do_aluno(
    aluno_id: int,
    db: Session = Depends(get_db)
):
    cursos = (
        db.query(models.Curso)
        .join(models.Matricula)
        .filter(models.Matricula.aluno_id == aluno_id)
        .all()
    )

    return cursos

# Listar alunos de um curso
@app.get("/cursos/{curso_id}/alunos", response_model=list[schemas.AlunoResponse])
def listar_alunos_do_curso(
    curso_id: int,
    db: Session = Depends(get_db)
):
    alunos = (
        db.query(models.Aluno)
        .join(models.Matricula)
        .filter(models.Matricula.curso_id == curso_id)
        .all()
    )

    return alunos