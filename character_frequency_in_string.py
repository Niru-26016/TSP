# Count the frequency of each character in a string. 
string=input("Enter the string: ")
dictionary={}
for i in string:
    if i not in dictionary:
        dictionary[i]=1
    else:
        dictionary[i]+=1
print("character\tcount")
for i in dictionary:
    print(f"{i}\t\t{dictionary[i]}")