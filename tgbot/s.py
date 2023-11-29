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
import json

# Checking if the file with already indicated sent lines exists
def load_sent_indices():
    try:
        with open('sent_indices.json', 'r') as file:
            return set(json.load(file))
    except FileNotFoundError:
        return set()

def save_sent_indices(indices):
    with open('sent_indices.json', 'w') as file:
        json.dump(list(indices), file)

def load_texts():
    with open('t.txt', 'r', encoding='utf-8') as file:
        transformed_texts = file.readlines()
    with open('p.txt', 'r', encoding='utf-8') as file:
        proverbs = file.readlines()
    return transformed_texts, proverbs

def send_message(bot, message, reply_to_message_id=None):
    chat_id = "@Chancellerist"
    # chat_id = "@chncllrt_test"
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

def post_evening_proverb(bot, proverb, sent_indices):
    send_message(bot, proverb, reply_to_message_id=morning_message_id)
    save_sent_indices(sent_indices)

def schedule_posts(updater, transformed_texts, proverbs, sent_indices):
    # Check if all indices have been used, if yes, clear the set
    # if len(sent_indices) >= len(transformed_texts):
    #     sent_indices.clear()

    # Select a random index from the available indices
    index = random.choice([i for i in range(len(transformed_texts)) if i not in sent_indices])
    sent_indices.add(index)

    # Post in the morning strict time
    schedule.every().day.at("10:38").do(post_morning_proverb, bot=updater.bot, transformed_text=transformed_texts[index])

    # Post in the evening strict time
    schedule.every().day.at("18:39").do(post_evening_proverb, bot=updater.bot, proverb=proverbs[index], sent_indices=sent_indices)

if __name__ == "__main__":
    transformed_texts, proverbs = load_texts()
    sent_indices = load_sent_indices()

    updater = Updater(TELEGRAM_BOT_TOKEN)
    schedule_posts(updater, transformed_texts, proverbs, sent_indices)

    updater.start_polling()

    while True:
        schedule.run_pending()
        time.sleep(1)
