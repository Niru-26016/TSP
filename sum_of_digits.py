number=int(input("Enter the number: "))
num=number
sum=0
while num>0:
    remainder=num%10
    sum+=remainder
    num//=10
print(f"sum of digits of {number} is {sum}")