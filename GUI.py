import tkinter as tk
Danny = tk.Tk()
Danny.title('Danny')
label1 = tk.Label(Danny, text='標籤', fg='blue', bg='orange', font=('新細明體', 12), padx=20, pady=10)
label1.pack()
Danny.mainloop()