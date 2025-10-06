#  Prime number check.
number=int(input("Enter the number: "))
prime=True
for i in range(2,number//2+1):
    if number%i==0:
        prime=False
if prime:
    print(f"{number} is Prime")
else:
    print(f"{number} is not prime")
