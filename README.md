# WikiBot - Wikipedia Search Telegram Bot

## Description

Wikipedia Search Bot is a Telegram bot built using the `aiogram` library in Python. The bot allows users to search for articles on Wikipedia and provides summaries and links to the full articles. Users can interact with the bot by sending commands and text messages to initiate searches and receive article information.

## Features

- Search for articles on Wikipedia.
- Get article summaries and links to full articles.
- Interactive user interface with buttons and keyboard shortcuts.
- Error handling for ambiguous queries and not-found articles.

## Technology Used and Setup

To run the Wikipedia Search Bot, you need to have Python installed on your system. The bot uses the `aiogram` library for interacting with the Telegram API and the `xml.etree.ElementTree` library for parsing the configuration XML. You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

Make sure you have `pip` installed and properly configured.

## How to Use

1. Clone or download the repository to your local machine.

2. Navigate to the project directory using your terminal.

3. Create a Telegram bot and obtain the API token from the [BotFather](https://core.telegram.org/bots#botfather).

4. Create a `config.xml` file in the project directory with your API token and message templates. You can refer to the provided `config.xml` example.

5. Run the bot by executing the following command in your terminal:

    ```bash
    python main.py
    ```

6. Interact with the bot in your Telegram chat to search for articles and receive summaries and links.

## Commands

- `/start`: Start a conversation with the bot and receive a welcome message.
- `/search`: Initiate a search for a Wikipedia article.
- `/help`: Display help text with information on how to use the bot.

## Customize

You can customize the bot's messages, behavior, and error handling by modifying the `bot.py` script. The provided XML configuration (`config.xml`) contains messages and error templates that the bot uses. You can adjust these templates to suit your preferences.

**Note:** The Wikipedia Search Bot is designed for educational and personal use. Make sure to follow Telegram's [bot guidelines](https://core.telegram.org/bots) and Wikipedia's [API terms of use](https://en.wikipedia.org/wiki/Wikipedia:Creating_a_bot#API_terms_of_use) when using the bot.

Enjoy searching and learning with the Wikipedia Search Bot!

**Disclaimer:** This bot relies on external libraries and APIs, and its functionality may be affected by updates to these libraries and APIs.
