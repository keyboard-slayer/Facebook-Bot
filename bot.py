# -*- coding: utf-8 -*-

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
import time
import os


from cleverbot import * # For this git: https://github.com/0v3rl0w/Unofficial-Cleverbot-Api

class Facebook(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.messenger.com")
        self.login()
        os.system("clear")
        raw_input("Press Enter when you're ready to spam...")
        self.name = self.getName()

    def login(self):
        self.driver.find_element_by_id("email").send_keys(raw_input("Email Address: "))
        self.driver.find_element_by_id("pass").send_keys(getpass(prompt="Password: "))
        self.driver.find_element_by_name("login").click()

    def getMsg(self):
         return self.driver.find_elements_by_xpath("//*[contains(@class, '_aok')]")[-1].text

    def getName(self):
        name = self.driver.find_element_by_class_name("_3oh-").text
        return name.encode("utf-8").replace("à", "a").replace("ï", "i").replace("ô", "o").replace("ê", "e").replace("é", "e").replace("è", "e").lower()

    def sendMsg(self, msg):
        try:
            self.driver.find_element_by_class_name("notranslate").send_keys(msg)
            self.driver.find_element_by_class_name("_38lh").click()

        except selenium.common.exceptions.NoSuchElementException:
            return False
if __name__ == "__main__":
    facebook = Facebook()
    bot = Cleverbot()
    print(facebook.name.split(' ')[0])
    bot.send("Je m'appelle {}".format(facebook.name.split(' ')[0]))
    facebook.sendMsg("Bonjour {}".format(facebook.name.split(' ')[0]))
    lastestMsg = "Bonjour {}".format(facebook.name.split(' ')[0])
    lastestTmp = ""
    while True:
        received = facebook.getMsg().encode("utf-8")
        time.sleep(1)
        print(received)
        if received != lastestMsg:
            lastestTmp = lastestMsg
            bot.send(str(received))
            lastestMsg = bot.get().lower()
            print(lastestMsg)
            if "t'appelle" not in lastestMsg and lastestMsg != lastestTmp:
                facebook.sendMsg(lastestMsg)
