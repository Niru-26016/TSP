# Find the power of two numbers (space-separated input). 

numbers=list(map(int, input("Enter the numbers: ").split()))
print(f"{numbers[0]} to the power of {numbers[1]} is {numbers[0]**numbers[1]}" )