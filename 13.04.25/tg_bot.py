import telebot
import time
bot = telebot.TeleBot('7980259854:AAEMErfPoTa6txuyQIlxQGTxezBrgDDFc80')
bot.polling(none_stop=True, interval=0)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        print('Started')
        while True:
            bot.send_message(message.from_user.id, 'а')
            time.sleep(10)
