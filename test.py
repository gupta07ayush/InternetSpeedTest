from tkinter import *
import speedtest
import time
from PIL import ImageTk, Image

root = Tk()  # object of tkinter module
root.title("Internet Speed Meter")
root.geometry('600x600')  # default size of tkinter window
root.config(bg="#1b4965")  # background color of the window


def speedcheck():
    ''' Function which does internet speed test '''
    st_obj = speedtest.Speedtest()  # s is the object of speedtest module
    st_obj.get_servers()

    down = st_obj.download()  # gives download speed in bits
    down = round(down / (10**6), 2)  # converts MBps into Mbps
    down = str(down) + " Mbps"

    # use single line to do the same to down which took 3 lines
    up = str(round(st_obj.upload() / (10**6), 2)) + " Mbps"

    # sends down and up test results to tkinter label
    down_speed_result.config(text=down)
    up_speed_result.config(text=up)

    # Gives url of the image which contains the test results.
    result_img = st_obj.results.share()
    print(result_img)

    for i in range(1, 11):
        root.update()
        time.sleep(1)
        countdown.config(text=i)


heading_back = Label(root, bg='#252422', borderwidth=5, relief=SOLID)
heading_back.place(x=0, y=0, height=100, width=600)

heading_lab = Label(root, text="Internet Speed Test", font=(
    'Time new roman', 30, 'bold'), bg='#252422', fg='#ffffff')
heading_lab.place(x=60, y=30, height=50, width=480)

down_speed_lab = Label(root, text="Download\nSpeed",
                       font=('Times new roman', 23, 'bold'), bg='#4cc9f0')
down_speed_lab.place(x=50, y=180, height=90, width=180)

down_speed_result = Label(root, text="00", font=(
    'Times new roman', 25, 'bold', ), bg='#f2e9e4')
down_speed_result.place(x=50, y=300, height=50, width=180)

up_speed_lab = Label(root, text="Upload\nSpeed",
                     font=('Times new roman', 23, 'bold', ), bg='#4cc9f0')
up_speed_lab.place(x=370, y=180, height=90, width=180)

up_speed_result = Label(root, text="00", font=(
    'Times new roman', 25, 'bold', ), bg='#f2e9e4')
up_speed_result.place(x=370, y=290, height=50, width=180)

test_button = Button(root, text="Start Test", font=('Arial', 30, 'bold'), bd=3,
                     relief='ridge', bg='#22223b', fg='white', command=speedcheck)
test_button.place(x=40, y=480, height=70, width=520)

countdown = Label(root, text='0', font=('arial', 70, 'bold'), bg='#1b4965')
countdown.place(x=270, y=360)

# mainloop at the end of the line which creates the tkinter window
root.mainloop()
