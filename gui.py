import tkinter
from tkinter import ttk, messagebox, Menu, Menubutton
from PIL import Image, ImageTk
import json
import requests
import io
import os


file = open("products.json", "r")
text = file.read()
file.close()
products_data = json.loads(text) #list
products = products_data['products']

"""
{
    "key":"value"
}

[
    "data1", "data2", {
    "key":"value"
}
]
"""

root = tkinter.Tk()
root.geometry("700x500")
root.title("Shop Mall") 
root.iconbitmap("icon.ico")
root.configure(bg="#000")
style = ttk.Style()
style.configure("Black.TLabel", background="black", foreground="white")
style.configure("Red.TLabel", background="red", foreground="white")
style.configure("White.TLabel", background="white", foreground="black")


def buy_product(but, id):
    but.config(text=id)
    pass

x = 0
y = 0
z = 0
for product in products :
    frame = ttk.Frame(root, padding=10, style="White.TLabel")   

    curdir = os.getcwd()
    imgdir = os.path.join(curdir, "images")

    if not os.path.exists(imgdir) :
        os.mkdir(imgdir)
    
    img_arr = str(product['thumbnail']).split("/")
    imag_name = img_arr.pop()
    imag_name = img_arr.pop()
    imag_name += ".webp"
    imag_path = os.path.join(imgdir, imag_name)

    if not os.path.exists(imag_path) :
        response = requests.get(product['thumbnail'], stream=True)
        with open(imag_path, "wb") as file :
            for chunk in response.iter_content(chunk_size=8096) :
                file.write(chunk)

    image = Image.open(imag_path)
    image = image.resize((50,50))
    image = ImageTk.PhotoImage(image=image)    
    label = ttk.Label(frame, image=image)
    product_name = ttk.Label(frame, text=product['title'])
    price_frame = ttk.Frame(frame)
    price = ttk.Label(price_frame, text=f"${product['price']}")
    category = ttk.Label(price_frame, text=f"{product['category']}")
    price.grid(column=0, row=0) 
    category.grid(column=1, row=0)
    button = ttk.Button(frame, text="View More", command= lambda: buy_product(button, product['id']))
    label.pack()
    product_name.pack()
    price_frame.pack()
    button.pack()
    x = z % 4
    y = z // 4
    frame.grid(column=x, row=y)
    z+=1
root.mainloop()