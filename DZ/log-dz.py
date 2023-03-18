import tkinter as tk

def checkpass():
    pas="123123"
    value=entertxt.get()
    if value==pas:
        label2=tk.Label(window, text="Password correct").grid(row=40, column=10)
    else:
        label2=tk.Label(window, text="Password incorrect").grid(row=40, column=10)

def checkname():
    name="Roman"
    value1=entername.get()
    if value1==name:
        label3=tk.Label(window, text="Roman correct").grid(row=70, column=10)
    else:
        label3=tk.Label(window, text="name incorrect").grid(row=70, column=10)

def call_func():
    checkname()
    checkpass()

window = tk.Tk()
window.title("Check password")
window.geometry("140x120+10+10")

label1 = tk.Label(window, text="Enter Password").grid(row=0, column=10)
entertxt=tk.Entry(window)
entertxt.grid(row=20, column=10)
tk.Button(window, text="login", command=call_func).grid(row=80, column=10)
label2 = tk.Label(window, text="Enter login").grid(row=50, column=10)
entername=tk.Entry(window)
entername.grid(row=60, column=10)


window.mainloop()