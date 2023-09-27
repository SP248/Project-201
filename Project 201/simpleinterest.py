from tkinter import *
window=Tk()

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i,2)


window.title('Simple Interest')
window.geometry("380x400")
window.configure(bg='lightcyan')
       

app_label=Label(window, text="Simple Interest", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principle_label=Label(window, text="", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
principle_label.place(x=20, y=90)
principle=Entry(window, text="", bd=2, width=22)
principle.place(x=150, y=92)

Showlabel = Label(result_frame,text = "Your result will be displayed here", bg = "grey", font = ("Calibri", 12), width = 55)
Showlabel.place(x=20,y=20)
Showlabel.pack()

rate_label = Label(window,text = "Rate Of Interest", fg = "black", bg = "lightcyan", font = ("Calibri", 12))
rate_label.place(x=20, y=140)
rate = Entry(window, text = "Rate of Interest", bd = 2, width = 15)
rate.place(x=150, y=142)

time_label = Label(window, text = "Time", fg = "black", bg = "lightcyan", font = ("Calibri", 12))
time_label.place(x=20, y=185)
time = Entry(window, text = "Time", bd = 2, width = 15)
time.place(x=150, y=187)

calculate_button = Button(window,text = "Calculate", fg = "black", bg = "cyan", bd = 4, command=calculate_interest)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12))
result_frame.pack(padx=30, pady=50)
result_frame.place(x=20,y=300)


Showlabel.destroy()

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()
window.mainloop()








