import telebot
from telebot import types
from dotenv import load_dotenv()
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = telebot.TeleBot(API_KEY)


MENU = ["Pizza", "Burger", "HotDog", "Salad"]

@bot.message_handler(commands=["start"])
def menu(msg):
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(item, callback_data=item) for item in MENU]
    
    markup.add(*buttons)
    
    bot.send_message(msg.chat.id, f"Welcome, choose a meale from menu:", reply_markup=markup)
bot.infinity_polling()


# @bot.callback_query_handler(func=lambda call: call.data in MENU)
# def menu(call):
#     meal = call.data
#     bot.answer_callback_query(call.id)

#     bot.send_message(call.message.chat.id, f"How many {meal}")
#     bot.register_next_step_handler(message, lambda msg: get_quantity(msg, meal))

# def get_quantity(message, meal):
#     pass