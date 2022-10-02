from dataclasses import replace


string="I am learning python"

a=len(string)
b=string.endswith("on")
c=string.count("n")
d=string.capitalize()
e=string.find("am") #if a word repeats, it tells only about the first occurence.
f=string.replace("I am","You are")

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)