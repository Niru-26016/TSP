#  Count frequency of numbers (from list input).
numbers=list(map(int, input("Enter the numbers: ").split()))
dictionary={}
for i in numbers:
    if i not in dictionary:
        dictionary[i]=1
    else:
        dictionary[i]+=1
print("number count")
for i in dictionary:
    print(f"{i}\t{dictionary[i]}")