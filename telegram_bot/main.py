import logging
import xml.etree.ElementTree as ET

from bot import start_polling

# Load configuration from config.xml
config_tree = ET.parse('config.xml')
api_token = config_tree.find('api_token').text

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    start_polling()
