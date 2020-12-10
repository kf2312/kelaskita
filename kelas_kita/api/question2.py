i = 1
number = []
while i <= 100:
    temp3 = i/3
    temp5 = i/5
    tempStr = str(i)

    if(temp3 - int(temp3) == 0):
        tempStr = tempStr + 'Fizz'

    if(temp5 - int(temp5) == 0):
        tempStr = tempStr + 'Buzz'  

    number.append(tempStr)
    i += 1

print("\n".join(number))