
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Words:", words)
print("Longest word:", max(words, key=len))
