from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas

from database import SessionLocal
from app.controllers import curso_controller


router = APIRouter(
    prefix="/cursos",
    tags=["Cursos"]
)


# Abre e fecha conexão com banco
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



# Criar curso
@router.post("/", response_model=schemas.CursoResponse)
def criar_curso(
    curso: schemas.CursoCreate,
    db: Session = Depends(get_db)
):

    return curso_controller.criar_curso(
        curso,
        db
    )



# Listar cursos
@router.get("/", response_model=list[schemas.CursoResponse])
def listar_cursos(
    db: Session = Depends(get_db)
):

    return curso_controller.listar_cursos(
        db
    )