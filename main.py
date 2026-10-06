from fastapi import FastAPI

from router import redisService 

app = FastAPI(
    title='URLshortner',
    description='url shortner service'
)


app.include_router(redisService,prefix='/api/shortner', tags=['shortner'])



def main():
    print("Hello from url-shortner!")


if __name__ == "__main__":
    main()
