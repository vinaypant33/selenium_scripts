import tkinter as tk
from tkinter import ttk
from pubsub import pub
from time import sleep
import threading




from scrapper import Selenium_scrapper





def single_threaded_ui():
    main_application  = tk.Tk()
    main_application.title("Amazon Order Scrapper")
    app_width  = 400 
    app_height  = 200
    


    x_location  = ( main_application.winfo_screenwidth() //2 ) - ( app_width //2 )
    y_location  = (main_application.winfo_screenheight() //2 ) - (app_height // 2)
    main_application.geometry(f'{app_width}x{app_height}+{x_location}+{y_location}')
    main_application.resizable( 0 , 0 )

    # Defining Contants : 
    yearly_selectionvar  = tk.BooleanVar()
    username_passwordvar  = tk.BooleanVar()
    is_working  = False

    def start_data_scrapping():
        webdriver  = Selenium_scrapper(username='vinaypant24@gmail.com' , password='Stillconquering@2290')
        
        

    def stop_data_scrapping():
        print("Data Scrapping Stopped")


    # Funcations that are to be added in the main application : 
    def username_password():
        
        print(username_passwordvar.get())
        if username_passwordvar.get() == True:
            # Controls for the username and password  : 
            global username_textbox
            global password_textbox
            username_textbox  = ttk.Entry(main_application , width=40 )
            password_textbox  = ttk.Entry(main_application  , width=40 , show="*")
            
            
            # username_textbox.insert(0 , "Enter Username")
            # password_textbox.insert( 0 , "Enter Password")
            
            username_textbox.insert(0 , 'vinaypant24@gmail.com')
            password_textbox.insert(0 , 'Stillconquering@2290')
            
            username_textbox.bind("<FocusIn>" , lambda e : username_textbox.delete( 0 , 'end'))
            password_textbox.bind("<FocusIn>" , lambda e : password_textbox.delete(0  , "end"))
            
            password_textbox.bind("<KeyRelease>" , lambda e : password_textbox.configure(show="*"))
            username_textbox.place(x = 10 , y  = 120)
            password_textbox.place(x = 10 , y = 150)
        else:
            try:
                username_textbox.destroy()
                password_textbox.destroy()
            except Exception as error:
                print(error)



    start_button  = ttk.Button(main_application  , text="Start Scrapping", width=30 , command=start_data_scrapping)
    stop_button = ttk.Button(main_application  , text="Stop Scrapping" , width=30 , command=stop_data_scrapping)

    # Save data by each year : 
    save_label  = ttk.Label(main_application  , text="Save Data on Yearly Basis : ")
    selction_button  =  ttk.Checkbutton(main_application , text="Save Data on yearly basis : " , variable=yearly_selectionvar)

    username_password_select  = ttk.Checkbutton(main_application , text="Automatically Enter Username Password" , variable=username_passwordvar , command=username_password)


    sleep_label  = ttk.Label(main_application , text="Enter Delay Timer : ")
    sleep_timer  = ttk.Spinbox(main_application  , width=10 , from_=0 , to=10)
    
    sleep_timer.set(7)



    start_button.place(x = 10 , y = 10)
    stop_button.place(x = 205 , y = 10)
    # save_label.place(x = 10 , y = 40)
    selction_button.place(x = 10 , y = 50)
    username_password_select.place(x = 10 , y = 70)
    sleep_label.place(x = 205 , y = 45)
    sleep_timer.place(x = 310 , y = 45)

    main_application.mainloop()


main_thread  = threading.Thread(target=single_threaded_ui)
main_thread.start()

main_thread.join()


print("threading part done")