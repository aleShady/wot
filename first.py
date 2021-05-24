from telegram.ext import Updater

u = Updater('TOKEN', use_context=True)
j = u.job_queue

def callback_minute(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='-1001230622142', 
                             text='One message every minute')

job_minute = j.run_repeating(callback_minute, interval=60, first=10)
