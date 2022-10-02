dictionary1 ={
    "dheere":"slowly",
    "tez":"fast",
    "sundar":"beautiful"
}

b1=input("Enter your choice from 'dheere','tez','sundar': ")
print("The meaning of the word is: ",dictionary1[b1])
print("The meaning of the word is: ",dictionary1.get(b1))#This line will not throw error in case the searched word is not present.