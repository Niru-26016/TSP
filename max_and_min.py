# Find the minimum and maximum numbers from space-separated input. 
numbers=list(map(int, input("Enter the numbers: ").split()))
print(f"maximum: {max(numbers)}\nminimum: {min(numbers)}")