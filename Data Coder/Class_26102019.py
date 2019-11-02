# def function (a1, a2):
#     mult = a1 * a2
#     print (mult)

# function (3,4)
# mylist = [10,5,15]
# function(mylist,4)

# def function2 (*args):
#     print (args)
#     #print (type(args))

# function2(2,3,5,6)

# function2(mylist)
# function2(*mylist)

def function3 (**kwargs):
    print (kwargs)
    print (type(kwargs))

function3(x=10,y=20,z=30)

# Variable Positional Argument
def test(*numbers,divisor, reverse = False):
    print(numbers)
    num_list = []
    for number in numbers:
        if reverse:
            if not number % divisor == 0:
                num_list.append(number)
        else:
             if number % divisor == 0:
                num_list.append(number)
    print(num_list)

nums = range(10,20)
test (*nums,divisor=2, reverse = True)


# Variable Keyword Argument
price = 20
def func2(**prod_list):
    print (prod_list)
    for i in prod_list:
        prod_list[i] = prod_list[i] * 20
    print (prod_list)

func2(Box=2, Shoe=3, Socks=4)

def func2(**prod_list):
    print (prod_list)
    total = 0
    for i in prod_list.copy():
        item_amount = prod_list[i] * 20
        total += item_amount
        prod_list[i] = item_amount
    prod_list['total'] = total
    print (prod_list)

func2(Box=2, Shoe=3, Socks=4)

def factorial_sol(n):
    if n<=1:
        return 1
    else:
        print (f"{n}*{n-1}", end ="*")
        return n*factorial_sol(n-1)

n = 5
print (factorial_sol(n))

numbers = [2,4,5,2,5,2,2,5,2]

def diff(_list):
    difference = _list[1] - _list.pop(0)

    if len(_list) < 2:
        return difference

    print(difference)
    return diff(_list)
