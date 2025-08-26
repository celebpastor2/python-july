import tkinter
from tkinter import ttk, messagebox, Menu, Menubutton
from PIL import Image, ImageTk


root = tkinter.Tk()
root.geometry("700x500")
root.title("Shop Mall") 
root.iconbitmap("icon.ico")
root.configure(bg="#000")
style = ttk.Style()
style.configure("Black.TLabel", background="black", foreground="white")
style.configure("Red.TLabel", background="red", foreground="white")
image = Image.open("icon.png")
image = image.resize((50, 50))
imageTkk = ImageTk.PhotoImage(image=image)

imageFrame = ttk.Frame(root, padding=10)
imageLabel = ttk.Label(imageFrame, image=imageTkk, width=100)

def click_now():
    imageButton.config(text="clicked")

imageButton = ttk.Button(imageFrame, text="click me", command=click_now)

imageFrame2 = ttk.Frame(root, padding=10)
imageLabel2 = ttk.Label(imageFrame2, image=imageTkk, width=100)

def click_now():
    imageButton2.config(text="clicked")

imageButton2 = ttk.Button(imageFrame2, text="click me", command=click_now)


imageFrame.grid(row=0, column=0)
imageLabel.pack()
imageButton.pack()

imageFrame2.grid(row=0, column=1)
imageLabel2.pack()
imageButton2.pack()


root.mainloop()