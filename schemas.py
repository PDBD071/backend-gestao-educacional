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