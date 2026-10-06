from fastapi import APIRouter, HTTPException

from redis_service import setValue, getValue

from config import Config

redisService = APIRouter()

@redisService.post('/')
async def getUrlShorten(url:str):

    if not url or not url.startswith(('http://', 'https://')):
        raise HTTPException(status_code=400, detail='URL must include http:// or https://')
    shortId = setValue(url)
    

    return f'http://localhost:{Config.port}/{shortId}'



