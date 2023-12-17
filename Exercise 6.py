import array
name = input("Please enter your name = ")
name_array = array.array('u', [])
for i in name:
    if i == "A":
        i = "B"
    elif i == "a":
        i = "b"
    name_array.append(i)
print(name_array)
name_array.reverse()
print(name_array)
