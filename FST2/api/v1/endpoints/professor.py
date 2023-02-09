from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.professor_models import ProfessorModel
from schemas.professor_schema import ProfessorSchema
from core.deps import get_session

router = APIRouter()

#Listando Professores
@router.get('/', response_model=List[ProfessorSchema])
async def get_professores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel)
        result = await session.execute(query)
        professores : List[ProfessorModel] = result.scalars().all()

        return JSONResponse(content=jsonable_encoder(professores))

#Listando Professores
@router.get('/{prof_id}', response_model=ProfessorSchema, status_code=status.HTTP_200_OK)
async def get_professor(prof_id:int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == prof_id)
        result = await session.execute(query)
        professor = result.scalar_one_or_none()
        if professor :
            return JSONResponse(content=jsonable_encoder(professor))
        else:
            HTTPException(detail='Professor não encontrado', status_code=status.HTTP_404_NOT_FOUND)

#Criando Professores
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProfessorSchema)
async def post_professor(professor: ProfessorSchema, db: AsyncSession = Depends(get_session)):
    novo_prof = ProfessorModel(nome=professor.nome, email=professor.email)
    db.add(novo_prof)
    await db.commit()
    return JSONResponse(content=jsonable_encoder(novo_prof))

#Editando Professores
@router.put('/{prof_id}', response_model=ProfessorSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_professor(prof_id: int, professor: ProfessorSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == prof_id)
        result = await session.execute(query)
        prof_up = result.scalar_one_or_none()
        if prof_up:
            prof_up.nome = professor.nome
            prof_up.email = professor.email
            await session.commit()
            return JSONResponse(content=jsonable_encoder(prof_up))
        else:
            raise HTTPException(detail='Professor não encontrado', status_code=status.HTTP_404_NOT_FOUND)

#Deletando Professores
@router.delete('/{prof_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_professor(prof_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == prof_id)
        result = await session.execute(query)
        prof_del = result.scalar_one_or_none()
        if prof_del:
            await session.delete(prof_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Professor não encontrado', status_code=status.HTTP_404_NOT_FOUND)