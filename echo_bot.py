import telebot

token = "Здесь токен"

bot = telebot.TeleBot(token)
name = 'Олег'
answer = ' Ба! Какие люди и без охраны!'
@bot.message_handler(content_types=['text'])
def echo(message):
    string = message.text
    if name in string:
      bot.send_message(message.chat.id, message.text + answer)
    else:
      bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True)

# Решение Нетологии:
# import telebot

# token = ''

# bot = telebot.TeleBot(token)

# my_name = 'Дима'


# @bot.message_handler(content_types=["text"])
# def echo(message):
#     if my_name in message.text:
#         text = 'Ба! Знакомые все лица'
#     else:
#         text = message.text
#     bot.send_message(message.chat.id, text)


# bot.polling(none_stop=True)