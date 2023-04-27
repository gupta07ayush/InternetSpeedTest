from tkinter import *
import speedtest

sp = Tk()
sp.title("Internet Speed Meter")
sp.geometry('500x700')
sp.config(bg="blue")

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10**6),2)) + " Mbps"
    up = str(round(sp.upload() / (10**6),2)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)
    result = sp.results.share()
    print(result)
    r = sp.results.dict()
    print(r)
   



lab = Label(sp, text="Internet Speed Test", font=('Times new roman', 30, 'bold'), bg='blue' )
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=('Times new roman', 30, 'bold', ))
lab.place(x=40, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=('Times new roman', 30, 'bold', ))
lab_down.place(x=40, y=200, height=50, width=380)

lab = Label(sp, text="Upload Speed", font=('Times new roman', 30, 'bold', ))
lab.place(x=40, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=('Times new roman', 30, 'bold', ))
lab_up.place(x=40, y=360, height=50, width=380)

button = Button(sp, text = "Start Test", font=('Arial', 30, 'bold'), relief='ridge', bg='red', fg='white', command=speedcheck)
button.place(x=40, y=460, height=50, width=380)


sp.mainloop()