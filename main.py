from fastapi import FastAPI

from router1 import redisService 
from router2 import shortnerService

app = FastAPI(
    title='URLshortner',
    description='url shortner service'
)


app.include_router(redisService,prefix='/api/{version}/shortner', tags=['shortner'])
app.include_router(shortnerService,tags=['redirection'])



def main():
    print("Hello from url-shortner!")


if __name__ == "__main__":
    main()
