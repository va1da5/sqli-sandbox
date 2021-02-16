import json

from fastapi import WebSocket

from app.schemas.message import Message


class Controller:

    event_registry = {}

    def register(self, websocket: WebSocket):
        self.websocket = websocket

    def _parse_event(self, data: str) -> Message:
        return Message(**json.loads(data))

    def _handle_event(self, message: Message):
        controller = self.event_registry.get(message.name, self._not_found)
        return controller(**message.message)

    def _not_found(self, *args, **kwargs):
        return "Event not found"

    async def handle(self):
        await self.websocket.accept()
        while True:
            data = await self.websocket.receive_text()
            try:
                message = self._parse_event(data)
                response = self._handle_event(message)
                if response:
                    await self.websocket.send_text(
                        json.dumps(response, indent=4, sort_keys=True, default=str)
                    )
            except Exception as exc:
                await self.websocket.send_text(str(exc))

    def event(self, name):
        def decorator(function):
            self.event_registry[name] = function
            return function

        return decorator


controller = Controller()
