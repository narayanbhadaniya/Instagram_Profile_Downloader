from tkinter import *
from tkinter.filedialog import asksaveasfile,askopenfile
import tkinter as tk
from PIL import Image,ImageTk
import instaloader

window=Tk()
window.title("Insta Profile Downloader")
window.config(bg="Skyblue")

sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
w=sw-800
h=sh-200
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))

def igprofile():
    iguser=str(E1.get())
    ig=instaloader.Instaloader()
    ig.download_profile(iguser,profile_pic_only=True)

#Heading
H=Label(window,text="Insta Profile Downloader",width=0,height=0,font=("comic sans ms",20,"bold underline"))
H.config(bg="white",fg="black")
H.place(x=130,y=10)

#label
l1=Label(window,text="Enter IG  Username",width=0,height=0,font=("comic sans ms",12,"bold"))
l1.config(bg="white",fg="black")
l1.place(x=120,y=250)
var1=StringVar()
E1=Entry(window,textvariable=var1,width=10,font=("comic sans ms",12,"bold"))
E1.config(bg="white",fg="black")
E1.place(x=350,y=250)
B1=Button(window,text="Download Profile",command=igprofile)
B1.place(x=240,y=350)

#transparent bg
window.wm_attributes("-transparentcolor","skyblue")
window.mainloop()
    
