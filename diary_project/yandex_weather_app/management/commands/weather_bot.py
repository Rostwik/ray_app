import textwrap

import requests
from django.core.management.base import BaseCommand
from yandex_weather_app.models import Town, BotState

from environs import Env
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Filters, Updater
from telegram.ext import CallbackQueryHandler, CommandHandler, MessageHandler

env = Env()
env.read_env()

yandex_weather_api_key = env.str('YANDEX_WEATHER_API_KEY')
telegram_api_token = env.str('TELEGRAM_API_TOKEN')


def start(bot, update):
    keyboard = [[InlineKeyboardButton('Узнать погоду', callback_data='Погода')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        f'Доброго денечка, {update.message.chat.username} ! \n Это погодный бот!',
        reply_markup=reply_markup,
    )

    return 'HANDLE_TOWN'


def handle_town(bot, update):
    query = update.callback_query

    if query.data == 'Погода':
        bot.send_message(
            chat_id=update.callback_query.message.chat_id,
            text='Введите, пожалуйста, название города:'
        )

        return 'HANDLE_WEATHER'


def handle_weather(bot, update):
    town = update.message.text

    try:
        town = Town.objects.get(name=town)

        yandex_api_url = 'https://api.weather.yandex.ru/v2/forecast'
        headers = {
            'X-Yandex-API-Key': yandex_weather_api_key
        }
        payload = {
            'lat': town.lat,
            'lon': town.lon,
            'extra': 'false'
        }
        response = requests.get(yandex_api_url, params=payload, headers=headers)
        response.raise_for_status()
        weather_json = response.json()['fact']

        weather_message = textwrap.dedent(
            f'''
                    Город: {town},
                    Температура: {weather_json['temp']} градусов Цельсия,
                    Атмосферное давление: {weather_json['pressure_mm']} мм рт.ст.,
                    Скорость ветра: {weather_json['wind_speed']} м/с
            '''
        )

        bot.send_message(
            chat_id=update.message.chat_id,
            text=weather_message
        )

    except Town.DoesNotExist:
        bot.send_message(
            chat_id=update.callback_query.message.chat_id,
            text='Введите, пожалуйста, название города:'
        )

    start(bot, update)


def handle_users_reply(bot, update):
    if update.message:
        user_reply = update.message.text
        chat_id = update.message.chat_id
    elif update.callback_query:
        user_reply = update.callback_query.data
        chat_id = update.callback_query.message.chat_id
    else:
        return

    user_state, created = BotState.objects.get_or_create(chat_id=chat_id)

    if user_reply == '/start':
        user_state.state = 'START'
    elif created:
        bot.send_message(
            chat_id=update.message.chat_id,
            text='Кажется Вы у нас впервые, запустите бота командой "/start"'
        )
        return

    states_functions = {
        'START':
            start,
        'HANDLE_TOWN':
            handle_town,
        'HANDLE_WEATHER':
            handle_weather,
    }

    state_handler = states_functions[user_state.state]

    next_state = state_handler(bot, update)
    user_state.state = next_state
    user_state.save()


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        updater = Updater(telegram_api_token)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(
            CallbackQueryHandler(handle_users_reply))
        dispatcher.add_handler(
            MessageHandler(Filters.text, handle_users_reply))
        dispatcher.add_handler(
            CommandHandler('start', handle_users_reply))

        updater.start_polling()

        updater.idle()
