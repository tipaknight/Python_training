from random import choice

import telebot


token = 'Место для токена'

bot = telebot.TeleBot(token)


RANDOM_TASKS = ['Почитать книгу', 'Выучить Python', 'Помыть машину', 'Посмотреть сериал', 'Посмотреть новости на день']

tasks = dict()

HELP = """
Список доступных команд:
/show или /print  - напечать все задачи на заданную дату
/todo или /add - добавить задачу
/random - добавить на сегодня случайную задачу
/help - Напечатать help
"""
def add_todo(date, task):
  if date in tasks:
      # Дата есть в словаре
      # Добавляем в список задачу
      tasks[date].append(task)
  else:
      # Даты в словаре нет
      # Создаем запись с ключом date
      tasks[date] = []
      tasks[date].append(task)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random_add(message):
    date = 'сегодня'
    task = choice(RANDOM_TASKS)
    add_todo(date, task)
    text = 'Задача ' + task + ' добавлена на дату ' + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['todo', 'add'])
def todo_add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    # проверка количества введеных символов
    if len(task) >= 3:
        add_todo(date, task)
        text = 'Задача ' + task + ' добавлена на дату ' + date
    else:
        text = 'Мало символов задачи'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show','print'])
def print_show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    for date in command:
        text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + '* ' + task + "\n"
    else:
      # вводим в словарь список всех дат
      list_of_all_dates = []
      # добавляем в список даты которые являются ключом к задачам
      for date in tasks.keys():
        list_of_all_dates.append(date)
        # выводим даты в которых есть какое-то задание
        text = 'Такой даты нет выберете из списка другую: ' + '\n' + str(list_of_all_dates) + "\n"

    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

