word = input("Please enter a word: ")
length = len(word)
print(f"First character:  {word[0:1:1]} ")
print(f"Last character: {word[length-1:length:1]}")
print(f"First four characters: {word[0:4:1]} ")
print(f"Every other character: {word[0::2]}")
print(f"Backwards: {word[::-1]}")


