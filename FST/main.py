from fastapi import FastAPI, HTTPException, status
from models import Aluno
from fastapi import Response
from fastapi import Path

app = FastAPI()

@app.get('/')
async def raiz():
    return {"mensagem": "Seja Bem Vindo ao More Devs"}

alunos = {
    1: {"Nome":"Lirinha", "Idade":19, "E-mail":"lira@gmail.com"},
    2: {"Nome":"Thiago", "Idade":37, "E-mail":"thiago@gmail.com"},
    3: {"Nome":"Joao", "Idade":17, "E-mail":"joao@gmail.com"},
    4: {"Nome":"Vander", "Idade":41, "E-mail":"vanderlaus@gmail.com"},

}

@app.get('/alunos')
async def get_alunos():
    return alunos

# @app.get("/alunos/{aluno_id}")
# async def get_aluno(aluno_id:int):
#     try:
#         aluno = alunos[aluno_id]
#         return aluno
#     except KeyError:
#         raise HTTPException (
#             status_code = status.HTTP_404_NOT_FOUND, detail='Aluno nao encontrado.' 
#         )

@app.get("/alunos/{aluno_id}")
async def update(aluno_id:int):
    try:
        aluno = alunos[aluno_id]
        return aluno
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno nao encontrado."
        )

@app.post("/alunos", status_code=status.HTTP_201_CREATED)
async def post_aluno(aluno:Aluno):
    next_id : int = len(alunos) +1
    alunos[next_id] = aluno
    del aluno.id
    return aluno

@app.get('/calculadora/')
async def calcular(num1:int, num2:int, num3:int):
    soma = num1 + num2 + num3
    raise HTTPException(
        status_code=status.HTTP_200_OK detail=f"A soma de {num1}, {num2} e {num3} é {soma}"
    )

@app.put("/alunos/{aluno_id}")
async def put_aluno(aluno_id:int, aluno:Aluno):
    if aluno_id in alunos:
        alunos[aluno_id] = aluno
        del aluno.id
        return aluno
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno nao encontrado."
        )

@app.delete("/alunos/{aluno_id}")
async def delete_aluno(aluno_id:int):
    if aluno_id in alunos:
        del alunos[aluno_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
            #status_code=status.HTTP_200_OK, detail="Aluno deletado com sucesso."
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno nao encontrado."
        )

@app.get("/alunosnomes/{aluno_nome}")
async def get_Nomealuno(aluno_nome:str):
    for aluno in alunos.values():
        if aluno['Nome'] == aluno_nome:
            print(aluno['Nome'])
            return aluno

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port= 8000,
        log_level = "info",
        reload = True
    )