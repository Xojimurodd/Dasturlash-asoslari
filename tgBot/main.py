import telebot

TOKEN = '5017667168:AAF_5Tk0Q2oKIp1eEjtNyluC-k51R6_OC6M'

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        text = m
        tb.send_message(chatid, text)


tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener) #register listener
tb.polling()
#Use none_stop flag let polling will not stop when get new message occur error.
tb.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
tb.polling(interval=3)

while True: # Don't let the main Thread end.
    pass
