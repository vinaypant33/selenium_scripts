import os
import sys
import pyautogui
import keyboard

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


from bs4 import BeautifulSoup


search_pages  = 1
current_username  = ""
current_password = ""
keywords  = ""




visible_button = "linkedin_bot/connect_button_visible.png"
hidden_button = "linkedin_bot/connect_hidden_1.png"



waiting  = 15 
microwaiting  = 2
link_list  = []

# Will get the user input here :
current_username = str(input("Enter Username  : "))
current_password = str(input("Enter Password : "))
keywords  = str(input("Enter Keywords Seperated By Space : "))

print("Starting Bot......")

options  = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("--disable-webrtc")  # Disable WebRTC
options.add_argument("--log-level=3")    # Reduce log verbosity
# options.add_argument("--headless") # Used to make invisible browser ( can be used instead of http requests )


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

sleep(microwaiting * 2)

try:
    driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[4]/button').click()
except Exception as button_error:
    messagebox.showerror("Linkedin Bot"  , f"Unable to find the login button {button_error}")
    sys.exit()



sleep(waiting)

for i in tqdm(range(search_pages)):
    driver.get(f"https://www.linkedin.com/search/results/people/?keywords={keywords}&page={i}")
    sleep(microwaiting)
    page_source = driver.page_source
    # print(page_source)
    soup = BeautifulSoup(page_source, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href :
            if "www.linkedin.com/in/" in href:
                link_list.append(href)
    driver.minimize_window()
    sleep(microwaiting)
    print(len(link_list))
    driver.maximize_window()



link_list = list(set(link_list))
# print(len(link_list))

# for link in link_list:
#     print(link)

with open("link_file.txt", "w") as file:
    for line in link_list:
        file.write(line + "\n")




# for each in link_list:
#     driver.get(each)
#     sleep(microwaiting)
#     try:
#         coordinattes_1  = pyautogui.locateOnScreen(visible_button)
#         if coordinattes_1:
#             print(f"Printed the coordinates_1 as {coordinattes_1}")
#         else:
#             try:
#                 coordinates_2  = pyautogui.locateOnScreen(hidden_button)
#                 if coordinates_2:
#                     print(f"Printed the coordinates_2 as {coordinates_2}")
#                 else:
#                     print("Unable to find any coordinates")
#             except Exception as image_error:
#                 print("Image Error" , image_error)
#     except Exception as first_error:
#         print("First Error {first_error}") 




def sending_message(name , id):
    if name:
        custom_message = "\n".join([
                                    f"Hi {name},",
                                    "I am heading to Ireland this January for my MS in Data Analytics and am looking to expand my network. I came across your profile and thought connecting, exploring synergies, and learning from your experience would be great.",
                                    "Looking forward to connecting!",
                                    "Best",
                                    "Vinay"])
    else:
        
        custom_message = "\n".join([
                                    "Hi ,",
                                    "I am heading to Ireland this January for my MS in Data Analytics and am looking to expand my network. I came across your profile and thought connecting, exploring synergies, and learning from your experience would be great.",
                                    "Looking forward to connecting!",
                                    "Best",
                                    "Vinay"])
        

    
    
    
    driver.find_element(By.ID , id).click()
    sleep(microwaiting )
    pyautogui.moveTo(1280 , 525 , 2) #1290 515
    pyautogui.click()
    pyautogui.write(custom_message)
    sleep(microwaiting)
    pyautogui.moveTo(1614 , 771, 1)
    pyautogui.click()






for each in link_list:

    driver.get(each)
    sleep(microwaiting *  5)
    try:
        element   = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button')
        # print(element.get_attribute('id'))
        try:
            name_element = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1')
            sending_message(name_element.get_attribute('innerText') , element.get_attribute('id'))
        except Exception as name_error:
            print('Unable to get the name : ')
    except Exception as error:
        print(f"First Error Trying Second Approach")
        try:
            driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button/span')
            print(element.get_attribute('id'))
            try:
                name_element = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1')
                ending_message(name_element.get_attribute('innerText') , element.get_attribute('id'))
            except Exception as name_error:
                print('Unable to get the name : ')
        except Exception as error:
            print(f"Second Error Trying Third Approach")
            try:
                driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[3]/div/span')
                print(element.get_attribute('id'))
                try:
                    name_element = driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1')
                    sending_message(name_element.get_attribute('innerText') , element.get_attribute('id'))
                except Exception as name_error:
                    print('Unable to get the name : ')
            except Exception as error:
                print(f"Third Approach Failed : Saving URl for Further Analysis")
                with open("checking_urls.txt", "a") as file:
                        file.write(each + "\n")


        

driver.close()
driver.quit()
sys.exit()

