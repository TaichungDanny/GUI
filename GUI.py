import tkinter as tk
# def click1():
#     global count
#     count += 1
#     labeltext.set('你按我' + str(count) + '次了')
#     textvar.set('按我')


def check_pd():
    if (pw.get() == '1234'):
        msg.set('歡迎登入!')
    else:
        msg.set('密碼錯誤! 請重新輸入:')


Danny = tk.Tk()
pw = tk.StringVar()
msg = tk.StringVar()
Danny.title('Danny')
Danny.geometry('450x150')

# count = 0
label1 = tk.Label(Danny, text='請輸入密碼:')
label1.pack()
entry = tk.Entry(Danny, textvariable=pw)
entry.pack()
button1 = tk.Button(Danny, text='登入', command=check_pd)
button1.pack()
labelmsg = tk.Label(Danny, textvariable=msg)
labelmsg.pack()
Danny.mainloop()