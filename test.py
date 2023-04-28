from tkinter import *
import speedtest

root = Tk()  # object of tkinter module
root.title("Internet Speed Meter")
root.geometry('460x600')  # default size of tkinter window
root.config(bg="blue")  # background color of the window


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


heading_lab = Label(root, text="Internet Speed Test", font=(
    'Times new roman', 30, 'bold'), bg='blue')
heading_lab.place(x=60, y=40, height=50, width=380)

up_speed_lab = Label(root, text="Download Speed",
                     font=('Times new roman', 30, 'bold', ))
up_speed_lab.place(x=40, y=130, height=50, width=380)

down_speed_result = Label(root, text="00", font=(
    'Times new roman', 30, 'bold', ))
down_speed_result.place(x=40, y=200, height=50, width=380)

up_speed_lab = Label(root, text="Upload Speed",
                     font=('Times new roman', 30, 'bold', ))
up_speed_lab.place(x=40, y=290, height=50, width=380)

up_speed_result = Label(root, text="00", font=(
    'Times new roman', 30, 'bold', ))
up_speed_result.place(x=40, y=360, height=50, width=380)

test_button = Button(root, text="Start Test", font=('Arial', 30, 'bold'),
                     relief='ridge', bg='black', fg='white', command=speedcheck)
test_button.place(x=40, y=460, height=50, width=380)

# mainloop at the end of the line which creates the tkinter window
root.mainloop()
