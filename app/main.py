from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings
from app.websocket.websocket import ws_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router)
app.include_router(ws_router)
