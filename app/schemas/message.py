from typing import Any

from pydantic import BaseModel


class Message(BaseModel):
    name: str
    message: Any
