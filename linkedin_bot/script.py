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





working  = True  
sleep_time  = 60
waiting  = 15
current_username  = ""
current_password  = ""
safe_requests  = 10
current_count = 0
total_requests  = 300
link_list  = []
microwaiting  = 2
connections  = 30


current_username  = str(input("Enter Username : "))
current_password = str(input("Enter Current Password :"))

print("Starting Bot .....")

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


sleep(waiting *  2)

for i in range(connections):
    
    try:
        i+=1
        driver.get(f"https://www.linkedin.com/search/results/people/?keywords=HR Ireland&page={i}")
        try:
            link_element  = driver.find_elements(By.CLASS_NAME , "QKwVMNcugJZCSCraHfEjkhgrjQqBBdvPIrI")
        except Exception as link_error:
            messagebox.showerror("Link Error" , link_error)
            sys.exit()
        
        try:
            for link in link_element:
                actual_link  = link.get_attribute("href")
                if "www.linkedin.com/in/" in actual_link:
                    link_list.append(actual_link)
        except Exception as link_read_error:
            messagebox.showerror("Link Read Error" , link_read_error)
        
        try:
            for each_link in link_list:
                driver.execute_script(f"window.open('{each_link}', '_blank');")
                try :
                    button_element = driver.find_element(By.CSS_SELECTOR , "span")
                except Exception as button_error:
                    messagebox.showerror("Linkedin Bot" , "Connect Button not Available")
                    continue
                try:
                    for link in link_list:
                        try:
                            # print(element.text)
                            # if element.get_attribute("innerText") == "connect":

                                sleep(microwaiting * 3)
                                pyautogui.moveTo(900 ,520 , 1)
                                pyautogui.click()
                                sleep(microwaiting)
                                pyautogui.moveTo(538 , 1000 , 2)
                                pyautogui.click()
                                pyautogui.click()
                                pyautogui.moveTo(1284 , 475 , 2) #1290 515
                                pyautogui.click()
                                multi_line_string = "\n".join([
                                    "Hi,",
                                    "I am heading to Ireland this January for my MS in Data Analytics and am looking to expand my network. I came across your profile and thought connecting, exploring synergies, and learning from your experience would be great.",
                                    "Looking forward to connecting!",
                                    "Best",
                                    "Vinay"])
                                pyautogui.write(multi_line_string)
                                pyautogui.moveTo(1614 , 771, 1)
                                pyautogui.click()
                                driver.switch_to.window(driver.window_handles[1])
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])
                                break
                        except Exception as button_element_error:
                            messagebox.showerror("Button Element Error" , button_element_error)
                except Exception as element_error:
                    messagebox.showerror("Element Error " , element_error)
        except Exception as iteration:
            messagebox.showerror("Unable to Iterate" , iteration)


    except Exception as page_error:
        messagebox.showerror("Page Error" , page_error)
        sys.exit()

