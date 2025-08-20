import os
path = os.path.join(os.getcwd(), "products")
path = os.path.join(path, "products.csv")

file = open(path, "a")
reader = open(path, "r")
reader.readline()
number = len( reader.readlines() ) 

print("Welcome to Shabby Shop")
print("++++++++++++++++++++++++++++++++++++++")
print("                                        ")
print("Please follow the prompt to add product to your database")
product_name = input("Enter the name of your product: ")
product_price = float( input("Enter the price of your product: "))
dept = int( input("What department is your product? ") )
file.write(f"\n{number+1},{product_name},{4},{dept},{product_price}")
