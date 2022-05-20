nput=input("Input: ")
print("Output: ", end="")
for letters in nput:
    if not letters.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(letters, end="")
print()