from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from tqdm import tqdm

# For Reference: 
import pyautogui

import csv

from tkinter import messagebox


current_scrapper_data = []


class Scrapper():
    
    
    def __init__(self , username = '' , password = '' , delay = 10) -> None:
        self.delay = delay
        self.username  = 'vinaypant24@gmail.com'
        self.password = 'Stillconquering@2290'
        
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
                sleep(self.delay * 2)
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
                                            current_amount  = self.chrome_driver.find_element(By.XPATH , '/html/body/div[1]/div[1]/div[1]/div[11]/div/div/div/div/div/div[2]/div[1]/div[2]/span/span/span[2]')
                                            # current_amount  = self.chrome_driver.find_element(By.CLASS_NAME , 'currencyINRFallback')
                                            
                                            inner_text = self.chrome_driver.execute_script("return arguments[1].innerText;", current_amount)
                                            print(inner_text)

                                            
                                            
                                        except Exception as error:
                                            print(error)
                                        
                                        
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
    
    
    def opening_tabs(self):
        length  = len(current_scrapper_data)
        print(length)
        
    
    def csv_saving(self , element):
        try:
            with open('scrapped.csv' , mode='a' ,newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([element])
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