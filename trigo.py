import math
from telegram import Update, Chat
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def cos(update: Update, context: CallbackContext) -> None:
    if update.message.text == "/cos":
        update.message.reply_text("Specify the value.")
    else:
        try:
            converter = 180/math.pi
            val = float(str(update.message.text).replace("/cos", ""))/converter
            ans = round(float(math.cos(val)), 2)
            update.message.reply_text(f'{ans}')
        except:
            update.message.reply_text("An error occured. Try changing values.")

def sin(update: Update, context: CallbackContext) -> None:
    if update.message.text == "/sin":
        update.message.reply_text("Specify the value.")
    else:
        try:
            converter = 180/math.pi
            val = float(str(update.message.text).replace("/sin", ""))/converter
            ans = round(float(math.sin(val)), 2)
            update.message.reply_text(f'{ans}')
        except:
            update.message.reply_text("An error occured. Try changing values.")

def tan(update: Update, context: CallbackContext) -> None:
    if update.message.text == "/tan":
        update.message.reply_text("Specify the value.")
    else:
        try:
            converter = 180/math.pi
            val = float(str(update.message.text).replace("/tan", ""))/converter
            ans = round(float(math.tan(val)), 2)
            update.message.reply_text(f'{ans}')
        except:
            update.message.reply_text("An error occured. Try changing values.")


def sec(update: Update, context: CallbackContext) -> None:
    if update.message.text == "/sec":
        update.message.reply_text("Specify the value.")
    else:
        try:
            converter = 180/math.pi
            val = float(str(update.message.text).replace("/sec", ""))/converter
            ans = round(1/float(math.cos(val)), 2)
            update.message.reply_text(f'{ans}')
        except:
            update.message.reply_text("An error occured. Try changing values.")

def cosec(update: Update, context: CallbackContext) -> None:
    if update.message.text == "/cosec":
        update.message.reply_text("Specify the value.")
    else:
        try:
            converter = 180/math.pi
            val = float(str(update.message.text).replace("/cosec", ""))/converter
            ans = round(1/float(math.sin(val)), 2)
            update.message.reply_text(f'{ans}')
        except:
            update.message.reply_text("An error occured. Try changing values.")

def cot(update: Update, context: CallbackContext) -> None:
    if update.message.text == "/cot":
        update.message.reply_text("Specify the value.")
    else:
        try:
            converter = 180/math.pi
            val = float(str(update.message.text).replace("/cot", ""))/converter
            ans = round(1/float(math.tan(val)), 2)
            update.message.reply_text(f'{ans}')
        except:
            update.message.reply_text("An error occured. Try changing values.")
