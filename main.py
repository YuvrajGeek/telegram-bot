import logging, random, secrets, wikipedia, math, json, requests
from telegram import Update, Chat
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from trigo import sin, cos, tan, cosec, sec, cot
from meth import add, subtract, multiply, divide

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

helper = '''
Here's the list of bot commands that you can use:
1. /help : See the list of commands.
2. /random : Generate a random number.
3. /hex characters: Generate the hexadecimal code.
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
'''

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(helper)

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(helper)

def random_command(update: Update, context: CallbackContext) -> None:
	update.message.reply_text(f'Random Number: {random.randint(1,100)}')

def diceroll(update: Update, context: CallbackContext) -> None:
	update.message.reply_text(f'Dice Says: {random.randint(1,6)}')


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
    try:
        if update.message.text == '/hex':
            update.message.reply_text('Please specify the integer after /hex.')
        else:
            length = int(str(update.message.text).replace('/hex', ''))
            key = secrets.token_hex(length)
            update.message.reply_text(f'Here\'s your hexadecimal value for {length}:\n{key}')
    except:
        update.message.reply_text('Could not generate hex code. NOTE:This command works for integers only. Specify the integer after /hex.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(helper)


def weather(update: Update, context: CallbackContext) -> None:
    weather_api_key = '<YOUR OPENWEATHERMAP API KEY>'
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
    updater = Updater("<YOUR TELEGRAM TOKEN HERE. GET IT FROM @BotFather.>", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("random", random_command))
    dispatcher.add_handler(CommandHandler("hex", secretkey))
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
