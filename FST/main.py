from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return {"mensagem": "Seja bem vindo ao Moredevs2Blu"}

alunos = {
    1:"Vander",
    2:"Lirinha",
    3:"Thiago",
    4:"Gisele"
}

@app.get('/alunos')
async def get_alunos():
    return alunos

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host= "127.0.0.1",
        port=8000,
        log_level = "info",
        reload= True
    )