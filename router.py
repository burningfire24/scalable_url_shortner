from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from redis_service import setValue, getValue

from config import Config

redisService = APIRouter()

@redisService.post('/')
async def getUrlShorten(url:str):
    
    if not url:
        raise HTTPException(status_code=305,detail='please provide valid URL')

    shortId = setValue(url)

    return f'http://localhost:{Config.port}/api/shortner/{shortId}'



@redisService.get('/{shortnerID}')
async def accessOriginalUrl(shortnerID:str):
    
    Original_url=getValue(shortnerID)
    return RedirectResponse(url=Original_url)