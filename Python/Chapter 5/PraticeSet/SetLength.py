s=set()
s.add(20)
s.add(20.0) # set takes 20.0 as 20 and does not take the repetative value.
s.add("20")

print(len(s))