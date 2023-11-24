import random
import schedule
import time
from telegram.ext import Updater

def load_texts():
    with open('../data/t.txt', 'r', encoding='utf-8') as file:
        transformed_texts = file.readlines()
    with open('../data/p.txt', 'r', encoding='utf-8') as file:
        proverbs = file.readlines()
    return transformed_texts, proverbs

def send_message(context, message):
    chat_id = "@Chancellerist"
    context.bot.send_message(chat_id=chat_id, text=message)

def post_proverb(updater, transformed_texts, proverbs, sent_indices):
    if len(sent_indices) >= len(transformed_texts):
        sent_indices.clear()  # Reset if all strings have been sent

    index = random.choice([i for i in range(len(transformed_texts)) if i not in sent_indices])
    sent_indices.add(index)

    # Post in the morning
    # schedule.every().day.at(f"{random.randint(9, 11)}:{str(random.randint(0, 59)).zfill(2)}").do(send_message, context=updater, message=transformed_texts[index])
    schedule.every().day.at("02:29").do(send_message, context=updater, message=transformed_texts[index])

    # Post in the evening
    # schedule.every().day.at(f"{random.randint(17, 20)}:{str(random.randint(0, 59)).zfill(2)}").do(send_message, context=updater, message=proverbs[index])
    schedule.every().day.at("02:30").do(send_message, context=updater, message=proverbs[index])

if __name__ == "__main__":
    transformed_texts, proverbs = load_texts()
    sent_indices = set()

    updater = Updater("5893964607:AAEjUcOGgcqRCVLUGWPH6QpTMi1A3KLMszs")
    post_proverb(updater, transformed_texts, proverbs, sent_indices)

    while True:
        schedule.run_pending()
        time.sleep(1)
