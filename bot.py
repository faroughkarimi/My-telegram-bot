import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# دریافت توکن از متغیر محیطی (آن را بعداً تنظیم می‌کنیم)
TOKEN = os.getenv("TOKEN")

# تنظیمات اولیه ربات
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# دستور استارت
def start(update, context):
    update.message.reply_text("سلام! من ربات بیمه کارآفرین هستم. چطور می‌توانم کمک کنم؟")

# پاسخ به پیام‌های کاربران
def reply(update, context):
    user_message = update.message.text.lower()
    
    if "بیمه عمر" in user_message:
        update.message.reply_text("برای خرید بیمه عمر، به لینک زیر مراجعه کنید:\n[لینک بیمه عمر]")
    elif "بیمه درمان" in user_message:
        update.message.reply_text("برای خرید بیمه درمان تکمیلی، به لینک زیر مراجعه کنید:\n[لینک بیمه درمان]")
    else:
        update.message.reply_text("من متوجه نشدم. لطفاً سوال خود را دوباره بپرسید.")

# افزودن دستورات به ربات
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

# اجرای ربات
updater.start_polling()
updater.idle()
