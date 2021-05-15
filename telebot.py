import telebot
bot = telebot.TeleBot('1835516731:AAFg_4eT3CzlKJ66pJh0oOeGKeA33me-UQg')
bot.infinity_polling()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, я бот который поможет тебе получить статистику твоих успехов. Для начала скажи мне свой имейл.')

@bot.message_handler(content_types=["text"])
def send_welcome(message):
    bot.reply_to(message, f'Привет, я бот который поможет тебе получить статистику твоих успехов. Для начала скажи мне свой имейл.')