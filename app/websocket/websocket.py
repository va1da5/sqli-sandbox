from fastapi import APIRouter, WebSocket

from .controller import controller
from .events import *

ws_router = APIRouter()


@ws_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    controller.register(websocket)
    await controller.handle()
