from telethon import TelegramClient, events
from config import API_ID, API_HASH


client = TelegramClient("session_name", API_ID, API_HASH)


# Обработчик для получения новых текстовых сообщений
@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    chat_id = event.chat_id
    message = event.raw_text
    print(chat_id, message)