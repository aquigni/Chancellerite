import random
import schedule
import time
from telegram.ext import Updater, CallbackContext
from telegram import Update

def load_texts():
    with open('../data/t.txt', 'r', encoding='utf-8') as file:
        transformed_texts = file.readlines()
    with open('../data/p.txt', 'r', encoding='utf-8') as file:
        proverbs = file.readlines()
    return transformed_texts, proverbs

def send_message(bot, message, reply_to_message_id=None):
    chat_id = "@Chancellerist"
    if reply_to_message_id:
        message = "👆 " + message
    sent_message = bot.send_message(chat_id=chat_id, text=message, reply_to_message_id=reply_to_message_id)
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
    schedule.every().day.at(f"{random.randint(9, 11)}:{str(random.randint(0, 59)).zfill(2)}").do(post_morning_proverb, bot=updater.bot, transformed_text=transformed_texts[index])
    # schedule.every().day.at("02:56").do(post_morning_proverb, bot=updater.bot, transformed_text=transformed_texts[index])

    # Post in the evening
    schedule.every().day.at(f"{random.randint(17, 20)}:{str(random.randint(0, 59)).zfill(2)}").do(post_evening_proverb, bot=updater.bot, proverb=proverbs[index])
    # schedule.every().day.at("02:57").do(post_evening_proverb, bot=updater.bot, proverb=proverbs[index])

if __name__ == "__main__":
    transformed_texts, proverbs = load_texts()
    sent_indices = set()

    updater = Updater("TELEGRAM_BOT_TOKEN")
    schedule_posts(updater, transformed_texts, proverbs, sent_indices)

    updater.start_polling()

    while True:
        schedule.run_pending()
        time.sleep(1)
