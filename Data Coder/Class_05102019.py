# List Comprehension

nums = [2, 4, 10, 3]

nums_square = [i ** 2 for i in nums]
print (nums_square)

x = [1, 3, 3, 1, 4, 7]
y = [3, 2, 1, 10, 5, 2]

mean_x = sum(x)/6
mean_y = sum(y)/6

value_x = [str(i) for i in x]
value_y = [str(i) for i in y]

print  (','.join(value_x))
print  (','.join(value_y))

print (mean_x)
print (mean_y)

var_x = ','.join([str(i-mean_x) for i in x])
print (var_x)
var_y = ','.join([str(i-mean_y) for i in y])
print (var_y)

var_sqr_x = ' '.join([str((i-mean_x)**2) for i in x])
print (var_sqr_x)
var_sqr_y = ','.join([str((i-mean_y)**2) for i in y])
print (var_sqr_y)

for i in x:
    print ((i-mean_x)**2)


mammal = [1,2,3,4,5, "cow", "cat"]
mammal.reverse()
print (mammal)



# r = mammal.index("cow")
# print (r)
# for x in mammal: 
#     print (x)                                                                                                          
#     if x == "goat":
#         break                                                                  