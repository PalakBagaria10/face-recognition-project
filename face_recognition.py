from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="FACE RECOGNIZER",font=("times new roman", 35,"bold"),bg="white",fg="GREEN")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"College_images\top9.jpeg")
        img_top=img_top.resize((650,700))
       
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        img_bottom=Image.open(r"College_images\top8.jpeg")
        img_bottom=img_bottom.resize((950,700))
       
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)


        b2=Button(f_lbl,text="Face Detector",cursor="hand2",command=self.face_recog,font=("times new roman", 15,"bold"),bg="darkgreen",fg="white")
        b2.place(x=365,y=620,width=200,height=40)

    #attendance
    def mark_attendance(self,n,r,p,d):
        with open("palak.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((p not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{p},{r},{n},{d},{dtString},{d1},Present")

        ##face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host='localhost',user='root', password='PVS@pvs123', database='face_recognizer')
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                if n is not None:
                    if isinstance(n,tuple):
                        n="+".join(n)
                    else:
                        n=str(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                # r="+".join(r)

                if r is not None:
                    if isinstance(r,tuple):
                        r="+".join(r)
                    else:
                        r=str(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                # d="+".join(d)
                if d is not None:
                    if isinstance(d,tuple):
                        d="+".join(d)
                    else:
                        d=str(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                p=my_cursor.fetchone()
                # p="+".join(p)
                if p is not None:
                    if isinstance(p,tuple):
                        p="+".join(p)
                    else:
                        p=str(p)

                if confidence>70:
                    cv2.putText(img,f"Id:{p}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(p,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        def recognise(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\Palak Bagaria\Desktop\Face recognition project\classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognise(img,clf,faceCascade) 
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognizer(root)
    root.mainloop()
    