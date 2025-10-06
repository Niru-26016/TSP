# Find the second largest number from space-separated input. 
numbers=list(map(int, input("Enter the numbers:").split()))
print(f"Second largest number: {sorted(numbers)[-2]}")