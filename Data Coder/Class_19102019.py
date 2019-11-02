def add_nums (a,b):
    #Adds two numbers
    sum_num = a+b
    print (sum_num)
    return 0

print (add_nums(1,2))
print (help(add_nums))
print (add_nums.__doc__)

def useless(name,age,_class):
    print (f"Hi {name}, welcome to {_class} class. You are {age} years old")

useless("John", 19, "first")
useless( "first","John", 19,)
useless(name="John", age=19, _class="first")
useless( age=19, name="John", _class="first")
#useless(name="John", 19, "first")
useless("John", 19, _class="first")

def func(a,b,c):
    print(f"A = {a}, B = {b}, C= {c}")

func(20,30,40)

def func(a=10,b=20,c=30):
    print(f"A = {a}, B = {b}, C= {c}")

func(a=50)

def mean(_list):
    mean = sum(_list)/len(_list)
    return mean

def variance(_list, mean):
    variance_value = [n-mean(_list) for n in _list]
    squared_variance = [n**2 for n in variance_value]

    return variance_value, squared_variance

numbers = [1,2,5,10,20]

mean_of_numbers = mean(numbers)
print (mean_of_numbers)

variance_of_numbers = variance(numbers, mean)
print (variance_of_numbers)
#print (variance_of_numbers[1])

names = [
    {
    "name": "ade",
    "age": 20,
    "score": 60  
    }, 
    {
    "name": "shade",
    "age": 40,
    "score": 70
    },
    {
    "name": "kunle",
    "age": 50,
    "score": 20
    }]
#print (names)

def funcs(new_list):
    ages = [i["age"] for i in new_list]
    scores = [i["score"] for i in new_list]
    return {'ages': ages, 'scores': scores}

age_list = funcs(names)

print (age_list['scores'])

