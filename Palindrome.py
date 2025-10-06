number=int(input("Enter the number: "))

if(int(str(number)[::-1])==number):
    print(f"{number} is Palindrome")
else:
    print(f"{number} is not Palindrome")
