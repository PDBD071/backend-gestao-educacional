from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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