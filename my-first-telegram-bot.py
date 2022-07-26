from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
import logging

import datetime
import weather_call

import pathlib

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
path_to_telegram_cred =str(pathlib.Path().resolve())+'telegram_credentials.txt'
with open(path_to_telegram_cred, 'r') as f:
    for line in f:
        if line[-1] == '\n':
            telegram_api_key = line[:-1]
        else:
            telegram_api_key = line


        
updater = Updater(token=telegram_api_key, use_context=True)
dispatcher = updater.dispatcher


def weather(update: Update, context: CallbackContext):
    hour_of_day = datetime.datetime.now().hour
    time_of_day=['Morgen', 'Mittag', 'Nachmittags', 'Abend']
    try:
        data = weather_call.weather_warrior(City=context.args[0])
        temp, weather = data[0], data[1]

        message = f"Willkommen! Die momentane Temperatur beträgt {str(temp)}° Celsius."
        if temp >= 25:
            message += " " + "Sie brauchen sich heute nicht warm anzuziehen."
        elif 15 < temp < 25:
            message += " " + f"Genießen Sie die {time_of_day[hour_of_day//8]}luft!"
        elif temp <= 15:
            message += " " + "Ziehen Sie sich lieber etwas wärmer an."
        elif temp <= 5:
            message += " " + "Ziehen Sie sich lieber einen Schal und Handschuhe an."
        message += " " + f"Das Wetter ist des Weiteren {str(weather)}. Bitte berücksichtigen Sie dies."
    
    except:
        if len(context.args) > 0:
            message = f"Die Angegebene Stadt {context.args[0]} existiert nicht!"
        else:
            message = f"Es wurde keine Stadt angegeben!"
        
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

start_handler = CommandHandler('weather', weather, pass_args=True)
dispatcher.add_handler(start_handler)
updater.start_polling()