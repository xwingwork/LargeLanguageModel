from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.db import init_db
from api.chat.routing import router as chat_router
from api.weather.routing import router as weather_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db() # 創建與資料庫互動的物件
    yield

app=FastAPI(lifespan=lifespan)

app.include_router(chat_router,prefix="/api/chats")
app.include_router(weather_router,prefix="/api/weather")

@app.get("/")
def read_index():
    return {"Working!!!213"}