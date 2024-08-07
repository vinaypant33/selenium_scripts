from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from tqdm import tqdm

import requests
import os

# For Reference: 
import pyautogui

import csv

from tkinter import messagebox

from pubsub import pub

current_scrapper_data = []


class Scrapper():
    
    
    def __init__(self , username = '' , password = '' , delay = 10) -> None:
        
        pub.sendMessage('message')
        self.delay = delay
        self.username  = 'vinaypant24@gmail.com'

        self.user_password_input  = input("Enter Password for Loggin In : ")
        self.password = self.user_password_input
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach' , True)
        self.chrome_driver = webdriver.Chrome(options=options)
        
        # self.chrome_driver.maximize_window()
        
        self.chrome_driver.get(r"https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        sleep(self.delay)
        
        if self.username == '':
            pass
        else:
            try:
                current_username_selection  = self.chrome_driver.find_element(By.NAME , "email")
                current_username_selection.send_keys(self.username)
                continue_button = self.chrome_driver.find_element(By.ID , 'continue').click()
                current_password_selection  = self.chrome_driver.find_element(By.NAME , 'password')
                current_password_selection.send_keys(self.password)
                password_button  = self.chrome_driver.find_element(By.ID , 'signInSubmit').click()
                sleep((self.delay * 2)+5)
                print(self.chrome_driver.title)
            except Exception as login_error:
                print(login_error)
                print('Unable to Login , waiting for Delay to login ')
                sleep(self.delay * 3)
            
            
            current_number = 2024
            for i in range(15):
                try:
                    self.chrome_driver.get(f'https://www.amazon.in/your-orders/orders?timeFilter=year-{current_number}')
                    current_title = self.chrome_driver.title
                    if current_title == 'Your Orders':
                        try:
                            for i in range(15):
                                self.chrome_driver.get(f'https://www.amazon.in/your-orders/orders?timeFilter=year-{current_number}&startIndex={i * 10}')
                                sleep(self.delay // 3)
                                
                                # Data Scrapping :
                                order_links  = self.chrome_driver.find_elements(By.CLASS_NAME , "a-link-normal")
                                for each in order_links:
                                    if "View order details" in each.text:
                                        # curent_order_link = each.get_attribute('href')
                                        # print(curent_order_link)
                                        self.other  = self.chrome_driver.execute_script(f"window.open('{each.get_attribute('href')}', '_blank');")
                                        
                                        sleep(self.delay // 3)
                                        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[1])
                                        
                                        try:
                                            date = self.chrome_driver.find_element(By.CLASS_NAME , 'order-date-invoice-item')
                                            payment_method  = self.chrome_driver.find_element(By.XPATH , '//*[@id="orderDetails"]/div[1]/div[11]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/ul/li/span')
                                            current_amount  = self.chrome_driver.find_element(By.CSS_SELECTOR , ".a-column.a-span5.a-text-right.a-span-last")
                                            item_name = self.chrome_driver.find_element(By.CSS_SELECTOR , ".a-fixed-left-grid-col.yohtmlc-item.a-col-right .a-row a.a-link-normal")
                                        except Exception as error:
                                            print(error)
                                            self.chrome_driver.close()
                                            self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[0])
                                            continue
                                        

                                        modified_text  = item_name.text.replace("," , "")

                                        # print(item_name.text)
                                        # print(modified_text)
                                        order_date_modified  = date.text.replace("Ordered on " , "")

                                        aa  = [f'{order_date_modified},{payment_method.text},{current_amount.text},{modified_text}']
                                        
                                        print(f'Procured Date {date.text} , Payment Method : {payment_method.text}, Current Amount : {current_amount.text}, Item_Name : {item_name.text}')
                                        self.csv_saving(aa)
                                        
                                        try:
                                            image_element  = self.chrome_driver.find_element(By.CSS_SELECTOR , 'img.yo-critical-feature')
                                            image_url  = image_element.get_attribute("src")
                                            folder_path = 'downloaded_images'
                                            response = requests.get(image_url)
                                            os.makedirs(folder_path, exist_ok=True)
                                            image_name = os.path.basename(f"{modified_text}.jpg")
                                            # image_name  = os.path.basename(image_url)
                                            image_path = os.path.join(folder_path, image_name)

                                            with open(image_path, 'wb') as file:
                                                file.write(response.content)
                                        except Exception as another_pass:
                                            print(another_pass)
                                            
                                        
                                        self.chrome_driver.close()
                                        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[0])
                                    
                                    # print(each.text)
                        except Exception as page_error:
                            print(f"Pagenation error {page_error}")
                    current_number-=1
                    sleep(self.delay // 2)
                except Exception as main_error:
                    print(main_error)
                    return
    
        self.chrome_driver.close()
        print("Scrapping Completed")
        
        pub.sendMessage('message')
        
    
    def opening_tabs(self):
        length  = len(current_scrapper_data)
        print(length)
        
    
    def csv_saving(self , element):
        try:
            with open('scrapped.csv' , mode='a' ,newline='') as file:
                csv_writer = csv.writer(file)
                # csv_writer.writerow([element])   # This only for the single item
                for entry in element:
                    main_element  = entry.split(',')
                    csv_writer.writerow(main_element)
                # csv_writer.writerow(element)
        except Exception as error:
            print(error)
            
    def csv_saving_list(self , element_list):
        try:
            with open('finalscrapper.csv' , mode='a' , newline='') as file:
                csv_writer = csv.writer(file)
                for row in element_list:
                    csv_writer(row)
        except Exception as list_error:
            print(list_error)