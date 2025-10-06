# Print the Fibonacci series up to N terms. 
number=int(input("Enter the number: "))
a,b=0,1
for i in range(number):
    print(a, end=" ")
    a,b=b,a+b