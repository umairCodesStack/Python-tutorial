#SETS 
#sets only have unique items ignore duplicate items
#sets items are unchangeable but you can add / remove from set
#sets are not ordered
thisSet={"keyboard","mouse","charger"}

#ACCESSING SET
for x in thisSet:
    print(x)

#ADDING ITEMS TO SET
thisSet.add("Mobile")
set2={"Extension","LED"}
thisSet.update(set2)
print(thisSet)

#adding list to set
mylist=["fruits","snacks"]
thisSet.update(mylist)
print(thisSet)

#REMOVING ITEMS FORM SET
thisSet.remove("fruits") #will raise error if not exist
thisSet.discard("fruits")
thisSet.pop() #remove random item

#UNION OF SETS
set1={"LED","charger","razor"}
set3=set1.union(set2)
#or 
set3=set1|set2
set3=set1.union(set2,thisSet)
print("SET 3",set3)

#INTERSECTION OF SETS
set3=set1.intersection(set2)
set3=set1 & set2
print(set3)
#intersection on original set
set1.intersection_update(set2)
print(set1)

#DIFFERENCE OF SETS
set3=thisSet.difference(set2)
set3=thisSet-set2
print(set3)
thisSet.difference_update(set1)
print(thisSet)

#FROZEN SET
y=frozenset(thisSet)
print(y)
thisSet.clear()
del thisSet

