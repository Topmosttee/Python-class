import requests

url = "http://checklight.pythonanywhere.com/get_readings/1x0d001/1/"
response = requests.get (url)
print (response)

data = response.json()
print (data["streets"][0])

def TowerofHanoi(n, from_rod, to_rod, aux_rod):
    if n==1:
        print("Move disk 1 from rod", from_rod, "to_rod", to_rod)
        return
    TowerofHanoi(n-1, aux_rod, aux_rod, to_rod)
    print ("Move disk", n, "from_rod", from_rod, "to_rod", to_rod)
    TowerofHanoi(n-1, aux_rod, to_rod, from_rod)

TowerofHanoi(4, "A", "C", "B")

class Bottle():
    pass

cokebottle = Bottle()

print(cokebottle)
print(type(cokebottle))

class Dog():
    legs = 4
    tail = 1
    color = "brown"

    def bark(self):
        sound = "woof"
        print (sound)

bingo = Dog()
print (bingo.legs)
print (bingo.tail)
print (bingo.color)
bingo.bark()

# instance attribute

class Man():
    __name = "ade"

    def __init__(self, name, skin, voice):
        
        self.skin = skin
        self.voice = voice

    def stop(self):
        print ("from self --> ", self.name)
    
    def get_name(self):
        return self.__name

me = Man ("Tope", "Brown", "Sonorous")
another_guy = Man("John", "Dark", "not fresh")
print (me.get_name(), me.skin, me.voice)
print (another_guy.get_name(), another_guy.skin, another_guy.voice)
#another_guy.name = "Shola"
print("\nAfter change\n")
print(another_guy.get_name(), another_guy.skin, another_guy.voice)

# class Acct():
#     __bal = 0

#     def __init__(self, name, bvn):
#         self.name = name
#         self.bvn = bvn

# new_acct = Acct("Bose", 10123)
# new_acct.__bal = 20000

# print (new_acct)


# import requests
# #from datetime import date

# url = "http://checklight.pythonanywhere.com/get_readings/1x0d001/1/"
# response = requests.get (url)
# #print (response)
# data = response.json()
# print (data["streets"][1])

# start_time = input ("Enter start time in this format -(Oct. 30, 2019, 12:10 AM) : )")
# end_time = input ("Enter end time in this format -(Oct. 30, 2019, 12:10 AM) : )")

# def frange(start, stop, step=1.0):
#     ''' "range()" like function which accept float type''' 
#     i = start
#     while i < stop:
#         yield i
#         i += step

# for n in frange (start_time, end_time)
# data = response.json()
# print (data["streets"][1])

