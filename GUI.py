import tkinter as tk
def click1():
    textvar.set('我被按過了')
Danny = tk.Tk()
Danny.title('Danny')
label1 = tk.Label(Danny, text='標籤', fg='blue', bg='orange', font=('新細明體', 12), padx=20, pady=10)
label1.pack()
textvar = tk.StringVar()
button1 = tk.Button(Danny, textvariable=textvar, command=click1)
textvar.set('按鈕')
button1.pack()
Danny.mainloop()