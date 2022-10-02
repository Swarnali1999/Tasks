nums = [22, 13, 10, 25, 16, 4, 0]

# .sort() vs sorted()
print("Sorted list: ",sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
print("Unsorted list: ",nums)           # [2, 3, 1, 5, 6, 4, 0]

# print(nums.sort())    # None
# print(nums)           # [0, 1, 2, 3, 4, 5, 6]

# .reverse() function reverse and updates the list
nums.reverse()
print("Reverse :" , nums)

# append(8) adds 8 at the end of the list
nums.append(55)
print("Append: ", nums)

# insert(3,8) will add 8 at 3 index
nums.insert(3,76)
print("Insert: ", nums)

# pop(3) will delete the element at index 3 and return its value
nums.pop(3)
print("Pop: ", nums)

# remove(25) will remove 25 from the last
nums.remove(25)
print("Remove: ", nums)