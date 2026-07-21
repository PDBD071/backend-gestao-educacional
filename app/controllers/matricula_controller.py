from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
import schemas


def criar_matricula(
    matricula: schemas.MatriculaCreate,
    db: Session
):

    # Verifica se o aluno existe
    aluno = db.query(models.Aluno).filter(
        models.Aluno.id == matricula.aluno_id
    ).first()

    if aluno is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    # Verifica se o curso existe
    curso = db.query(models.Curso).filter(
        models.Curso.id == matricula.curso_id
    ).first()

    if curso is None:
        raise HTTPException(
            status_code=404,
            detail="Curso não encontrado"
        )

    # Verifica matrícula duplicada
    matricula_existente = db.query(models.Matricula).filter(
        models.Matricula.aluno_id == matricula.aluno_id,
        models.Matricula.curso_id == matricula.curso_id
    ).first()

    if matricula_existente:
        raise HTTPException(
            status_code=400,
            detail="Aluno já matriculado neste curso"
        )

    # Cria matrícula
    nova_matricula = models.Matricula(
        aluno_id=matricula.aluno_id,
        curso_id=matricula.curso_id
    )

    db.add(nova_matricula)
    db.commit()
    db.refresh(nova_matricula)

    return nova_matricula