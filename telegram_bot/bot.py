# import logging
# import os
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)


# TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# if not TELEGRAM_BOT_TOKEN:
#     exit("Specify TELEGRAM_BOT_TOKEN env variable")
    
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     effective_chat = update.effective_chat
#     if not effective_chat:
#         logger.warning("effective_chat is None")
#         return
#     await context.bot.send_message(
#         chat_id=effective_chat.id, 
#         text="I'm a bot, please talk to me!")    

# # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")



# if __name__ == '__main__':
#     application = ApplicationBuilder().token("TELEGRAM_BOT_TOKEN").build()
    
#     start_handler = CommandHandler('start', start)
#     application.add_handler(start_handler)
    
#     application.run_polling()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat is None")
        return
    await context.bot.send_message(
        chat_id=effective_chat.id, 
        text="Привіт,я бот, який допоможе вибрати тобі найкращу мангу!")

if __name__ == '__main__':
    application = ApplicationBuilder().token('5539579648:AAGWzUQ4Z49Es4ptW_garrxSCdstzNSeMr8').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
    
    
    
    
    


    

