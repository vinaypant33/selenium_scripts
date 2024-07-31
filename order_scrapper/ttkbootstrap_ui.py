import ttkbootstrap as btk
import threading





def data_scrapping():
    pass
    


def ui():
    main_window = btk.Window()
    main_window.title("Amazon Scrapper")
    main_window.geometry("300x300")
    main_window.resizable(0,0)
    
    # Controls for the Main application : 
    page_depth  = btk.Label(main_window , text="Page Depth")
    
    
    
    
    
    page_depth.place(x = 0 , y = 0)

    main_window.mainloop()




ui_thread  = threading.Thread(target=ui)





if __name__ =='__main__':
    # thread to handle the main application 
    ui_thread.start()
    ui_thread.join()