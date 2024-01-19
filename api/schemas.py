from pydantic import BaseModel


class Phone(BaseModel):
    """Validate Phone"""

    phone: str
    # uname: str


class Message(BaseModel):
    """Validate Phone"""

    phone: str
    uname: str


class MessagePOST(BaseModel):
    """Validate Phone"""

    message_text: str
    from_phone: str
    username: str


class Goods(BaseModel):
    goods: str