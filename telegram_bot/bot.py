import xml.etree.ElementTree as ET

import wikipedia
from aiogram import Bot, Dispatcher, types
from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
    KeyboardButton, ParseMode, ReplyKeyboardMarkup
)

# Load configuration from config.xml
config_tree = ET.parse('config.xml')
api_token = config_tree.find('api_token').text
messages = config_tree.find('messages')

bot = Bot(token=api_token)
dp = Dispatcher(bot)
wikipedia.set_lang("en")  # Set the language for Wikipedia queries

# Retrieve text messages from the XML file
welcome_text = messages.find('welcome').text
search_prompt_text = messages.find('search_prompt').text
help_text = messages.find('help_text').text
ambiguous_error_text = messages.find('ambiguous_error').text
not_found_error_text = messages.find('not_found_error').text
unknown_command_error_text = messages.find('unknown_command_error').text

# Define main search and help buttons with emojis
search_button = KeyboardButton('Search')
help_button = KeyboardButton('Help')
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[search_button], [help_button]], resize_keyboard=True)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    The send_welcome function is a coroutine that sends the user a
    welcome message.
    It also sets up the main keyboard for them to use.
    """
    await message.reply(welcome_text, reply_markup=main_keyboard)


@dp.message_handler(
    lambda message: message.text.lower() in ['search', '/search'])
async def start_search(message: types.Message):
    """
    The start_search function is a coroutine that sends the user a
    message prompting them to enter their search query.
    """
    await message.reply(search_prompt_text)


@dp.message_handler(lambda message: message.text.lower() in ['help', '/help'])
async def show_help(message: types.Message):
    """
    The show_help function is a callback function that will be called when
    the user presses the help button.

    It will send a message to the user with some helpful information about
    how to use this bot.
    """
    await message.reply(help_text, parse_mode=ParseMode.MARKDOWN,
                        reply_markup=main_keyboard)


@dp.message_handler(lambda message: not message.text.startswith('/'))
async def process_search(message: types.Message):
    """
    The process_search function is the main function of this module.
    It takes a message object as an argument and returns nothing.
    The function searches for the query in Wikipedia, gets the summary of it,
    and sends it to chat.
    """
    search_query = message.text
    try:
        page = wikipedia.page(search_query)
        page_title = f"📖 *{page.title}*"
        # Get the first sentence of the summary
        page_summary = page.summary.split('.')[0]
        reply_markup = InlineKeyboardMarkup(row_width=1)
        url_button = InlineKeyboardButton(text="Read Article 📚", url=page.url)
        reply_markup.insert(url_button)
        await message.reply(f"{page_title}\n\n📝 {page_summary}",
                            parse_mode=ParseMode.MARKDOWN,
                            reply_markup=reply_markup)

    except wikipedia.DisambiguationError as e:
        options = '\n'.join(e.options)
        error_message = ambiguous_error_text.format(
            search_query=search_query, options=options)
        await message.reply(error_message)
    except wikipedia.PageError:
        not_found_message = not_found_error_text.format(
            search_query=search_query)
        await message.reply(not_found_message)


@dp.message_handler()
async def echo(message: types.Message):
    """
    The echo function is a simple echo command that will repeat whatever
    the user says.

    It's used to demonstrate how to use commands and filters.
    """
    await message.reply(unknown_command_error_text, reply_markup=main_keyboard)


def start_polling():
    """
    The start_polling function is a shortcut for executor.start_polling(dp, skip_updates=True).
    It starts the polling process and blocks the current thread until Ctrl+C (SIGINT) is pressed.
    """
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
