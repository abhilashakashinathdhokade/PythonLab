#Q2
a = [10, "Abhi", 20, "Harshu", 30, "Amit"]
numbers=[]
names=[]
for x in a:
    if type(x) == int:
        numbers.append(x)
    else:
        names.append(x)

numbers.sort(reverse=True)

print(numbers)
print(names)
            