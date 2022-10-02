a = {"name": "Ram",
	"from": "India",
	"marks": [92,98,96],
    "nested_dictionary":{"Tiger":55,"range":[3,4,5]},
    1:2}

# printing the keys of dictionary 'a'. 'dict_keys' is the bydefault typeof dictionary.
print(a.keys())    

# printing the key's values of dictionary 'a'. 'dict_keys' is the bydefault typeof dictionary.
print(a.values())

# printing the type of keys and values of dictionary 'a'.
print(type(a.keys()))
print(type(a.values()))

# converting the type of dictionary 'a'. 
# It is also known as typecasting.
print(list(a.keys()))
print(list(a.values()))

# updating the dictionary
uD={"u1":"done","u2":[3,'hi'],"nested_dictionary2":{"updating":"45","dd":"gg"}}
a.update(uD)
print("\nUpdated dictionary is: ",a)

# getting value with .get method.
print(a.get("marks")) # .get returns None if key is not present in the dictionary.
print(a["marks"]) # [] syntax throws error if key is not present in the dictionary.