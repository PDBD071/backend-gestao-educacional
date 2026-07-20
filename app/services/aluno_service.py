from fastapi import HTTPException
import models


def verificar_aluno(db, aluno_id):

    aluno = db.query(models.Aluno).filter(
        models.Aluno.id == aluno_id
    ).first()

    if aluno is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return aluno



def verificar_curso(db, curso_id):

    curso = db.query(models.Curso).filter(
        models.Curso.id == curso_id
    ).first()

    if curso is None:
        raise HTTPException(
            status_code=404,
            detail="Curso não encontrado"
        )

    return curso



def verificar_matricula_existente(db, aluno_id, curso_id):

    matricula = db.query(models.Matricula).filter(
        models.Matricula.aluno_id == aluno_id,
        models.Matricula.curso_id == curso_id
    ).first()

    if matricula:
        raise HTTPException(
            status_code=400,
            detail="Aluno já matriculado neste curso"
        )

    return True