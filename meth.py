import math
from telegram import Update, Chat
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def add(update: Update, context: CallbackContext) -> None:
    numbers = str(update.message.text).replace('/sum ', '').split(',')
    total = 0
    for number in numbers:
        total += float(number)
    update.message.reply_text(f'{total}')

def multiply(update: Update, context: CallbackContext) -> None:
    if update.message.text == '/multiply':
        update.message.reply_text('Please Specify the Numbers to be Multplied.\nSeperate them using a ",".\nFor instance, if you want to multiply 2, 4 and 8; type /multiply 2,4,8')
    else:
        numbers = str(update.message.text).replace('/multiply ', '').split(',')
        res = 1
        for number in numbers:
            res = res*float(number)
        update.message.reply_text(f'{res}')

def divide(update: Update, context: CallbackContext) -> None:
    if update.message.text == '/divide':
        update.message.reply_text('Please Specify the Numbers to be divided.\nSeperate them using a ",".\nFor instance, if you want to divide 9 by 3; type /divide 9, 3.')
    else:
        numbers = str(update.message.text).replace('/divide ', '').split(',')
        result = float(float(numbers[0])/float(numbers[1]))
        update.message.reply_text(f'{result}')


def subtract(update: Update, context: CallbackContext) -> None:
    if update.message.text == '/subtract':
        update.message.reply_text('Please Specify the Numbers to be subtracted.\nSeperate them using a ",".\nFor instance, if you want to subtract 9 from 78; type /subtract 78, 9.')
    else:
        numbers = str(update.message.text).replace('/subtract ', '').split(',')
        result = float(float(numbers[0])-float(numbers[1]))
        update.message.reply_text(f'Your result: {float(numbers[0])} - {float(numbers[1])} = {result}')
