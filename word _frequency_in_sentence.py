# Count the frequency of each word in a sentence. 
string=input("Enter the string: ").split()

dictionary={}
for i in string:
    if i not in dictionary:
        dictionary[i]=1
    else:
        dictionary[i]+=1
print(dictionary)