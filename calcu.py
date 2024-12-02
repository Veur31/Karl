from tkinter import *
from functools import partial
win = Tk()
win.configure(bg="#A6AEBF")
btns = ["**", "//", "%", "C","7", "8", "9", "+","4", "5", '6', "-","1", "2", "3", "*",".", "0", "=", "/"]
rownum,columnnum= 1,0   
def solve(answer):
    if answer == "=":
        ans =str(eval(res.cget("text")))
        res.config(text=ans)
    elif answer == "C":
        res.config(text="")
    else:
        res.config(text=res.cget("text")+answer)
res = Label(win, text="", fg="Black", font=("MRK Maston Pro",20), bg= "#A6AEBF",width=18, relief="sunken")
res.grid(row= 0, column=columnnum, columnspan=4, sticky="ew")
res.grid_columnconfigure(0,weight=1)
for i in range(len(btns)):
    Button(win, width=4, height=1, text=btns[i], font=("MRK Maston Pro",22),relief="sunken", bg="#C5D3E8", command=partial(solve, btns[i])).grid(row= rownum+2, column=columnnum)
    columnnum += 1
    if columnnum ==4:
        rownum += 1
        columnnum = 0
win.geometry("312x327+600+250")
win.mainloop()