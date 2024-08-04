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
        self.username  = ''
        self.password = ''
        
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
                                
                                try:
                                    selector  = self.chrome_driver.find_elements(By.CSS_SELECTOR , "a.a-link-normal.yohtmlc-order-details-link")
                                    for each in selector:
                                        self.other  = self.chrome_driver.execute_script(f"window.open('{each.get_attribute('href')}', '_blank');")
                                        sleep(self.delay // 4)
                                        # sleep(self.delay * 3)
                                        
                                        try:
                                            
                                            date = self.chrome_driver.find_elements(By.CLASS_NAME , 'order-date-invoice-item')
                                            for child in date:
                                                print(child.text)
                                            # procured_date  = self.chrome_driver.find_element(By.XPATH , '//*[@id="orderDetails"]/div[1]/div[9]/div[1]/div[1]/div/span[1]')
                                            # payment_method  = self.chrome_driver.find_element(By.XPATH ,'//*[@id="orderDetails"]/div[1]/div[11]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/ul/li/span')
                                            # product_name = self.chrome_driver.find_element(By.XPATH , '//*[@id="orderDetails"]/div[1]/div[13]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[1]/a')
                                            # price = self.chrome_driver.find_element(By.XPATH , '//*[@id="od-subtotals"]/div[6]/div[2]/span/span/span[2]')
                                            
                                            # print(payment_method.text)
                                            # pass
                                        
                                            
                                            # print(f'Product Name : {product_name.text}, Procured Date : {procured_date.text}, Payment Method : {payment_method.text}, Price : {price.text}')
                                            
                                            
                                        except Exception as link_error:
                                            print(link_error)
                                            # messagebox.showerror("" , str(link_error))
                                        # print("i am gonna length the seelctor")
                                        # print(len(selector))
                                        sleep(self.delay // 4)
                                        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[1])
                                        self.chrome_driver.close()
                                        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[0])
                                        
                                        
                                        # self.other.close()
                                        # self.csv_saving(each.get_attribute('href'))
                                        # pass
                                        # print(each.get_attribute('href'))
                                        # current_scrapper_data.append(each.get_attribute('href'))
                                        
                                        
                                except Exception as second_class_error:
                                    print(f"Second Class Error {second_class_error}")
                                    
                                # yohtmlc-order-level-connections
                                
                                # try:
                                #     selector  = self.chrome_driver.find_elements(By.CSS_SELECTOR , "a-link-normal")
                                #     for each in selector:
                                #         if "View order details" in each.text:
                                #             self.other  = self.chrome_driver.execute_script(f"window.open('{each.get_attribute('href')}', '_blank');")
                                #             sleep(self.delay // 3)
                                #             print(len(selector))
                                #             sleep(self.delay)
                                #             self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[1])
                                #             self.chrome_driver.close()
                                #             self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[0])
                                # except Exception as second_error:
                                #     print(second_error)
                                
                            print("Execution Completed")
                                
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
