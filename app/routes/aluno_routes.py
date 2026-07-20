from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal


router = APIRouter(
    prefix="/alunos",
    tags=["Alunos"]
)


# Abre e fecha conexão com banco
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



# Criar aluno
@router.post("/", response_model=schemas.AlunoResponse)
def criar_aluno(
    aluno: schemas.AlunoCreate,
    db: Session = Depends(get_db)
):

    novo_aluno = models.Aluno(
        nome=aluno.nome,
        email=aluno.email
    )

    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)

    return novo_aluno



# Listar alunos
@router.get("/", response_model=list[schemas.AlunoResponse])
def listar_alunos(
    db: Session = Depends(get_db)
):

    return db.query(models.Aluno).all()



# Buscar aluno por ID
@router.get("/{aluno_id}", response_model=schemas.AlunoResponse)
def buscar_aluno(
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

    return aluno



# Atualizar aluno
@router.put("/{aluno_id}", response_model=schemas.AlunoResponse)
def atualizar_aluno(
    aluno_id: int,
    aluno: schemas.AlunoCreate,
    db: Session = Depends(get_db)
):

    aluno_db = db.query(models.Aluno).filter(
        models.Aluno.id == aluno_id
    ).first()

    if aluno_db is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    aluno_db.nome = aluno.nome
    aluno_db.email = aluno.email

    db.commit()
    db.refresh(aluno_db)

    return aluno_db



# Excluir aluno
@router.delete("/{aluno_id}")
def excluir_aluno(
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

    db.delete(aluno)
    db.commit()

    return {
        "mensagem": "Aluno excluído com sucesso"
    }
    from app.controllers import aluno_controller


@router.post("/matriculas", response_model=schemas.MatriculaResponse)
def criar_matricula(
    matricula: schemas.MatriculaCreate,
    db: Session = Depends(get_db)
):

    return aluno_controller.criar_matricula(
        matricula,
        db
    )