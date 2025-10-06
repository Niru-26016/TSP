# Remove duplicate characters from a string. 
string=input("Enter the string: ")
string2=""
for i in string:
    if i not in string2:
        string2+=i
    
print(f"{string2}")