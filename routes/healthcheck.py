import asyncio

from fastapi import APIRouter

router = APIRouter(prefix='/api')


@router.get("/healthcheck")
async def healthcheck() -> dict:
    return {'status': 'ok'}


@router.post("/load/{seconds}")
async def dummy_load(seconds: int) -> dict:
    """
    seconds: Количество секунд эмулируемой CPU-нагрузки
    """
    await asyncio.sleep(seconds)
    return {'status': 'ok'}
