from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas

from database import SessionLocal
from app.controllers import matricula_controller


router = APIRouter(
    prefix="/matriculas",
    tags=["Matrículas"]
)


# Abre e fecha conexão com banco
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



# Criar matrícula
@router.post("/", response_model=schemas.MatriculaResponse)
def criar_matricula(
    matricula: schemas.MatriculaCreate,
    db: Session = Depends(get_db)
):

    return matricula_controller.criar_matricula(
        matricula,
        db
    )



# Listar cursos de um aluno
@router.get("/aluno/{aluno_id}/cursos", response_model=list[schemas.CursoResponse])
def listar_cursos_do_aluno(
    aluno_id: int,
    db: Session = Depends(get_db)
):

    aluno = db.query(models.Aluno).filter(
        models.Aluno.id == aluno_id
    ).first()

    if aluno is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )


    cursos = (
        db.query(models.Curso)
        .join(models.Matricula)
        .filter(models.Matricula.aluno_id == aluno_id)
        .all()
    )

    return cursos



# Listar alunos de um curso
@router.get("/curso/{curso_id}/alunos", response_model=list[schemas.AlunoResponse])
def listar_alunos_do_curso(
    curso_id: int,
    db: Session = Depends(get_db)
):

    curso = db.query(models.Curso).filter(
        models.Curso.id == curso_id
    ).first()

    if curso is None:
        raise HTTPException(
            status_code=404,
            detail="Curso não encontrado"
        )


    alunos = (
        db.query(models.Aluno)
        .join(models.Matricula)
        .filter(models.Matricula.curso_id == curso_id)
        .all()
    )

    return alunos