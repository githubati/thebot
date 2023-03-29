import logging
import openai
# import os
# import re
import requests
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Telegram ve OpenAI API anahtarlarınızı girin
TELEGRAM_API_KEY = "6249220580:AAHUShDpXndDPfamLiY_wm_V_xE76_0lMRQ"
OPENAI_API_KEY = "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"

# OpenAI API anahtarınızı kullanarak OpenAI ile iletişim kurun
openai.api_key = OPENAI_API_KEY

# Ayarlamak istediğiniz modelin adını belirtin
MODEL_NAME = "text-davinci-002"

# Günlüğe kaydetme işlemini yapılandırın
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    """Botun /start komutunu işlemek için kullanılır."""
    update.message.reply_text("Merhaba! Ben OpenAI GPT-4 ile çalışan bir Telegram botuyum. Bana bir şeyler yaz ve yanıtlamama izin ver!")

def text_message(update: Update, context: CallbackContext):
    """Gelen metin mesajlarını işlemek için kullanılır."""
    input_text = update.message.text
    prompt = f"{input_text}\n\nGPT-4:"

    # OpenAI API'sini kullanarak modeli ince ayar yapın
    response = openai.Completion.create(
        engine=MODEL_NAME,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # GPT-4'ün ürettiği metni alın ve Telegram kullanıcısına gönderin
    reply = response.choices[0].text.strip()
    update.message.reply_text(reply)

def main():
    """Botun ana işleyicisidir."""
    updater = Updater(TELEGRAM_API_KEY)

    # Komut işleyicileri
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, text_message))

    # Botu başlat ve güncellemeleri almaya başla
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

