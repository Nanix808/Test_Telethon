from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from api.router import api_router
from telethone_client import client


app = FastAPI()


# Telethon цикла событий равным циклу событий FastAPI.
@asynccontextmanager
async def lifespan(app: FastAPI):
    await client.start()
    yield
    await client.disconnect()


app = FastAPI(lifespan=lifespan)

# Добавляем роуты из папки api
app.include_router(api_router, prefix="/api", tags=["api_v1"])

app.mount("/static", StaticFiles(directory="static"), name="static")

# Запуск сервера Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
