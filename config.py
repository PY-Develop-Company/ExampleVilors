# файл для читання config.ini
from configparser import ConfigParser
import os
import sys

config = ConfigParser()

# у разі запуску exe з консолі файл config.ini не знаходиться
# дана стрічка коду вирішує цю проблему
os.chdir(os.path.dirname(sys.argv[0]))
# читання файлу config.ini
config.read("config.ini")

TOKEN = config["BOT"]["Token"]
