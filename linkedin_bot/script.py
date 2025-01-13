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

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin

import keyboard



'''
How it works : 
1. Make a text file for the keywords for which the bot will send the connect requestes the name of the file should be keywords or else it won't work. 
2. Make another text file for the country specific if there is any or else it would only search for the keywords not the country : will change this to Tkinter based UI later
3. It makes a log file which contains the current time and the error log to check later

'''


working  = True
sleep_time  = 60
waiting = 15
current_username  = ""
current_password  = ""
safe_requestes  =10
current_count  = 0 
total_rqeustes  = 300
link_list  = []
microwaiting  = 2

# current_username = input("Enter Username :")
# current_password = input("Enter Password : ")


print("Starting the Selenium Bot ")

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

options.add_argument("--disable-webrtc")  # Disable WebRTC
options.add_argument("--log-level=3")    # Reduce log verbosity

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



sleep(waiting)

# Check for the searchbox and then wait for the searchbox to load : 
# Oncde Logged In we can just use the Url for the movement to different search results : 
driver.get("https://www.linkedin.com/search/results/people/?keywords=HR Ireland")

# searchbox  = WebDriverWait(driver , waiting).until(EC.visibility_of_element_located((By.XPATH , '//*[@id="global-nav-typeahead"]/input')))
# searchbox.send_keys("HR Ireland")

# pyautogui.press('enter')

link_element  = driver.find_elements(By.CLASS_NAME , "QKwVMNcugJZCSCraHfEjkhgrjQqBBdvPIrI")


# for link in link_element:
#     print(link.get_attribute("href"))


for link in link_element:
    actual_link  = link.get_attribute("href")
    if "www.linkedin.com/in/" in actual_link:
        link_list.append(actual_link)



for each_link in link_list:
    driver.execute_script(f"window.open('{each_link}', '_blank');")
    button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span"))
        )
    for element in button_element:
        # print(element.get_attribute("innerText"))
        if element.get_attribute("innerText") == "Connect":
            # name   = driver.find_element(By.TAG_NAME , "h1")
            # name   = driver.find_element(By.CLASS_NAME ,"YCdONOXJXKRGeKnrrfqwYMdEHbrpNwqWyw")
            # print(name.get_attribute("innerText"))

            
            try:
                sleep(microwaiting)
                pyautogui.moveTo(538 , 1027 , 2)
                pyautogui.click()
                pyautogui.moveTo(1290 , 515 , 2) #1290 515
                pyautogui.click()

                multi_line_string = "\n".join([

                    "Hi" ,
                    "I’m heading to Ireland this January for my MS in Data Analytics and am looking to expand my network. I came across your profile and thought connecting, exploring synergies, and learning from your experience would be great.",
                    "Looking forward to connecting!",
                    "Best",
                    "Vinay" ])
            except Exception as first_error:
                pass 

                


            try:



                location  = element.location
                x_location  = location["x"]
                y_location  = location["y"]
                print(x_location)
                print(y_location)

                # pyautogui.moveTo(981 , 183 ,duration=4)
                sleep(microwaiting)
                print(pyautogui.position())

                # # element.click()
                # location  = element.location

                # x_value  =  location['x']
                # y_value  = location['y']
                
                # window_position = driver.execute_script("return {x: window.screenX, y: window.screenY};")

                # x_value  =  window_position['x'] + location['x']
                # y_value  = window_position['y'] + location['y']

            
                # driver.minimize_window()
                # sleep(microwaiting)
                # driver.maximize_window()
                # pyautogui.moveTo(x_value  , y_value , duration=2)
                # pyautogui.click()
               
            except Exception as error:
                messagebox.showerror("Linkedin Bot Error :" , error)
            # print(element)
            break
        # if 'connect' in element.text:
        #     element.click()
            # sleep(waiting)

    sleep(microwaiting)




sleep(sleep_time * 3)
driver.close()
driver.quit()

