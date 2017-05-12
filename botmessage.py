import sys
import time
import telepot
import sendmessage

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    sendMessage = sendmessage.SendMessage()

    if content_type == 'text':
        print(msg['text'])

        message = sendMessage.getPMInfoMessage(msg['text'])
        bot.sendMessage(chat_id, message)

TOKEN = '330472065:AAEfrxS78hh_fLsEWdiUQgfapjbwsRfU6sA'  # get token from command-line
CHATID = '62443661'
SEND='https://api.telegram.org/bot330472065:AAEfrxS78hh_fLsEWdiUQgfapjbwsRfU6sA/sendMessage?chat_id=62443661&text=Hello'
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
