from telethon import TelegramClient, events
from config import API_ID, API_HASH


client = TelegramClient("session_name", API_ID, API_HASH)

# Словарь в который будем записывать чаты
chat_dict = {"user_id": "user_id", "user_is_self": "user_is_self", "message": "message"}


# Обработчик для получения новых текстовых сообщений и добавление в словарь
@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    chat_id = event.chat_id
    message = event.raw_text
    user = await event.get_sender()
    user_id = []
    user_is_self = []
    print(user)
    if hasattr(user, "id"):
        user_id = user.id
    if hasattr(user, "is_self"):
        user_is_self = user.is_self
    # Добавляем сообщение в список текущего чата, если чата нет он создастся
    chat = chat_dict.setdefault(str(chat_id), [])
    chat.append({"user_id": user_id, "user_is_self": user_is_self, "message": message})
    print(chat)
