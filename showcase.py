import os
path = os.path.join(os.getcwd(), "products")
path = os.path.join(path, "products.csv")
with open(path, "r") as file :
    header = file.readline().split(",")
    body = file.readlines()
    body = body[:10]
    products = []

    for product in body :
        product = product.split(",")
        products.append( dict(zip([head.split("\n")[0] for head in header], product)) )
        

    for product in products :
        print( f"id - {product['product_id']}", f"name - {product['product_name']}", f"price  - {product['price']}")
