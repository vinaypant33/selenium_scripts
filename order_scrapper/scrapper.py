from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from tqdm import tqdm

# For temporary solution : Closing automated browser  : 
import pyautogui

'''
# Press and hold the first key
pyautogui.keyDown('ctrl')

# Press and hold the second key
pyautogui.keyDown('c')

# Release the second key
pyautogui.keyUp('c')

# Release the first key
pyautogui.keyUp('ctrl')
'''

class Selenium_scrapper():
    
    
    def __init__(self , username  = '' , password = '' , delay = 6  , yearly_selection   = False , autoamted_username  = False) -> None:
        self.delay = delay
        self.username  = username
        self.password = password
        self.yearly_selection  = yearly_selection
        self.automated_username  = autoamted_username
        
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.chrome_driver = webdriver.Chrome(options = options)

        # pyautogui.keyDown('ctrl')
        # pyautogui.keyDown('w')
        # pyautogui.keyUp('ctrl')
        # pyautogui.keyUp('w')
        
        self.chrome_driver.maximize_window()
        
        
        
        self.chrome_driver.get(r"https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        sleep(self.delay)
        
        
        if self.username == '':
            sleep(self.delay * 2)
         
            current_title = self.chrome_driver.title
            print(current_title)
            if current_title == 'Amazon Sign In':
                
                print("Contains")
            else:
                pass
            self.chrome_driver.get('https://www.amazon.in/your-orders/orders?timeFilter=year-2024&ref_=ppx_yo2ov_dt_b_filter_all_y2024')
            
           
        else:
            try:
                
                current_username_selection  = self.chrome_driver.find_element(By.NAME , "email")
                current_username_selection.send_keys(self.username)
                continue_button = self.chrome_driver.find_element(By.ID , 'continue').click()
                current_password_selection  = self.chrome_driver.find_element(By.NAME , 'password')
                current_password_selection.send_keys(self.password)
                password_button  = self.chrome_driver.find_element(By.ID , 'signInSubmit').click()
                sleep(self.delay)
            except Exception as login_error:
                print(login_error)
                print('Unable to Login , waiting for Delay to login ')
                sleep(self.delay * 3)
                
                
            for i in range(15):
                try:
                    current_number = 2024
                    self.chrome_driver.get(f'https://www.amazon.in/your-orders/orders?timeFilter=year-{current_number}&startIndex=0&ref_=ppx_yo2ov_dt_b_pagination_1_1')
                    current_title = self.chrome_driver.title
                    print(current_title)
                    current_number-=1
                    sleep(self.delay // 2)
                except Exception as main_error:
                    print(main_error)
                    return
            
            
    
        
    def close_browser(self):
        self.chrome_driver.close()
        self.chrome_driver.quit()


if __name__ == '__main__':
    main_driver  = Selenium_scrapper()
    
    
    