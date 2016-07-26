import telebot
import imperors
import phrases

token = "252873975:AAHxV2D_95HsLGL4IC6qo56P9ryByuMOSBs"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.from_user.id, phrases.help)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "учить" or message.text == "Учить":
        bot.send_message(message.from_user.id, '\n'.join(imperors.merged_list))
    else:
        bot.send_message(message.from_user.id, "Я так не умею :(")
#    elif message == "тест" or message == "Тест":

bot.polling(none_stop=True, interval=0)
