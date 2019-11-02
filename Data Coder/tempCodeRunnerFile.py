
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
