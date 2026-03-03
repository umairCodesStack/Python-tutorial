thisList=["apple","orangle","grapes"]
#list allows multiple data types
list2=[1,"apple",False,3.5]

#length of list will print numbers of items in list
print(len(thisList))

#CONSTRUCTOR OF LIST
consList=list(("apple","bnanna","apricort"))

#ACCESS LIST ITEMS
print(list2[1])
newList=list2[1:]

#CHANGE LIST ITEMS
list2[1]="banana"

list2[1:]=["orange",True,3.0]

thisList[1:]="orange"
thisList.insert(2,"watermelon")

#ADD ITEMS TO LIST
thisList.append("grapes")

topical=["pineapple","almond","dates"]
thisList.extend(topical)

print(thisList)
#you can extend with tuples and other itmes like dictionary
tupleItems=("abc","dec")
thisList.extend(tupleItems)
print(thisList)

#REMOVE ITEMS FROM LIST

#remove specific item
thisList.remove("abc")
#remove at specific index
thisList.pop(1)
#remove at last index
thisList.pop()
print(thisList)
del thisList[2]
print(thisList)

#delete entire list
del topical

#clear this list
thisList.clear()
print(thisList)

fruits=["apple","orangle","grapes","apple","banana"]

#LOOPING THROUGH LIST

#looping all items
for x in fruits:
    print(x)

#looping with index
for index in range(len(fruits)):
    print(index,":",fruits[index])

#while loop
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1


#short-hand of loop
print("Printing using short-hand")
[print(x) for x in fruits]



#LIST COMPREHENSION

#extracting fruits having a in their name
newList=[]
for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList) 

#this all can be done in one line
newList=[x for x in fruits if  x!="apple"]

copyList=[x for x in fruits]

print(newList)
print(copyList)

upperCase=[x.upper() for x in fruits]
print(upperCase)

sameVal=["hello" for x in fruits]
print(sameVal)
#ITERABLE

nums=[x for x in range(10)]
odds=[x for x in range(20) if x%2!=0]

print(nums)
print(odds)

#replace grapes with orange
newlist = [x if x != "grapes" else "orange" for x in fruits]
print(newlist)

#SORT LIST

#sorting is alphanumeric
thisList.sort()
print(fruits)

nums=[1,3,4,5,7,2,0]
nums.sort()
print(nums)


#case-insestive sort
mixFruits=["Pappay","Pomigrante"]
mixFruits.extend(thisList)
mixFruits.sort(key= str.lower())
print(mixFruits)

#descenting order sort
nums.sort(reverse=True)

#custom sort 
#sort which number is more close to 50
def myfunc(n):
  return abs(n - 50)

bigNums=[100, 50, 65, 82, 23]
bigNums.sort(key=myfunc)

#COPY LIST
num3=bigNums.copy()
#or 
num3=bigNums[:]
#or
num3=list(bigNums)


#JOIN LIST
num4=nums+bigNums
#or
num5=[4,5,6,8]
num4.extend(num5)
#or
for x in num5:
    num4.append(x)