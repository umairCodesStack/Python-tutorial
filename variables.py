#many values to many variables
x,y,z="ali","ahmad",5

#OR 
a=b=c="orange"

#unpacking a collection
fruites=["apple","grapes","oranges"]
q,w,e=fruites
print(q,w,e)

def myfunction():
    global myvar
    myvar="oxi"
    print("Printing varaible",myvar)


#now myvar's scope is global

