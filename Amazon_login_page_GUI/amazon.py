from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Amazon")
root.geometry('400x500')



img = Image.open("amazlogo.png")
resize_img = img.resize((100,100))
img = ImageTk.PhotoImage(resize_img)
img_label = Label(root,image = img)
img_label.pack(pady=(10,10))

login_label = Label(root,text = "Login",fg ='Black')
login_label.pack(pady=(10,10),ipadx = 10, side= TOP, anchor="w")
login_label.config(font =('verdana',20))

email_label = Label(root,text = "Email or mobile phone number",fg = "Black",justify="left")
email_label.pack(pady = 5,anchor ='w',ipadx =10)
email_label.config(font =('verdana',10))
email_input = Entry(root,width = 50)
email_input.pack(ipady=6,pady = (1,15),ipadx = 10)


pass_label = Label(root,text = "Password                              Forgot password",fg = "Black",justify="left")
pass_label.pack(pady = 5,anchor ='w',ipadx =10)
pass_label.config(font =('verdana',10))
pass_label = Entry(root,width = 50)
pass_label.pack(ipady=6,pady = (1,15),ipadx = 10)

login_button = Button(root,text = "Login",fg = "black",bg = "#FCAE56",width = 45,height = 1)
login_button.pack(pady = (10,20))

Checkbutton1 = IntVar()
Button1 = Checkbutton(root, text="Keep me signed in",
                      variable=Checkbutton1,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10)
Button1.pack(anchor = "w",ipadx =23 )

new_label = Label(root,text = "New to amazon?")
new_label.pack(pady = (10,10))

create_button = Button(root,text = "Create your amazon account",width = 45,height = 10)
create_button.pack(pady = (10,10))
root.mainloop()