from django.core.management.base import BaseCommand
import telebot
from shop.models import Cars

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")

TOKEN = "6961684634:AAGscyVdrsmhYY7lzNoIlK-IgiMC5D93kqU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['add'])
def add_cars(message):
    try:
        command, cars_name, cars_color = message.text.split()
        cars_color = int(cars_color)

        new_cars = Cars(name=cars_name, color=cars_color)  # Исправлено: заменено поле price на color
        new_cars.save()

        bot.send_message(message.chat.id, f"Car {cars_name} added successfully!")
    except ValueError:
        bot.send_message(message.chat.id, "Invalid command format. Use /add <cars_name> <cars_color>")

@bot.message_handler(commands=['cars'])
def list_cars(message):
    all_cars = Cars.objects.all()
    if all_cars:
        cars_list = "\n".join([f"{car.name} - {car.color}" for car in all_cars])
        bot.send_message(message.chat.id, cars_list)
    else:
        bot.send_message(message.chat.id, "No cars available.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Starting bot...")
    bot.polling()
