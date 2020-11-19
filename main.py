import logging
import random
import secrets
import wikipedia
import math
import json
import requests
from telegram import Update, Chat
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi!')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
    '''
    Here's the list of bot commands that you can use:
    1. /help : See the list of commands.
    2. /random : Generate a random number.
    3. /secretkey length: Generate a random set of characters.
    4. /wikipedia query : Get the results of your query from Wikipedia.
    5. /sum a, b, c, d, e... : Get the sum of numbers.
    6. /subtract b, a : Subtract two numbers.
    7. /multiply a, b, c, d, e... : Get the product of numbers.
    8. /divide b, a : Divide two numbers.
    9. /sin a : Get the sin ratio of the number.
    10. /cos a : Get the cos ratio of the number.
    11. /tan a : Get the tan ratio of the number.
    12. /cosec a : Get the cosec ratio of the number.
    13. /sec a : Get the sec ratio of the number.
    14. /cot a : Get the cot ratio of the number.
    15. /weather citynamehere : Get the weather of the city.
    16. /diceroll : Roll a dice.
    ''')

def random_command(update: Update, context: CallbackContext) -> None:
	update.message.reply_text(f'Random Number: {random.randint(1,100)}')

def diceroll(update: Update, context: CallbackContext) -> None:
	update.message.reply_text(f'Dice Says: {random.randint(1,6)}')


# *****Trigonometric Functions*****
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
# ****Trignometry Ends Here*****

def wikipedia_command(update: Update, context: CallbackContext) -> None:
    if update.message.text == "/wikipedia":
        update.message.reply_text("Please specify your query.")
    else:
        query = str(update.message.text).replace("/wikipedia ", '')
        try:
            page = wikipedia.page(query)
            title = page.title
            summary = wikipedia.summary(query, sentences=5)
            update.message.reply_text(f'{title}\n{summary}')
        except:
            update.message.reply_text(f"No Page found. Try changing the spelling of the words or using another term for your query.")

def secretkey(update: Update, context: CallbackContext) -> None:
    if update.message.text == '/secretkey':
        update.message.reply_text('Please specify the length of the key.')
    else:
        length = int(str(update.message.text).replace('/secretkey ', ''))
        key = secrets.token_hex(length)
        update.message.reply_text(f'Here\'s your secret key: {key}')


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

def echo(update: Update, context: CallbackContext) -> None:
    pass

def subtract(update: Update, context: CallbackContext) -> None:
    if update.message.text == '/subtract':
        update.message.reply_text('Please Specify the Numbers to be subtracted.\nSeperate them using a ",".\nFor instance, if you want to subtract 9 from 78; type /subtract 78, 9.')
    else:
        numbers = str(update.message.text).replace('/subtract ', '').split(',')
        result = float(float(numbers[0])-float(numbers[1]))
        update.message.reply_text(f'Your result: {float(numbers[0])} - {float(numbers[1])} = {result}')

def weather(update: Update, context: CallbackContext) -> None:
    weather_api_key = '<YOUR OPENWEATHERMAP API KEY HERE>'
    hard_url = "http://api.openweathermap.org/data/2.5/weather?"
    if update.message.text == '/weather':
        update.message.reply_text('Please specify the location after the /weather command.')
    else:
        try:
            city = str(update.message.text).replace("/weather", "")
            complete_url = f"{hard_url}appid={weather_api_key}&q={city}"
            response = requests.get(complete_url).json()
            if response['cod'] != '404':
                main = response['main']
                temperature = main['temp']
                pressure = main['pressure']
                humidity = main['humidity']
                weather = response['weather']
                weather_description = weather[0]['description'].capitalize()
                update.message.reply_text(f'Weather of {city.capitalize()}\nTemperature: {temperature}K\nPressure: {pressure}hPa\nHumidity: {humidity}%\n{weather_description}')
            else:
                update.message.reply_text("City not found.")
        except:
            update.message.reply_text('An error occured.')

def main():
    updater = Updater("<YOUR TOKEN HERE. GET IT FROM @BotFather.>", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("random", random_command))
    dispatcher.add_handler(CommandHandler("secretkey", secretkey))
    dispatcher.add_handler(CommandHandler("diceroll", diceroll))
    dispatcher.add_handler(CommandHandler("sum", add))
    dispatcher.add_handler(CommandHandler("multiply", multiply))
    dispatcher.add_handler(CommandHandler("divide", divide))
    dispatcher.add_handler(CommandHandler("subtract", subtract))
    dispatcher.add_handler(CommandHandler("wikipedia", wikipedia_command))
    dispatcher.add_handler(CommandHandler("cos", cos))
    dispatcher.add_handler(CommandHandler("sin", sin))
    dispatcher.add_handler(CommandHandler("tan", tan))
    dispatcher.add_handler(CommandHandler("cosec", cosec))
    dispatcher.add_handler(CommandHandler("sec", sec))
    dispatcher.add_handler(CommandHandler("cot", cot))
    dispatcher.add_handler(CommandHandler("weather", weather))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
