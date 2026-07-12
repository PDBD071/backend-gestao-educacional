from pydantic import BaseModel, EmailStr


class AlunoBase(BaseModel):
    nome: str
    email: EmailStr


class AlunoCreate(AlunoBase):
    pass


class AlunoResponse(AlunoBase):
    id: int

    class Config:
        from_attributes = True


class CursoBase(BaseModel):
    titulo: str


class CursoCreate(CursoBase):
    pass


class CursoResponse(CursoBase):
    id: int

    class Config:
        from_attributes = True


# ==========================
# MATRÍCULAS - SPRINT 2
# ==========================

class MatriculaBase(BaseModel):
    aluno_id: int
    curso_id: int


class MatriculaCreate(MatriculaBase):
    pass


class MatriculaResponse(MatriculaBase):
    id: int

    class Config:
        from_attributes = True

        # ==========================
# RELACIONAMENTOS - SPRINT 2
# ==========================

class CursoAlunoResponse(CursoResponse):
    pass


class AlunoCursoResponse(AlunoResponse):
    pass