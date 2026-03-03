#TUPLES is one of four data types of python i.e tuples,list,dictionary, and set

#Tuples are unchangeable and allow duplicate
newTuple=("apple","orange","banana")

#ACCESSING TUPLE
print(newTuple[0])
print(newTuple[0:])

#UPDATE TUPLE
#to make changes(add,remove,update) in tuple convert this into list

#change value
y=list(newTuple)
y[0]="grapes"
newTuple=tuple(y)
print(newTuple)

#add value
y=list(newTuple)
y.append("kiwi")
newTuple=tuple(y)
print(newTuple)

#adding tuple to a tuple
newFruit=("papaya",)
newTuple+=newFruit
print(newTuple)

#remove item
y=list(newTuple)
y.remove("kiwi")
newTuple=tuple(y)
print(newTuple)

#delete tuple
del newTuple



#UNPACKING TUPLE
items=("keyboard","charger","food")
(keyboard,charger,food)=items
fruits=("apple","orange","banana","papaya","grapes","kiwi","watermelon","apple")
(apple,orange,banana,*red)=fruits
print(red)
(x,*red,z)=fruits
print(x)
print(red)
print(z)

#LOOPING THROUGH TUPLES
for x in fruits:
    print(x)

#or 
for index in range(len(fruits)):
    print(fruits[index])

#JOINING TUPLES
tuple1=[0,1,2,3]
tuple2=[4,5,6]
tuple3=tuple1+tuple2

tuple4=tuple3*2

x=fruits.count("apple")
print(x)
position=fruits.index("apple")
print(position)