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
        
        print(self.username)
        if self.username == '':
            pass
        else:
            print(self.chrome_driver.title)
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
                                sleep(self.delay // 2)
                                
                                # try:
                                #     first_class_data  = self.chrome_driver.find_elements(By.CLASS_NAME , "a-unordered-list a-nostyle a-vertical")
                                #     for first_link in first_class_data:
                                #         print(first_link.text)
                                # except Exception as first_link_error:
                                #     print(f"First Class Error {first_link_error}")
                                
                                try:
                                    selector  = self.chrome_driver.find_elements(By.CSS_SELECTOR , "a.a-link-normal.yohtmlc-order-details-link")
                                    for each in selector:
                                        print(each.get_attribute('href'))
                                except Exception as second_class_error:
                                    print(f"Second Class Error {second_class_error}")
                                # price_data  = self.chrome_driver.find_elements(By.CLASS_NAME , 'yohtmlc-product-title')
                                # # price_data  = self.chrome_driver.find_elements(By.XPATH , '//*[@id="a-page"]/section/div[1]/div[15]/div/div[1]/div/div/div/div[1]/div/div[2]/div[2]/span')
                                
                                # # self.csv_saving(price_data)
                                # for element in price_data:
                                #     self.csv_saving(element.text)

                                # try:
                                #     current_amount  = self.chrome_driver.find_elements(By.CLASS_NAME , "a-color-secondary value") #a-size-base a-color-secondary   a-size-base a-color-secondary
                                # except Exception as first_error:
                                #     print(first_error)
                                
                                # try:
                                #     current_amount  = self.chrome_driver.find_elements(By.CLASS_NAME , 'a-size-base a-color-secondary')
                                # except Exception as second_error:
                                #     print(second_error)
                                
                                # for each in current_amount:
                                #     print("reached and corected ")
                                #     print(each)
                                #     print(each.get_attribute('value'))
                        except Exception as page_error:
                            print(f"Pagenation error {page_error}")
                    current_number-=1
                    sleep(self.delay // 2)
                except Exception as main_error:
                    print(main_error)
                    return
    
    def csv_saving(self , element):
       
        
        try:
            with open('scrapped.csv' , mode='a' ,newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([element])
        except Exception as error:
            print(error)
            
            
'''

order-card js-order-card



a-box-group a-spacing-base order js-order-card


currencyINRFallback

a-color-secondary value

a-link-normal




'''