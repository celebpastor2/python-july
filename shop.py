import tkinter
from tkinter import ttk, messagebox, Menu, Menubutton
from PIL import Image, ImageTk
import json
import requests
import io
import os
import shutil


file = open("products.json", "r", encoding="utf8")
text = file.read()
file.close()
products = json.loads(text) #list



root = tkinter.Tk()
root.geometry("700x500")
root.title("Shop Mall") 
root.iconbitmap("icon.ico")
root.configure(bg="#aaa")
style = ttk.Style()
style.configure("Black.TLabel", background="black", foreground="white")
style.configure("Red.TLabel", background="red", foreground="white")
style.configure("White.TLabel", background="white", foreground="black")


def buy_product(but, id):
    id = int( id )
    product = products[id - 1]
    frame = tkinter.Toplevel(root)
    if product :
        frame.title(product['title']) 
        image_frame = ttk.Frame(frame)     
        description_frame = ttk.Frame(frame)
        image_frame.grid(column=0, row=0)     
        description_frame.grid(column=1, row=0)     
    
    else :
        frame.title("Product Not Found")

    frame.geometry("500x700")
    frame.transient(root)

images = []
def process_product(product, z) :
    frame = ttk.Frame(root, padding=10, style="White.TLabel")   

    curdir = os.getcwd()
    imgdir = os.path.join(curdir, "images")

    if not os.path.exists(imgdir) :
        os.mkdir(imgdir)
    
    img_arr = str(product['image']).split("/")
    imag_name = img_arr.pop()
    imag_path = os.path.join(imgdir, imag_name)

    if not os.path.exists(imag_path):
        response = requests.get(product['image'], stream=True)
        with open(imag_path, "wb") as file :
            for chunk in response.iter_content(chunk_size=4048) :
                file.write(chunk)

    print(imag_name)
    images.append( Image.open(imag_path) )
    images[z] = images[z].resize((150,150))
    images[z] = ImageTk.PhotoImage(images[z])    
    label = ttk.Label(frame, image=images[z])
    product_name = ttk.Label(frame, text=product['title'][:20])
    price_frame = ttk.Frame(frame)
    price = ttk.Label(price_frame, text=f"${product['price']}")
    category = ttk.Label(price_frame, text=f"{product['category']}")
    price.grid(column=1, row=0) 
    category.grid(column=0, row=0)
    button = ttk.Button(frame, text="View More", command= lambda: buy_product(button, product['id']))
    label.pack()
    product_name.pack()
    price_frame.pack()
    button.pack()
    x = z % 4
    y = z // 4
    frame.grid(column=x, row=y)
z = 0
for product in products :
    process_product(product, z)
    z+=1
root.mainloop()

"""
Create a product page using the TopLevel element created in this code.
Use grid and pack method to design the Toplevel element
"""