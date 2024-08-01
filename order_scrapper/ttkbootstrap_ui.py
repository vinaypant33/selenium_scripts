import ttkbootstrap as btk
import threading


import selenium_scrapper_2




def ui():
    
    
    def data_scrapping():
        pass
    
    def checkbox_checked():
        if unpwd_const.get() ==1 :
            print("1")
            main_window.geometry("300x225")
            username_entry = btk.Entry(main_window  , width=45)
            password_entry = btk.Entry(main_window , show="*" , width=45)
            
            username_entry.insert( 0 , "vinaypant24@gmail.com")
            password_entry.insert(0 , "Stillconquering@229")
            
            username_entry.place(x = 10 , y = 155)
            password_entry.place(x = 10 , y = 185)
            
        else:
            print("0")
            main_window.geometry("300x155")
    
    
    main_window = btk.Window()
    
    #constants for the username and password
    unpwd_const  = btk.IntVar()
    unpwd_const.set(0)
    
    
    main_window.title("Amazon Scrapper")
    main_window.geometry("300x155")
    main_window.resizable(0,0)
    
    # Controls for the Main application : 
    page_depth  = btk.Label(main_window , text="Page Depth")
    depth_selector  = btk.Spinbox(main_window , from_=1 , to=30)
    sleep_label = btk.Label(main_window , text="Select Wait Time")
    sleep_selector  = btk.Spinbox(main_window , from_=1 , to=20)
    auto_selector_unpwd = btk.Checkbutton(main_window , text="Auto Enter Username and Password"  ,variable=unpwd_const , command=checkbox_checked)
    start_button  = btk.Button(main_window , text="Start Scrapping" , width=18)
    stop_button = btk.Button(main_window , text="Stop Scrapping" , width=18)
    
    
    
    
    depth_selector.set(5)
    sleep_selector.set(10)
    
    
    
    
    page_depth.place(x = 10 , y = 20)
    depth_selector.place(x = 120 , y = 10)
    sleep_label.place(x = 10 , y = 55)
    sleep_selector.place(x = 120 , y = 50)
    auto_selector_unpwd.place(x = 10 , y = 90)
    start_button.place(x =10 , y = 120)
    stop_button.place(x = 160 , y = 120)
    main_window.mainloop()




ui_thread  = threading.Thread(target=ui)





if __name__ =='__main__':
    # thread to handle the main application 
    ui_thread.start()
    ui_thread.join()