from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def pong():
    # тут можуть бути деякі асинхронні операції
    # приклад: `notes = await get_all_notes()`
    return {"ping": "pong!"}