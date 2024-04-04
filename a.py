from tkinter import *
cry = [
    ['ا','0','ب','پ','ت','ث','1'],
    ['ج','2','4','چ','ح','5','3'],
    ['خ','د','6','ذ','ر','7','ز'],
    ['ژ','س','ش','8','9','ص','ض'],
    ['ط','ظ','ع','غ','ف','ق','ک'],
    ['گ','ل','م','ن','و','ه','ي']
]

def root():
    root = Tk()
    root.geometry('500x500')
    root.resizable(False , False)
    root.config(bg = "black")
    pas = Entry(root,font = ('Times 14',30),fg = 'yellow',bd = 7,bg = 'green');pas.place(x = 0,y = 100,width = 370)
    def desc():
        v = pas.get()
        gh = scrypt.get()
        if len(v)%2 != 0:
            for i in range(len(gh)):scrypt.delete(0)
            scrypt.insert(END,'The statement is incorrect')
        else:
            es = []
            adder = 0
            dfg = int(len(v)/2)
            for i in range(len(gh)):scrypt.delete(0)
            for i in range(dfg):
                adder2 = ''
                for i in range(2):
                    adder2 += v[adder]
                    adder += 1
                es.append(adder2)

            try:
                for i in es:
                    for i in range(len(gh)):scrypt.delete(0)
                    for i in es:
                        a = int(i[1])
                        b = int(i[0])
                        if a == 7 and b == 7: scrypt.insert(END,' ')
                        else: scrypt.insert(END,cry[a-1][b-1])
            except ValueError:    
                for i in range(len(gh)):scrypt.delete(0)
                scrypt.insert(0,'Error')
            
                
    Button(root,text = 'click',font = ('Times 14',20),bg = 'yellow',command = desc).place(x = 400,y = 100)
    scrypt = Entry(root,font = ('Times 14',30),fg = 'yellow',bd = 7,bg = 'red');scrypt.place(x = 0,y = 300,width = 370)
    root.mainloop()

def password():
    pa = Tk()
    pa.geometry('500x200')
    pa.resizable(False , False)
    pa.config(bg = "red")
    pas = Entry(pa,font = ('Times 14',30),fg = 'yellow',bd = 7,bg = 'green',show = '*');pas.pack()
    def checked():
        a = pas.get()
        if a == "erfunfoolfuu":
            pa.destroy()
            root()
        else:
            for i in range(len(a)):pas.delete(0)
    Button(pa,text = 'click',bg = 'black',fg = 'white',font = ('Times 14',25),command = checked).pack()
    pa.mainloop()

password()



