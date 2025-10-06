number=int(input("Enter the number: "))
fact=1
if number==0 or number==1:
    print(f"factorial of {number} is {fact}")
else:
    for i in range (1,number+1):
        fact*=i
    print(f"factorial of {number} is {fact}")



