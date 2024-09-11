from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman", 35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"College_images\help.jpeg")
        img_top=img_top.resize((1530,720))
       
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(f_lbl,text="Email:palakbagaria10@gmail.com",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=550,y=300)

        dev_label=Label(f_lbl,text="This is a Face Recognition Attendance System Software in which students details are sored and attendance are marked accordingly.\n While using this software if you have any query contact us on the given Email. Thank you! ",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=300,y=220)

if __name__ =="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
    