# Read a lowercase word and print the vowel count and consonant count separated by a space.
string=input("Enter the string: ").lower()
vowels=["a","e","i","o","u"]
vowels_count=0
consonant_count=0
for i in string:
    if i in vowels:
        vowels_count+=1
    else:
        consonant_count+=1

print(f"vowels count: {vowels_count}\nconsonant count: {consonant_count}")
