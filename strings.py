print("It's cold outside")

print('He is called "Johny"')

#multi-line strings
str="""
Line 01
Line 02
Line 03
"""
x="Hello there"
#print(x[0])

# for i in x:
#     print(i)

#print(len(x))

txt="Pyhton is free"
#print("free" in txt)

if "free" in txt:
    print("free is present in txt")


#Slicing of Strings
print("Slice from index 2 to 5",txt[2:5])
print("Slice from start to 2",txt[:2])
print("Slice from 5 to end",txt[5:])
print("Negative indexing",x[-5:-1])



#String Modifications
print("Upper case", x.upper())
b="  Hello    "
print("Remove whitespaces from start and end",b.strip())
b="Wellcome,to jungle"
print(b.split(','))
print(b.replace('W','J'))

#Concate String
a="Hello"
b="World"
print(a+" "+b)

#String format
price=123
txt=f"Price of product is {price}"
print(txt)