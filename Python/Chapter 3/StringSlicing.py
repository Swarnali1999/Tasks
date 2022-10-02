from msilib import init_database


name="India"
sentence="India is a great country."

# in string slicing, string starts from0 to (length-1).
# in string slicing, last index is not included in python.

sliced_string1=name[1:3]
sliced_string2=name[:4]
sliced_string3=name[0:]
sliced_string4=sentence[2:8]

print(sliced_string1)
print(sliced_string2)
print(sliced_string3)
print(sliced_string4)