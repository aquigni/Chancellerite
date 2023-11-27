from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('YOUR_TELEGRAM_BOT_TOKEN')

# Add this line to check the token
print("Loaded Telegram Bot Token:", TELEGRAM_BOT_TOKEN)

import random
import schedule
import time
from telegram.ext import Updater, CallbackContext
from telegram import Update

def load_texts():
    with open('t.txt', 'r', encoding='utf-8') as file:
        transformed_texts = file.readlines()
    with open('p.txt', 'r', encoding='utf-8') as file:
        proverbs = file.readlines()
    return transformed_texts, proverbs

def send_message(bot, message, reply_to_message_id=None):
    chat_id = "@Chancellerist"
    parse_mode = None
    if reply_to_message_id:
        message = "👆 <tg-spoiler>" + message + "</tg-spoiler>"
        parse_mode = "HTML"
    sent_message = bot.send_message(chat_id=chat_id, text=message, parse_mode=parse_mode, reply_to_message_id=reply_to_message_id)
    return sent_message.message_id

morning_message_id = None

def post_morning_proverb(bot, transformed_text):
    global morning_message_id
    morning_message_id = send_message(bot, transformed_text)

def post_evening_proverb(bot, proverb):
    send_message(bot, proverb, reply_to_message_id=morning_message_id)

def schedule_posts(updater, transformed_texts, proverbs, sent_indices):
    if len(sent_indices) >= len(transformed_texts):
        sent_indices.clear()

    index = random.choice([i for i in range(len(transformed_texts)) if i not in sent_indices])
    sent_indices.add(index)

    # Post in the morning
    # morning_hour = random.randint(9, 11)
    # morning_minute = random.randint(0, 59)
    # morning_time = f"{morning_hour:02d}:{morning_minute:02d}"
    # schedule.every().day.at(morning_time).do(post_morning_proverb, bot=updater.bot, transformed_text=transformed_texts[index])
    # test mode strict time
    schedule.every().day.at("10:01").do(post_morning_proverb, bot=updater.bot, transformed_text=transformed_texts[index])

    # Post in the evening
    # evening_hour = random.randint(17, 20)
    # evening_minute = random.randint(0, 59)
    # evening_time = f"{evening_hour:02d}:{evening_minute:02d}"
    # schedule.every().day.at(evening_time).do(post_evening_proverb, bot=updater.bot, proverb=proverbs[index])
    # test mode strict time
    schedule.every().day.at("18:01").do(post_evening_proverb, bot=updater.bot, proverb=proverbs[index])

if __name__ == "__main__":
    transformed_texts, proverbs = load_texts()
    sent_indices = set()

    updater = Updater(TELEGRAM_BOT_TOKEN)
    schedule_posts(updater, transformed_texts, proverbs, sent_indices)

    updater.start_polling()

    while True:
        schedule.run_pending()
        time.sleep(1)
