from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os

counter = 1
def rotate_img():
    global counter
    img_label.config(image = img_array[counter%len(img_array)])
    counter = counter+1


root = Tk()
root.geometry('500x500')
root.configure(background="#FCAE56")
root.title("Image Viewer")


view_label = Label(root,text = "Image Viewer App",fg = 'white',bg = "#FCAE56" )
view_label.pack(pady = (10,10))
view_label.config(font=('verdana', 24))

files = os.listdir('realme_/realme_images')
img_array = []
for file in files:
    img = Image.open(os.path.join('realme_/realme_images', file))
    resize_img = img.resize((300,300))
    img_array.append(ImageTk.PhotoImage(resize_img))

img_label = Label(root,image = img_array[0])
img_label.pack(pady = (15,10))

next_button = Button(root,text = "Next",bg = 'white',fg = 'Black',width = 20,height = 2,command= rotate_img)
next_button.pack(pady = (10,10))

root.mainloop()