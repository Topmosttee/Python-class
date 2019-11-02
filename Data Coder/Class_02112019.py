class Mammal:
    # General attributes - can be used by all classes that inherit from this class
    blood = "warm"
    limbs = 4
    eyes = 2

    # instance attributes = must be called in a special way (i.e. included in the parenthesis when it needs to be inherited by another class)
    def __init__(self, sound = "mute", name = "Unnamed"):
        self.name = name
        self.sound = sound

    def breate(self):
        print ("Breatin out")
        print ("Breatin in")

class Dog (Mammal):
    family = "canine"

    def __init__(self, can_play_fetch, sound = "mute",name = "Unnamed"):
        super().__init__(sound = sound, name = name)
        can_play_fetch = can_play_fetch

class Cat (Mammal):
    family = "feline"

bob = Cat(name = "Bob")
buno = Dog(name = "Buno", can_play_fetch = True)
generic = Mammal()

print (bob.name, bob.family)
print (buno.name, buno.family)
print (generic.blood)
bob. breate()

x = [1,2,3,4,5]
y = ["a", "b", "c", "d", "e"]
z = ["a", "b", "c", "d", "e"]

print (list(zip(x.y,z)))

class Stat_guy:
    def __init__(self, sample = []):
        self.sample = sample

    def get_mean(self):
        mean_samples = sum(self.sample)/len(self.sample)
        print ("Mean :", mean_samples)
        return mean_samples

    def compare_with(self, other_data):
        response = len(self.sample) > len(other_data.sample)
        mean_response = self.get_mean() > other_data.get_mean()
        print ("I am greater than the other data: ", response)
        print ("My mean is greater ", mean_response)

my_stat_data = [1,40, 2, 60, 52, 2, 70, 8, 9]
new_stat_guy = Stat_guy (sample = my_stat_data)
print(new_stat_guy.sample)
new_stat_guy.get_mean()

my_second_stat_data = [10, 3, 1, 4, 5, 7,8, 2]
second_stat_guy = Stat_guy(sample = my_second_stat_data)
new_stat_guy.compare_with(second_stat_guy)



