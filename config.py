# файл для читання config.ini

from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

TOKEN = config["BOT"]["Token"]
