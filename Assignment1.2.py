#Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line

with open("myfile.txt", "r") as f:
    lines = f.readlines()

print("Total lines:", len(lines))
print("2nd line:", lines[1])
print("4th line:", lines[3])

