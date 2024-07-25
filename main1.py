import telebot
import requests

# Initialize the Telegram bot with your API key
bot = telebot.TeleBot('5834739589:AAE0dMkUisxk8fwPggbbSYYj952uxNm0WYs')

# Initialize the Pixabay API with your API key
pixabay_api_key = '33936820-64e006957239d0cdfc5e6fafb'
pixabay_api_url = f'https://pixabay.com/api/?key={pixabay_api_key}&q='

# Define the handler for the /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Hi! Send me a keyword to generate an image.')

# Define the handler for text messages
@bot.message_handler(func=lambda message: True)
def generate_image(message):
    try:
        # Use the Pixabay API to search for an image based on the user's input keyword
        query = message.text
        response = requests.get(pixabay_api_url + query).json()

        # Retrieve the URL of the image from the Pixabay API response
        image_url = response['hits'][0]['largeImageURL']

        # Download the image from the URL
        image_data = requests.get(image_url).content

        # Send the image to the user
        bot.send_photo(message.chat.id, photo=image_data)

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

# Start the bot and listen for messages
bot.polling(none_stop=True)
