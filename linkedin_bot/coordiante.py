


import pyautogui
from time import sleep

visible_button = "D:\Freelance Work\current_git_hub\selenium_scripts\linkedin_bot\connect_button_visible.png"
hidden_button = "D:\Freelance Work\current_git_hub\selenium_scripts\linkedin_bot\connect_hidden_1.png"



sleep(3)


coordinattes_1  = pyautogui.locateOnScreen(visible_button)
if coordinattes_1:
    print(f"Printed the coordinates_1 as {coordinattes_1}")
else:
    coordinates_2  = pyautogui.locateOnScreen(hidden_button)
    if coordinates_2:
        print(f"Printed the coordinates_2 as {coordinates_2}")
    else:
        print("Unable to find any coordinates")