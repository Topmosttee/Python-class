# import mycode
# newname = mycode.name
# newage = mycode.age
# newstate = mycode.state
# print (newname,"is", newage,"and lives in", newstate)


# number = int (input ("Enter a number : "))
# if (number%2) == 0:
#     print (number, 'is an even number')
# else:
#     print (number, 'is an odd number')

# value = 40

# print ('Anita passed the exam:', (value>=55))

# q = 1,2,3,4,5,7
# print (min(q))

# Print ("Please enter your date of birth using the format below:")
# Day = int (input("Enter the day:"))
# Month = int (input("Enter the month"))
# Year = int (input("Enter te year:"))

# import calendar
# name = input("Hello, please enter your name : ")
# date_of_birth = input("Please enter dob in format dd/mm/yyyy : ")
# splitted_date = date_of_birth.split(" ")
# #print (splitted_date)
# day = splitted_date[0]
# month = int(splitted_date[1])
# year = splitted_date[2]
# month_name = calendar.month_abbr[month]
# #print (name, "your were born on day", day, "month", month, "and year", year,".")
# message = "Hello " + name + ", you were born on day " + day + " of " + month_name + " in year" + year
# message = f"Hello {name } you were born on day {day} of {month_name} in year {year}"
# print (message)

# #reverse text
# text = input("Enter any set of numbers or text: ")
# print (text[::-1])

# #reverse text
# text = input("Enter any set of numbers or text: ")
# reversed_text = "-".join(reversed(text))
# print (reversed_text)

#palindrome
# text = input("Enter any set of numbers or text: ")
# reversed_text = (text[::-1])
# if text == reversed_text:
#     print ('Text is a palindrone')
# else:
#     print ('Text is not a palindrone')

# # Searching for a string and number of occurences
text = "My mother is the best mother in the world"
sub_string = 'mother' in text
count_string = text.count('mother')

print ('Mother exists in the text: ', sub_string)
print ('Mother occurs', count_string, 'times in the text')
