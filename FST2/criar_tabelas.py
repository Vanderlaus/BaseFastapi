from core.configs import settings
from core.database import engine
from models.aluno_models import AlunoModel

print('executando documento criar_tabelas')
async def create_tables():
    print('entrando na função')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabela criada com sucesso!')

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())