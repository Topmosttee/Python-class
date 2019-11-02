# # Searching for a string and number of occurences
log = open ("brown_skin.txt", "r")
record = open ("record.csv","a")
text = log.read ()
if not text : print ("Word","Number",sep =",", file = record)
word = input ("Enter a word to search: ")
count_string = text.count(word)
words = word.capitalize()
print (words,'occurs', count_string, 'times in the text')

print (word, count_string, sep = ",", file = record)

# # Searching for a string and number of occurences
while True:
    lyrics_file = "brown_skin.txt"
    lyrics = open (lyrics_file, "r")
    log_file = "log.csv"
    log = open(log_file, "a")
    word = input ("Please enter a word: ")
    if (word != "done!!"):
        word_count = lyrics.read().upper().count(word.upper())
        print (f"{word} appears {word_count} times")
    else:
        break

# # Searching for a string and number of occurences
word = input ("Please enter a word: ")
while word != "done!!":
    lyrics_file = "brown_skin.txt"
    lyrics = open (lyrics_file, "r")
    log_file = "log.csv"
    log = open(log_file, "a")
    word_count = lyrics.read().upper().count(word.upper())
    print (f"{word} appears {word_count} times")
    word = input ("Please enter a word: ")

    

# # Print multiplication table
# for i in (1,2,3,4,5,6,7,8,9,10,11,12):
#     for j in (1,2,3,4,5,6,7,8,9,10,11,12):
#         print (str(i*j).center(5)," ", end ='')
#     print ()

# countdown timer
import time
def countdown (n):
    while n>0:
        print (n)
        time.sleep(1)
        n-=1
        if n == 0:
            print ("go")
Time = int(input ("Enter number of seconds: "))
countdown(Time)

#countdown timer
import time
seconds = 30
for i in reversed (range (0, seconds)):
    print (i, end = "")
    print ("\r", end = "")
    time.sleep(1)
    

# Leap year
count = 0
for i in range(1700, 2019):
    if (i % 4) == 0:
        print (i, "is a leap year")
        count +=1
print ("There are", count, "leap years")

# Leap year
for i in range(1700, 2019):
    if (i % 4) == 0:
        print (i, ' ', end = '')

# Odd numbers
x = int(input("Enter the beginning number: "))
y = int(input ("Enter the end number: "))
for i in range(x,y+1):
    if (i % 2) != 0:
        print (i)

# Odd numbers
x = int(input("Enter the beginning number: "))
y = int(input ("Enter the end number: "))
for i in range(x,y+1):
        print ([i % 2] != 0)