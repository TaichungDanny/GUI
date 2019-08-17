import tkinter as tk
def click1():
    global count
    count += 1
    labeltext.set('你按我' + str(count) + '次了')
    textvar.set('按我')



Danny = tk.Tk()
labeltext = tk.StringVar()
Danny.title('Danny')
Danny.geometry('450x150')
labeltext.set('歡迎光臨')
count = 0
label1 = tk.Label(Danny, fg='blue', font=('新細明體', 12), padx=20, pady=10, textvariable=labeltext)
label1.pack()
textvar = tk.StringVar()
button1 = tk.Button(Danny, textvariable=textvar, command=click1)
textvar.set('按我')
button1.pack()
Danny.mainloop()