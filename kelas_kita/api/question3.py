number = [0, 1]
i = 2
while i <= 8:
    number.append(number[i-1] + number[i-2])
    i += 1
print(str(number))

# numberStr = []
# for x in number:
#     numberStr.append(str(x) + ', ')
# print(number)