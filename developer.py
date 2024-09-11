from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman", 35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"College_images\top3.jpg")
        img_top=img_top.resize((1530,720))
       
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        
        img_top2=Image.open(r"College_images\d1.jpg")
        img_top2=img_top2.resize((200,200))
       
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)
        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=10,y=0,width=200,height=200)

        img_top3=Image.open(r"College_images\d2.jpg")
        img_top3=img_top3.resize((200,200))
       
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)
        f_lbl=Label(main_frame,image=self.photoimg_top3)
        f_lbl.place(x=280,y=0,width=200,height=200)
       
       
        img_top4=Image.open(r"College_images\d3.jpg")
        img_top4=img_top4.resize((200,200))
       
        self.photoimg_top4=ImageTk.PhotoImage(img_top4)
        f_lbl=Label(main_frame,image=self.photoimg_top4)
        f_lbl.place(x=10,y=300,width=200,height=200)

        img_top5=Image.open(r"College_images\d4.jpg")
        img_top5=img_top5.resize((200,200))
       
        self.photoimg_top5=ImageTk.PhotoImage(img_top5)
        f_lbl=Label(main_frame,image=self.photoimg_top5)
        f_lbl.place(x=280,y=300,width=200,height=200)

        #developer info
        dev_label=Label(main_frame,text="Hello, My name is Palak.",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=200)

        dev_label=Label(main_frame,text="I am a student.",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=240)

        dev_label1=Label(main_frame,text="Hello, My name is Prisha.",font=("times new roman",13,"bold"),bg="white")
        dev_label1.place(x=280,y=200)

        dev_label1=Label(main_frame,text="I am a student.",font=("times new roman",13,"bold"),bg="white")
        dev_label1.place(x=280,y=240)

        dev_label2=Label(main_frame,text="Hello, My name is Shubhanshi.",font=("times new roman",13,"bold"),bg="white")
        dev_label2.place(x=0,y=500)

        dev_label2=Label(main_frame,text="I am a student.",font=("times new roman",13,"bold"),bg="white")
        dev_label2.place(x=0,y=540)

        dev_label3=Label(main_frame,text="Hello, My name is Vandita.",font=("times new roman",13,"bold"),bg="white")
        dev_label3.place(x=280,y=500)

        dev_label3=Label(main_frame,text="I am a student.",font=("times new roman",13,"bold"),bg="white")
        dev_label3.place(x=280,y=540)
       
if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
    