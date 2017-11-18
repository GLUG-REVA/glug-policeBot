from telegram.ext import Updater, CommandHandler, RegexHandler
import os

#This is constant code and thus there is no need to change it.
updater = Updater(token=os.environ['TEL_GLUG'])
dispatcher = updater.dispatcher

#The code below contains all the methods that will handle the bot's actions
def police(bot, update):
    try:
        bot.getUpdates(5)
    except:
        print 'Wrong'
    print 'We have gotten the updates'
    chat = bot.getChat(update.message.chat_id)
    admins = chat.get_administrators()
    auth_users = [admin.user for admin in admins]
    user = update.effective_user
    txt = 'Message sent by authorized entity only.'
    if user not in auth_users:
        try:
            bot.deleteMessage(update.message.chat_id, update.message.message_id)
            txt = 'Policing has been done. You cannot escape the long arm of the law.'
        except:
            txt = 'Unauthorized message deleted before policing done. The law prevails.'
            pass
    #bot.sendMessage(chat_id=update.message.chat_id, text=txt)


#The code below contains all the code handlers
police_handler = RegexHandler(r'.+', police)
dispatcher.add_handler(police_handler)

updater.start_polling()
