import os
import sys
from selenium import webdriver
from typing import Any
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
# For showing the sequence in the cmd : 
from tqdm import tqdm
# For showing the messagebox in case of the error which needs to be recorded : 
from tkinter import messagebox
import pyautogui




'''
How it works : 
1. Make a text file for the keywords for which the bot will send the connect requestes the name of the file should be keywords or else it won't work. 
2. Make another text file for the country specific if there is any or else it would only search for the keywords not the country : will change this to Tkinter based UI later
3. It makes a log file which contains the current time and the error log to check later

'''


working  = True
sleep_time  = 60
waiting = 10
current_username  = ""
current_password  = ""
safe_requestes  = 10
current_count  = 0 
total_rqeustes  = 300


# current_username = input("Enter Username :")
current_password = input("Enter Password : ")

print("Starting the Selenium Bot ")

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver  = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
driver.maximize_window()

# Login and Check for Credentials : 
try:
    username  = driver.find_element(By.ID , "username")
    username.send_keys("vinaypant24@gmail.com")
except Exception as username_error:
    messagebox.showerror("Linkedin Bot" , f"Username Error  {username_error}")
    sys.exit()


try:
    password = driver.find_element(By.ID , "password")
    password.send_keys(current_password)
except Exception as password_error:
    messagebox.showerror("Linkedin Bot" , f"Password Error {password_error}")
    sys.exit()

try:
    driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[4]/button').click()
except Exception as button_error:
    messagebox.showerror("Linkedin Bot"  , f"Unable to find the login button {button_error}")



# sleep(waiting)

# Check for the searchbox and then wait for the searchbox to load : 













sleep(sleep_time)
driver.close()
driver.quit()

