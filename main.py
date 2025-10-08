import logging
from config import TELEGRAM_MASTER_CHAT_ID
from bots.telegram_bot import start_telegram_bot

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the social manager application...")
    
    # Start the Telegram bot
    start_telegram_bot(TELEGRAM_MASTER_CHAT_ID)

if __name__ == "__main__":
    main()