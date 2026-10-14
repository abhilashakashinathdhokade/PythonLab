#Write a program to read a file and count how many vowels are present in its content
with open("myfile.txt", "r") as f:
    data = f.read()

count = 0

for ch in data:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels:", count)

