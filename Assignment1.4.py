with open("myfile.txt", "r") as f:
    data = f.read()

words = data.split()

print("Total words:", len(words))
print("Unique words:", set(words))

