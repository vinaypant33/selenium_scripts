from bs4 import BeautifulSoup

# Your HTML snippet
html_content = """
<!-- Paste the HTML content here -->
"""

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the name
name = soup.find('a', class_='QKwVMNcugJZCSCraHfEjkhgrjQqBBdvPIrI')
name_text = name.get_text(strip=True) if name else "Name not found"

# Extract the job title and company
job_title_company = soup.find('div', class_='cesUrSERKWpafEWlNUJUYAicYwWVgbiQKwwU t-14 t-black t-normal')
job_title_company_text = job_title_company.get_text(strip=True) if job_title_company else "Job title or company not found"

# Extract the location
location = soup.find('div', class_='NUVcpIVwXOTmywJoLAacAoFgUrLkLSRAwWtJ t-14 t-normal')
location_text = location.get_text(strip=True) if location else "Location not found"

# Print extracted information
print(f"Name: {name_text}")
print(f"Job Title and Company: {job_title_company_text}")
print(f"Location: {location_text}")



 #searchbox  = WebDriverWait(driver , waiting).until(EC.visibility_of_element_located((By.XPATH , '//*[@id="global-nav-typeahead"]/input')))
# searchbox.send_keys("HR Ireland")
# pyautogui.press('enter')
            # try:
            #     location  = element.locationd
            #     x_location  = location["x"]
            #     y_location  = location["y"]
            #     print(x_location)
            #     print(y_location)

            #     # pyautogui.moveTo(981 , 183 ,duration=4)
            #     sleep(microwaiting)
            #     print(pyautogui.position())

            #     # # element.click()
            #     # location  = element.location

            #     # x_value  =  location['x']
            #     # y_value  = location['y']
                
            #     # window_position = driver.execute_script("return {x: window.screenX, y: window.screenY};")

            #     # x_value  =  window_position['x'] + location['x']
            #     # y_value  = window_position['y'] + location['y']
            #     # driver.minimize_window()
            #     # sleep(microwaiting)
            #     # driver.maximize_window()
            #     # pyautogui.moveTo(x_value  , y_value , duration=2)
            #     # pyautogui.click()
               
            # except Exception as error:
            #     messagebox.showerror("Linkedin Bot Error :" , error)
            # # print(element)
            
        # if 'connect' in element.text:
        #     element.click()
            # sleep(waiting)


