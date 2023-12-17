import array
name = array.array('u', [])
a1 = str(input("Please enter the 1st character of your name or just enter '0' to finish the process = "))
name.append(a1)
a2 = str(input("Please enter the 2nd character of your name or just enter '0' to finish the process = "))
name.append(a2)
a3 = str(input("Please enter the 3rd character of your name or just enter '0' to finish the process = "))
name.append(a3)
counter1 = 3
while True:
    counter1 += 1
    counter1 = str(counter1)
    print("Please enter the " + counter1 + "th character of your name or just enter '0' to finish ", end='')
    print("the process = ", end='')
    a4 = str(input())
    if a4 == "0":
        break
    counter1 = int(counter1)
    name.append(a4)
name.reverse()
print(name)
