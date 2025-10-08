from vk_api.longpoll import VkLongPoll, VkEventType
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_URL = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_MASTER_CHAT_ID')

def send_message_to_telegram(user_name, message_text):
    message = f"📨 VK: {user_name}: {message_text}"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(TELEGRAM_BOT_URL, data=payload)

def main():
    vk_session = vk_api.VkApi(token=os.getenv('VK_GROUP_TOKEN'))
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            user_id = event.user_id
            user_info = vk_session.method('users.get', {'user_ids': user_id})
            user_name = user_info[0]['first_name']
            message_text = event.text

            send_message_to_telegram(user_name, message_text)

if __name__ == "__main__":
    main()