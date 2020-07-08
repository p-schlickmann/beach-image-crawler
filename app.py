import re
from time import sleep
import keyboard
import selenium.common.exceptions as SeleniumEXC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyperclip import copy

from scraper.database.conn import DatabaseConnection


class Printer:
    def __init__(self, state):
        self.state = state
        self.browser = webdriver.Chrome('C:/Users/edu/Downloads/driver/chromedriver.exe')

    def get_from_db(self):
        with DatabaseConnection('./database/BR.db') as cursor:
            select_query = "SELECT * FROM locations WHERE state=?"
            results = cursor.execute(select_query, (self.state,))
            return results.fetchall()

    def print(self, states):
        bot = self.browser

        bot.get('https://snazzymaps.com/style/124771/google-maps-clean#')
        element = WebDriverWait(bot, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[3]/button[2]')))
        element.click()
        element = WebDriverWait(bot, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[1]/button')))
        element.click()

        full_screen = bot.find_element_by_tag_name("body")
        full_screen.send_keys(Keys.F11)

        for row in states:
            state_name = row[0]
            city_name = row[1]
            beach_name = row[2]
            searcher = bot.find_element_by_xpath('/html/body/main/div[3]/div[1]/div[2]/div/input')
            searcher.click()
            searcher.send_keys(Keys.CONTROL, 'a')
            searcher.send_keys(Keys.BACKSPACE)
            searcher.send_keys(f'{beach_name} {city_name}')
            while True:
                try:
                    if keyboard.is_pressed('f10'):
                        copy(f'{state_name}#{city_name}#{beach_name}')
                        break
                    elif keyboard.is_pressed('f9'):
                        break
                    elif keyboard.is_pressed('f8'):
                        sleep(2)
                        while True:
                            try:
                                if keyboard.is_pressed('f2'):
                                    break
                            except:
                                continue
                        continue
                except:
                    continue


printer = Printer('<city you want>')
results = printer.get_from_db()
printer.print(results)
