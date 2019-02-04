#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import selenium
from selenium import webdriver
from getpass import getpass 
from cleverbot import Cleverbot

import os

class Messenger:
    def __init__(self):
        self.driver = webdriver.Firefox() # Because Firefox is better 
        self.driver.get("https://www.messenger.com")

    def login(self, username: str, password: str):
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("pass").send_keys(password)
        self.driver.find_element_by_name("login").click()

    def getReceiverName(self) -> str:
        name = self.driver.find_element_by_class_name("_3oh-").text
        return name.replace("à", "a").replace("ï", "i").replace("ô", "o").replace("ê", "e").replace("é", "e").replace("è", "e").lower()

    def getMsg(self) -> str:
        return self.driver.find_elements_by_xpath("//*[contains(@class, '_aok')]")[-1].text

    def send(self, msg):
        try:
            self.driver.find_element_by_class_name("notranslate").send_keys(msg)
            self.driver.find_element_by_class_name("_38lh").click()

        except selenium.common.exceptions.NoSuchElementException:
            return 1

    def quit(self):
        self.driver.quit()

def waitAnswer(msg=""):
    while ai.get() == msg:
        continue
    return True

if __name__ == "__main__":
    lastestMsg = ""
    bot = Messenger()
    print("Loading the Cleverbot API...")
    ai = Cleverbot()
    
    username = input("Login: ")
    password = getpass(prompt="Password: ")

    bot.login(username, password)

    input("Press enter, when you are ready ...")

    ai.send("Hi, my name is {bot.getReceiverName()} ")
    
    waitAnswer()
    bot.send(ai.get())
    lastestMsg = ai.get()


    while True:
        if bot.getMsg() != lastestMsg:
            print(lastestMsg)
            ai.send(bot.getMsg())
            waitAnswer(lastestMsg)
            bot.send(ai.get())
            lastestMsg = ai.get()


    bot.quit()
    exit()
    