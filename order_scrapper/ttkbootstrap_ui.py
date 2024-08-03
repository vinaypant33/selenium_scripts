import ttkbootstrap as btk
import threading


from main_scrapper import Scrapper


def ui():
    
    def thread_started():
        print(current_username)
        webdriver  = Scrapper(username=current_username , password=current_password)
        # webdriver = Selenium_scrapper()
        webdriver.opening_tabs()
        
        
    def checking_():
        global is_working
        current_status  = is_working
        if is_working == True:
            pass
        else:
            return
        main_window.after(1000 , checking_)
    
    def data_scrapping():
        global thread_count
        thread_count+=1
        if thread_count <= 1:
            scrapping_thread  = threading.Thread(target=thread_started)
            scrapping_thread.start()
            scrapping_thread.join()
        else:
            print("thread already started")
            
    
    def stop_scrapping():
        global is_working
        is_working = False
    
    def checkbox_checked():
        if unpwd_const.get() ==1 :
            main_window.geometry("300x225")
            username_entry = btk.Entry(main_window  , width=45)
            password_entry = btk.Entry(main_window , show="*" , width=45)
            username_entry.insert( 0 , "vinaypant24@gmail.com")
            password_entry.insert(0 , "Stillconquering@2290")
            username_entry.place(x = 10 , y = 155)
            password_entry.place(x = 10 , y = 185)
            
            global current_username
            global current_password
            
            current_password = username_entry.get()
            current_password = password_entry.get()
            
        else:
            main_window.geometry("300x155")
    
    
    main_window = btk.Window()
    
    #constants for the username and password
    unpwd_const  = btk.IntVar()
    unpwd_const.set(0)
    
    global is_working
    is_working  = True
    
    global thread_count
    thread_count  = 0
    
    global current_username
    global current_password
    
    current_username = ''
    current_password  = ''
    
    
    main_window.title("Amazon Scrapper")
    main_window.geometry("300x155")
    main_window.resizable(0,0)
    
    # Controls for the Main application : 
    page_depth  = btk.Label(main_window , text="Page Depth")
    depth_selector  = btk.Spinbox(main_window , from_=1 , to=30)
    sleep_label = btk.Label(main_window , text="Select Wait Time")
    sleep_selector  = btk.Spinbox(main_window , from_=1 , to=20)
    auto_selector_unpwd = btk.Checkbutton(main_window , text="Auto Enter Username and Password"  ,variable=unpwd_const , command=checkbox_checked)
    start_button  = btk.Button(main_window , text="Start Scrapping" , width=18 , command=data_scrapping)
    stop_button = btk.Button(main_window , text="Stop Scrapping" , width=18 , command=stop_scrapping)
    
    
    depth_selector.set(5)
    sleep_selector.set(10)
    
    
    
    
    page_depth.place(x = 10 , y = 20)
    depth_selector.place(x = 120 , y = 10)
    sleep_label.place(x = 10 , y = 55)
    sleep_selector.place(x = 120 , y = 50)
    auto_selector_unpwd.place(x = 10 , y = 90)
    start_button.place(x =10 , y = 120)
    stop_button.place(x = 160 , y = 120)
    checking_()
    main_window.mainloop()




ui_thread  = threading.Thread(target=ui)





if __name__ =='__main__':
    # thread to handle the main application 
    ui_thread.start()
    ui_thread.join()