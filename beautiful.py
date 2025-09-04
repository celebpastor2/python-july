import requests
from bs4 import BeautifulSoup
import os
import random
import string

def generateTxt(limit = 10) :
    text = string.ascii_uppercase + string.ascii_lowercase + string.digits
    let = ""
    for t in range(limit) :
        let += random.choice(text)

    return let



url = "https://jumia.com.ng"
response = requests.get(url=url)
html = response.text
soup    = BeautifulSoup(html, "html.parser")

title = soup.select("div.-me-start")

for div in title :
    image = div.find("img")
    img = image.attrs['data-src']

    if not "https" in img :
        #print("not found")
        continue
    
    print("found")
    mydir = os.getcwd()
    image_dir = os.path.join(mydir, "jumia_images")

    if not os.path.exists(image_dir) :
        os.mkdir(image_dir)

    imag_name =  img.split("/").pop().split("?")[0] 
    another = img.split("/").pop().split("?")[1]
    ext = imag_name.split(".")[1] 
    imag_name = imag_name.split(".")[0] 
    imag_name += another or "" + "." + ext

    
    imag_path = os.path.join(image_dir, imag_name)

    response = requests.get(img, stream=True)
    with open(imag_path, "wb") as file :
        for chunk in response.iter_content(chunk_size=4048) :
            file.write(chunk)


