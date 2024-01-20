import io
from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
import qrcode
from telethon import errors

from telethone_client import client, chat_dict
from api.schemas import Phone, Message, MessagePOST, Goods
from config import templates, BASE_URL
from wildberries import parse_wildberries

api_router = APIRouter()


# Рендерим главную страницу
@api_router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# Рендерим страницу authorization
@api_router.get("/authorization", response_class=HTMLResponse)
async def authorization(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


# На вход прилетает номер телефона и отправляет его в web и telegramm
@api_router.post("/login")
async def qr_code(phone: str = Form(...)):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"{BASE_URL}api/check/login?phone={phone}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    stream = io.BytesIO()
    img.save(stream)
    stream.seek(0)
    # отправляем в telegramm
    await client.send_file(phone, stream, caption="Login QR Code", force_document=True)
    stream.seek(0)
    # отправляем в web
    return StreamingResponse(stream, media_type="image/png")


# На вход прилетает номер телефона и и получаем статус авторизации waiting_qr_login, logined or error
@api_router.get("/check/login")
async def check_login(phone: Phone = Depends()):
    if phone:
        if phone:
            return JSONResponse({"status": "logined"}, status_code=200)
        else:
            return JSONResponse({"status": "waiting_qr_login"}, status_code=200)
    else:
        return JSONResponse({"status": "error"}, status_code=200)


# Получить сообщения по чату
@api_router.get("/messages")
async def get_messages(response: Message = Depends()):
    return JSONResponse(
        {"data": chat_dict.get(response.uname, [])[:50]}, status_code=200
    )


# Отправить сообщения другому пользователю
@api_router.post("/messages")
async def post_messages(request: MessagePOST):
    try:
        await client.send_message(request.username, request.message_text)
        return JSONResponse({"status": "ok"}, status_code=200)
    except errors.FloodWaitError as e:
        return JSONResponse({"status": e}, status_code=200)


@api_router.get("/wild")
async def get_goods(goods: Goods = Depends()):
    data = parse_wildberries(goods.goods)
    return JSONResponse(data, status_code=200)
