from fastapi import FastAPI
from fastapi import HTTPException, status
from models import Aluno, alunos
from fastapi import Response
from typing import Optional, Dict, List, Any
from fastapi import Path, Query, Header, Depends
from time import sleep

app = FastAPI(
    title="MoreDevs2Blu",
    version='0.1.0',
    description='Desenvolvido pela melhor turma de Python do Sul do Mundo',
)

def db():
    try:
        print('conexão com o banco')
        sleep(1)
    finally:
        print('conexão com o banco')
        sleep(1)

@app.get('/')
async def raiz():
    return {"mensagem": "Seja Bem Vindo ao More Devs"}

@app.get('/alunos', 
    description='lista de todos alunos', 
    summary='retorno substantivo',
    response_description='Lista de Alunos cadastrados',
    )
async def get_alunos():
    return alunos

@app.get('/alunos/{aluno_id}',
    description='lista um aluno específico', 
    summary='retorno indivíduo',
    response_description='Lista de um Aluno cadastrado',
    )
async def get_aluno(aluno_id:int = Path(default=None, title='ID Aluno', description='deve ser entre 1 ou 2', gt=0, lt=7), db: Any = Depends(db)):
    try:
        aluno = alunos[aluno_id - 1]
        return aluno
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado."
        )

@app.post("/alunos", 
    status_code=status.HTTP_201_CREATED, 
    description='cadastro de aluno', 
    summary='inclusao de indivíduo',
    response_description='Cadastro de Aluno',
    )
async def post_aluno(aluno:Aluno):
    next_id : int = len(alunos) +1
    aluno.id = next_id
    alunos.append(aluno)
    return aluno

@app.put("/alunos/{aluno_id}", 
    description='atualização de dados do aluno', 
    summary='atualiza um indivíduo',
    response_description='Atualiza cadastro do Alunos',
    )
async def put_aluno(aluno_id:int, aluno:Aluno):
    if aluno_id in aluno:
        alunos[aluno_id] = aluno
        del aluno.id
        return aluno
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno nao encontrado."
        )

@app.delete("/alunos/{aluno_id}", 
    description='deleta um aluno', 
    summary='deleta um indivíduo',
    response_description='Deleta Aluno cadastrado',
    )
async def delete_aluno(aluno_id:int):
    if aluno_id in alunos:
        del alunos[aluno_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno nao encontrado."
        )

#@app.get("/alunosnomes/{aluno_nome}", 
#    description='lista o aluno pelo nome', 
#    summary='retorno indivíduo',
#    response_description='Lista de Aluno pelo nome',
#    )
#async def get_Nomealuno(aluno_nome:str):
#    for aluno in alunos.values():
#        if aluno['Nome'] == aluno_nome:
#            print(aluno['Nome'])
#            return aluno



@app.get('/calculadora/',
    description='calcula valores da url', 
    summary='retorno resultado da soma',
    response_description='Resultado da soma dos valores',
    )
async def calcular(num1:int = Query(default=None, gt=5), num2:int = Query(default=None, gt=5), xdevs:str = Header(default=None), num3: Optional[int] = None):
    soma = num1 + num2
    if num3:
        soma = soma + num3
    print(f'devs: {xdevs}')
    return soma

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port= 8000,
        log_level = "info",
        reload = True
    )