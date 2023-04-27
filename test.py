from tkinter import *
import speedtest

root = Tk()
root.title("Internet Speed Meter")
root.geometry('500x700')
root.config(bg="blue")


def speedcheck():
    s = speedtest.Speedtest()
    s.get_servers()
    
    down = s.download()
    down = round(down / (10**6), 2)
    down = str(down) + " Mbps"
    
    up = str(round(s.upload() / (10**6),2)) + " Mbps"
    
    down_speed_result.config(text=down)
    up_speed_result.config(text=up)
    
    result_img = s.results.share()
    print(result_img)
    

up_speed_lab = Label(root, text="Internet Speed Test", font=('Times new roman', 30, 'bold'), bg='blue' )
up_speed_lab.place(x=60, y=40, height=50, width=380)

up_speed_lab = Label(root, text="Download Speed", font=('Times new roman', 30, 'bold', ))
up_speed_lab.place(x=40, y=130, height=50, width=380)

down_speed_result = Label(root, text="00", font=('Times new roman', 30, 'bold', ))
down_speed_result.place(x=40, y=200, height=50, width=380)

up_speed_lab = Label(root, text="Upload Speed", font=('Times new roman', 30, 'bold', ))
up_speed_lab.place(x=40, y=290, height=50, width=380)

up_speed_result = Label(root, text="00", font=('Times new roman', 30, 'bold', ))
up_speed_result.place(x=40, y=360, height=50, width=380)

test_button = Button(root, text = "Start Test", font=('Arial', 30, 'bold'), 
                     relief='ridge', bg='red', fg='white', command=speedcheck)
test_button.place(x=40, y=460, height=50, width=380)


root.mainloop()