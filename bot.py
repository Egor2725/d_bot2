import telebot

from keybord import base


token = "965621463:AAEPum7Lvd8x-f6djcogU4n9d8woYOhrMIo"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello!', reply_markup=base())




bot.polling(none_stop=True)

