# Find the Nth term in the Fibonacci series.
number = int(input("Enter the number: "))
a,b=0,1
for i in range(number-1):
    a,b=b,a+b
print(f"{number}th term of Fibonacci series is {a}")