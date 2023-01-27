from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

app = FastAPI()

@app.get('/')
async def raiz():
    return {"mensagem": "Seja bem vindo ao Moredevs2Blu"}

alunos = {
    1:{"Nome" : "Vander", "Idade" : "41", "Email" : "vanderlaus@hotmail.com"},
    2:{"Nome" : "Thiago", "Idade" : "33", "Email" : "thiago@hotmail.com"},
    3:{"Nome" : "João", "Idade" : "22", "Email" : "joao@hotmail.com"},
    4:{"Nome" : "Gisele", "Idade" : "24", "Email" : "gisele@hotmail.com"}
}

@app.get('/alunos')
async def get_alunos():
    return alunos

@app.get("/alunos/{aluno_id}")
async def get_aluno(aluno_id:int):
    try:
        aluno = alunos[aluno_id]
        alunos.update({"id" : aluno_id})
        return aluno

    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrato"
        )

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host= "127.0.0.1",
        port=8000,
        log_level = "info",
        reload= True
    )