from fastapi import Depends
from sqlalchemy.orm import Session

import models
import schemas

from app.services import aluno_service


def criar_matricula(
    matricula: schemas.MatriculaCreate,
    db: Session
):

    # Verifica regras de negócio
    aluno_service.verificar_aluno(
        db,
        matricula.aluno_id
    )

    aluno_service.verificar_curso(
        db,
        matricula.curso_id
    )

    aluno_service.verificar_matricula_existente(
        db,
        matricula.aluno_id,
        matricula.curso_id
    )


    nova_matricula = models.Matricula(
        aluno_id=matricula.aluno_id,
        curso_id=matricula.curso_id
    )

    db.add(nova_matricula)
    db.commit()
    db.refresh(nova_matricula)

    return nova_matricula