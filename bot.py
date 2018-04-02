# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
import time


class PiewDieBot(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get("https://www.pewdiebot.com/en/")

    def get(self):
        return self.driver.execute_script("return cleverbot.reply")

    def send(self, reply):
        return self.driver.execute_script("cleverbot.sendAI('%s')" % (reply))

class Facebook(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.messenger.com")
        self.login()

        self.driver.get(raw_input("Your facebook Conversation: "))

    def login(self):
        self.driver.find_element_by_id("email").send_keys(raw_input("Email Address: "))
        self.driver.find_element_by_id("pass").send_keys(getpass(prompt="Password: "))
        self.driver.find_element_by_name("login").click()

    def getMsg(self):
         return self.driver.find_elements_by_xpath("//*[contains(@class, '_aok')]")[-1].text

    def sendMsg(self, msg):
        self.driver.find_element_by_class_name("notranslate").send_keys(msg)
        self.driver.find_element_by_class_name("_38lh").click()
if __name__ == "__main__":
    facebook = Facebook()
    bot = PiewDieBot()
    time.sleep(3)
    lastestMsg = bot.get()
    facebook.sendMsg(lastestMsg)
    while True:
        received = facebook.getMsg()
        time.sleep(1)
        print(received)
        if received != lastestMsg:
            bot.send(str(received.replace('\'', '').replace("\"", "").replace("@", "").lower()))
            lastestMsg = bot.get()
            print(lastestMsg)
            facebook.sendMsg(lastestMsg)
