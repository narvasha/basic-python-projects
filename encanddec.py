from tkinter import*
from tkinter import messagebox
import base64
import os
def decrypt():
    print("")
    
def encrypt():
     password=code.get()
     
     if password : 
         Screen1=Toplevel(Screen)
         Screen1.title("encryption")
         Screen1.geometry("400x200")
         Screen1.configure(bg="#ed3833")
         
         Message=text1.get(1.0,END)
         encode_message=Message.encode("ascii")
         base64_bytes=base64.b64decode(encode_message)
         encrypt=base64_bytes.decode("ascii")
         
         Label(Screen1,text="ENCRYPT",font="arial",fg="white",bg="ed3833").place(x=10,y=0)
         text2=Text(Screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
         text2.place(x=10,y=40,width=380,height=150)
         
         
         
    
from turtle import Screen
def main_screen():
    screen=Tk()
    screen.geometry("375x398")
    
    #icon
image_icon = PhotoImage(file="C:\Users\ASUS\Desktop\python\encanddec.py")

Screen.iconphoto(False,image_icon)
Screen.title("PctApp")

def reset():
    code.set("")
    text1.delete(1.0,END)
    
            
    
Label(text= "Enter text for encryption and decryption",fg="black",font=("calbri",13) ).place(x=10,y=10)
text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
text1.place(x=10,y=50,width=355,height=100)
Label(text="ENTER secreat key for encryption and decryption",fg="black",font=("calbri",13) ).place(x=10,y=10)
   
code=StringVar()
Entry(textvariable=code,width=19,bd=0,font=("arial,25"),show="*").place(x=10,y=200)
  
Button(text="Encrypt",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt ).place(x=10,y=250)
Button(text="decrypt",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
Button(text="Reset",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)

Screen.mainloop()
   
main_screen()
        