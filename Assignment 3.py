#import random
#for x in range(10):
#  print random.randint(1,21)*5,
#print

import random
def getrandnum():
  randnum = random.randint(0,9)
  return randnum

random_number = getrandnum()
print (random_number)
