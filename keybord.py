from telebot import types



def start_key():
    k_b = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("↕Вернуться")
    k_b.add(btn)
    return k_b


def base():
    k_b = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("$Курсы валют")
    btn2 = types.KeyboardButton("☀Погода")
    btn3 = types.KeyboardButton("✌Афиша tut.by")
    btn4 = types.KeyboardButton("☆Заведения\nрядом")
    k_b.add(btn1, btn2, btn3, btn4)
    return k_b

