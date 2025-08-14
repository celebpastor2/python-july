import os
import pathlib as Path

path  = os.path.join( "products", "products.csv")
os.chdir('..')
file    = open(path, "r")
head    = file.readline()
file.close()

print(head)
exit()


#gets the current working directory
#print(os.getcwd())

#change the current working directory
os.chdir('..')
print(os.getcwd())
liist = os.listdir() 

for file in liist :
    if os.path.exists(file) :
        print("it is a file")
    
    elif os.path.isdir(file) :
        print("it is a directory")

    else :
        print("is not a file or a directory")

#creates a directory
os.mkdir("nameOfDir")