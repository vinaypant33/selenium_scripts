import os
import sys

from selenium import webdriver
from typing import Any
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from tqdm import tqdm
from tkinter import messagebox
import pyautogui
import keyboard



crawl_pages  = 10
link_list  = []
waiting_time  = 10
microwaiting  = 1
keywords  = "HR Ireland"

print("Starting Bot......")

options  = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("--disable-webrtc")  # Disable WebRTC
options.add_argument("--log-level=3")    # Reduce log verbosity


driver  = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
driver.maximize_window()


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
    sys.exit()



sleep(waiting_time *  4)

for i in tqdm(range(crawl_pages)):
    sleep(microwaiting *  2)
    try:
        driver.get(f"https://www.linkedin.com/search/results/people/?keywords={keywords}&page={i}")
        try:
            link_element  = driver.find_elements(By.CLASS_NAME , "VqtxQbWoLpIbcJnGtZXbaJEBDNpAbVzwGjIU")
            try:
                for link in link_element:
                    actual_link  = link.get_attribute("href")
                    if "www.linkedin.com/in/" in actual_link:
                        link_list.append(actual_link)
            except Exception as list_error:
                messagebox.showerror("Link Error" , list_error)
        except Exception as link_error:
            messagebox.showerror("Link Error" , link_error)
            sys.exit()
    except Exception as page_reading_error:
        messagebox.showerror("Page Error" , page_reading_error)


link_list = list(set(link_list))


# for i in range(100):
#     link_list.append(i)


print(f"Scrapping Completed.......")
print("Starting Sending Requests ............")



print(len(link_list))

for link in link_list:
    try:
        driver.execute_script(f"window.open('{link}', '_blank');")
        print(link_list[i])
        try:
            conect_button  = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button/span')
            sleep(microwaiting * 2 )
        except Exception as find_span_error:
            messagebox.showerror("Finding Error" , find_span_error)
    except Exception as parsing_error:
        messagebox.showerror("Parsing Error" , parsing_error)

