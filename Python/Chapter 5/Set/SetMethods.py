b=set()

# adding data in an empty set. 
b.add(3)
b.add(4)
b.add(9)
b.add(3) # will not print repetative elements. Only one 3 will get printed. 
b.add(3)
# items can also be added by follwing method.
# b = {1,2}

# we can not add list in set as list is not hasable which means in list we can change data later on.
# b.add([2,3,5])

# we can add tuple in set though.
b.add((2,3,5))

# we can not add dictionary in set as dictionary is not hasable which means in dictionary we can change data/elements later on.
# b.add({"dictionary":5})

print(b)

# printing the length of set
print(len(b))

# removing item from set
b.remove(3)
# b.remove(78) # throws an error as 78 is not present in the set
print("After removing: ", b)

# poping item from set.
# b.pop()
# print("After popping: ", b)

# empting the set
# b.clear()
# print("After clear: ", b)

# union of set
b1=b.union({4,78,9})
print("After union: ", b1)

# intersection of set
b2=b.intersection({4})
print("After intersection: ",b2)