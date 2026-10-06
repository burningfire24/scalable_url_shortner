from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from redis_service import getValue

shortnerService=APIRouter()



@shortnerService.get('/{shortnerID}')
async def accessOriginalUrl(shortnerID:str):
    
    Original_url=getValue(shortnerID)
    if Original_url is None:
        raise HTTPException(status_code=404,detail="url not found")
    return RedirectResponse(url=Original_url,status_code=302)