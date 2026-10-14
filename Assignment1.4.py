#Read a file, split its content into words, and store them in a list.
#Print the total number of words.
#Print all unique words.
with open("myfile.txt", "r") as f:
    data = f.read()

words = data.split()

print("Total words:", len(words))
print("Unique words:", set(words))

