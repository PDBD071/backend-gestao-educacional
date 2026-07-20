import models
import schemas


def criar_curso(
    curso: schemas.CursoCreate,
    db
):

    novo_curso = models.Curso(
        titulo=curso.titulo
    )

    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)

    return novo_curso



def listar_cursos(db):

    return db.query(models.Curso).all()