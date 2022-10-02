# empty set will not return the type as <class 'set'>.
# it will return <class 'dict'>.
a={}
print(type(a))

# proper way to create an empty set.
b=set()
print(type(b))