from sqlalchemy.orm import Session

import models
import schemas


def criar_curso(
    curso: schemas.CursoCreate,
    db: Session
):

    novo_curso = models.Curso(
        titulo=curso.titulo
    )

    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)

    return novo_curso


def listar_cursos(
    db: Session
):

    return db.query(models.Curso).all()