# Dictionary is a collection of key-value pairs.
# It is unordered, mutable, indexed and cannot contain duplicate keys

a = {"name": "Ram",
	"from": "India",
	"marks": [92,98,96],
    "nested_dictionary":{"Tiger":55,"range":[3,4,5]}}

# printing all items from dictionary    
print(a.items())    

# printing single item from dictionary
print(a['name'])

# printing particular item from nested_dictionary which is inside dictionary named a.
print(a['nested_dictionary']["Tiger"])

# Dictionary is mutable. So, we can update the key values here.
a['marks']=[4,6,2]
print(a['marks'])