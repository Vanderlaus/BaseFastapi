from typing import Optional
from pydantic import BaseModel, validator

class Aluno(BaseModel):
    id : Optional[int] = None
    nome : str
    idade : int
    email : str

    @validator('nome')
    def validar_nome(cls, value:str):
        abacate = value.split(' ')
        if len(abacate) < 3:
            raise ValueError('O Nome deve ter no mínimo 3 espaços')
        return value

alunos = [
    Aluno(id=1, nome="Vander Luis Lauschner Caralho", idade=41, email="vanderlaus@hotmail.com"),
    Aluno(id=2, nome="Luis Marcos Paulo", idade=31, email="vanderlauschner@gmail.com")
]