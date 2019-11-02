# # Exhaustive Learning
# import datetime
# begin =datetime.datetime.now()
# Testvalue = 0
# Steps = 0.0001
# Number = 9
# while Number + Steps > Testvalue**2:
#     Testvalue += Steps
#     print (Testvalue, Testvalue**2)
# end = datetime.datetime.now()
# cost = (end - begin).seconds
# print (cost)

for i in range(111,987):
    split_number = str(i)
    a = split_number[0]
    b = split_number[1]
    c = split_number[2]
    result = [a,b,c]
    answer = "".join(result)
    answer1 = int(answer)
    print (answer1)
    y = i + i + i
    print (i)
    print (y)
    if y == answer1:
        print (y)

i = 123
split_number = str(i)
a = split_number[0]
b = split_number[1]
c = split_number[2]
result = [a,b,c]
answer = "".join(result)
answer1 = int(answer)
print (answer1)
y = i + i + i
print (y)

import random
x = random.randint(1,6)
y = random.randint(1,6)
while True:
    x = random.randint(1,6)
    y = random.randint(1,6)

    print (x,y)

    if x == 6 and y == 6:
        break


x