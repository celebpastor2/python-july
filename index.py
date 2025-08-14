#from mailbox import BabylMessage

"""
This is a Comment in Python - a multi line comment
"""

text = """Version of nginx for Windows uses the native Win32 API (not the Cygwin emulation layer). Only the select() and poll() (1.15.9) connection processing methods are currently used, so high performance and scalability should not be expected. Due to this and some other known issues version of nginx for Windows is considered to be a beta version. At this  , it provides almost the same functionality as a UNIX version of nginx except for XSLT filter, image filter, GeoIP module, and embedded Perl language."""
#count the "the" in the above text
#count the "a" in the text
#count the "of" and "are" and specify the difference
#a loop is a code block that will need to run over and over again at a specific interval
#an iteration is running a loop over contents of a sequence
#any data type that we can a loop over is call iterable
dicct = {
    "key1"  : "value2",
    "key2"  : "value3"
}

#adding value
dicct.update({"key3": "value3"})
dicct["key5"] = "value5"

#x means create mode
#r means read mode
#a means the append mode
#w means write mode
#b means write in binary mode

file = open("products.csv","+a")
file2 = open("products.csv", "r")
header = file2.readline()


body = list( file2.readlines() )
body = body[:10]
line = len(body)
line += 1
newcsv = f"{line},New Product,6,34,34.96"
file.write(f"\n{newcsv}")
file.close()
