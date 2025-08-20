import os
import random
import string

class Product():
    price = 0.0
    name = ""
    id = 0
    dept = 0
    sku = 0
    def __init__(self, productData:str):
        data = productData.split(",")
        self.price = float( data[4] )
        self.name = str( data[1] )
        self.id = str( data[0] )
        self.dept = int( data[3] )
        self.sku = int( data[2] )

    def __eq__(self, other): #equal to
        if isinstance(other, self.__class__) :
            return self.price == other.price and self.name == other.name
        
        else :
            return False
        
    def __gt__(self, other): #greater than
        if isinstance(other, self.__class__) :
            return self.price > other.price
        
        else :
            return False
        
    def __lt__(self, other): #lesser than
        if isinstance(other, self.__class__) :
            return self.price < other.price
        
        else :
            return False
        
    def __le__(self, other): #lesser than or equal to
        if isinstance(other, self.__class__) :
            return self.price <= other.price
        
        else :
            return False   
             
    def __ge__(self, other): #greater than or equal to
        if isinstance(other, self.__class__) :
            return self.price >= other.price
        
        else :
            return False
        
    def __str__(self):
        return f"{self.id} - {self.name} - {self.price}"
        
    def addToCart(self):
        pass
class Customer():
    id = 0
    balance = 0

    def bill(self, value: float):
        pass

class Cart():
    def __init__(self, product: Product, customer: Customer, quantity = 1):
        isExists = os.path.exists("cart.json")

        if not isExists :
            file = open("cart.json", "x")
            file.close()
        
        file = open("cart.json", "+a")
        data = str(product)
        data += f" - {quantity} - {customer.id} \n"
        file.write(data)
        file.close()

    def count_items(self, customer:Customer) :
        id = customer.id
        isExists = os.path.exists("cart.json")

        if not isExists : 
            return 0
        
        file = open("cart.json", "r")
        allItems = file.readlines()
        customer_items = [item for item in allItems if id in item ]
        return len(customer_items)
    
    def checkout(self, customer:Customer):
        isExists = os.path.exists("cart.json")

        if not isExists : 
            return 0
        
        file = open("cart.json", "r")
        allItems = file.readlines()
        customer_items = [item for item in allItems if id in item ]

        return Order(customer_items)





class Order():
    def __init__(self, items):
        customer = ""
        isValid = True
        totalPrice = 0
        data = ""
        for item in items:
           itemed = item.split(" - ")
           customer = itemed.pop()
           quatity = int( itemed.pop() )
           price    = float( itemed.pop() )
           totalPrice  += quatity * price
           cust = customer.split("\n")[0]
           data += f"{itemed[0]} - "

           if cust != customer :
               isValid = False

           else: 
               customer = cust

        if not isValid :
            return False
        
        customer = Customer(customer)
        isBilled = customer.bill(totalPrice)

        if not isBilled :
            return False
        
        isExists = os.path.exists("order.txt")

        if not isExists : 
            file = open("order.txt", "x")
            file.close()
        
        file = open("order.txt", "a")
        order_id = random.choice(string.ascii_letters)

        for c in range(10) :
            order_id += random.choice(string.ascii_letters)

        data = f"@{order_id} {totalPrice} \n"
        file.write(data)
        file.close()
        return True
        

               

