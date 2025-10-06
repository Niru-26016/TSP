# Read space-separated integers and find their average. 
numbers=list(map(int, input("Enter the numbers: ").split()))
average = sum(numbers)/len(numbers)
print(f"average: {average}")