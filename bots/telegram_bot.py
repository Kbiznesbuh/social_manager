from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import os
from dotenv import load_dotenv
from database.db_manager import DatabaseManager
from utils.message_router import MessageRouter

load_dotenv()

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize database manager
db_manager = DatabaseManager()

# Initialize message router
message_router = MessageRouter()

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your message manager bot.')

def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.first_name
    message_text = update.message.text

    logger.info(f'Received message from {user_name}: {message_text}')
    
    # Store message in the database
    db_manager.store_message('telegram', update.message.message_id, user_id, user_name, message_text)

    # Route message to the appropriate source
    message_router.route_message('telegram', user_id, user_name, message_text)

def main() -> None:
    updater = Updater(os.getenv('TELEGRAM_BOT_TOKEN'))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()