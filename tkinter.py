from tkinter import *

def klikker():
    global a
    a+=1
    btn.config(text=a)
def klikker_(event):
    global a
    a-=1
    btn.config(text=a)
suurus=20
def minuoma(event):
    global suurus
    if event.num==5 or event.delta==-120:
        suurus+=1
    else:
        suurus-=1
    lvl.counfigure(width=suurus,text=suurus)

def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text) #num=int(text)

aken=Tk()
aken.title("Tkinter_app")
aken.geometry("800x600")
aken.iconbitmap("kart.ico")

btn=Button(aken,text="Valjuta siia",bg="pink",fg="green",font="Arial 20",height=5,width=20,activebackground="blue",command=lambda:klikker()) #lkn po btn -> klikker()
btn.bind("<Button-3>",klikker_)
btn.pack()

lbl=Label(aken,text="Numetus",borderwidth=5,relief="groove") #raised,sunken,flat,ridge,solid
lbl.bind("<MouseWheel>",minuoma)
lbl.pack()

ent=Entry(aken,width=20,borderwidth=5,font="Arial 20")
ent.bind("<Return>",text_to_lbl) #Enter
ent.pack()

img=PhotoImage(file="kart2",).subsample(2)
lbl_img=Label(aken, Image=img)
lbl_img.pack() #side=LEFT


aken.mainloop()
