thisList=["apple","orangle","grapes"]
#list allows multiple data types
list2=[1,"apple",False,3.5]

#length of list will print numbers of items in list
print(len(thisList))

#constructor of list
consList=list(("apple","bnanna","apricort"))

#accessing list items
print(list2[1])
newList=list2[1:]

#change list items
list2[1]="banana"

list2[1:]=["orange",True,3.0]

thisList[1:]="orange"
thisList.insert(2,"watermelon")