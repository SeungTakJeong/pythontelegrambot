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

TOKEN = '304118278:AAH3uUnl_FC2tJj434zuYtBXfaGmMsuv1Rc'  # get token from command-line
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
