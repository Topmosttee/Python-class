# date_of_birth = input ("Hello, please enter your date of birth (dd/mm/yyyy): ")
# year = int(date_of_birth.split("/")[2])
# # split_date = date_of_birth.split("/")
# # year = int(split_date[2])
# if (2019 - year) < 21:
#     print ("Sorry, you are underage")
# else:
#     print ("Great, pick a drink")

# # Tenary operator
# department = ["science", "commercial"]
# score = 60
# classes = "science" if score>70 else "commercial"
# print (classes)

#nested if
# tired_response = input ("Are you tired? Enter T/F: ")
# if tired_response == "T":
#     headache_response = input ("Do you have a headache? Enter T/F: ")
#     if headache_response == "T":
#         sleepy_response = input ("Have you been sleeping well? Enter T/F: ")
#         if sleepy_response == "T":
#             fever_response = input ("Do you have a fever? Enter T/F: ")
#             if fever_response == "T":
#                 print ("You have malaria. ")
#             else:
#                 print ("Sorry, we can't help you")
#         else:
#             print ("You may need to catch some sleep")
#     else:
#         print ("Get some food")
# else:
#     print ("Why are you then disturbing")


# #nested if and printing to file
# csv_file = open("clinic_log.csv", "a")
# name = input("Hello what is your name: ")
# print(name, sep = ",", file = csv_file)

# tired_response = input ("Are you tired? Enter T/F: ")
# response = True if tired_response == "T" else False
# print ("", "Tired", response, sep =",", file = csv_file)

# if tired_response == "T":
#     headache_response = input ("Do you have a headache? Enter T/F: ")
#     response = True if headache_response == "T" else False
#     print ("", "Headache", response, sep =",", file = csv_file)

#     if headache_response == "T":
#         sleepy_response = input ("Have you been sleeping well? Enter T/F: ")
#         response = True if sleepy_response == "T" else False
#         print ("", "Sleepy", response, sep =",", file = csv_file)

#         if sleepy_response == "T":
#             fever_response = input ("Do you have a fever? Enter T/F: ")
#             response = True if fever_response == "T" else False
#             print ("", "Fever", response, sep =",", file = csv_file)

#             if fever_response == "T":
#                 response = True if fever_response == "T" else False
#                 print ("", "Fever", response, sep =",", file = csv_file)
#                 print ("You have malaria. ")
#             else:
#                 print ("Sorry, we can't help you")
#         else:
#             print ("You may need to catch some sleep")
#     else:
#         print ("Get some food")
# else:
#     print ("Why are you then disturbing")


#nested if and printing to file
csv_file = open("clinic2_log.csv", "a")
name = input("Hello what is your name: ")
age = input("How old are you?: ")
print("Name", "Age", "Tired", "Headache", "Sleepy", "Fever", sep = ",", file = csv_file)

tired_response = input ("Are you tired? Enter T/F: ")
response = True if tired_response == "T" else False

if tired_response == "T":
    headache_response = input ("Do you have a headache? Enter T/F: ")
    response1 = True if headache_response == "T" else False
    
    if headache_response == "T":
        sleepy_response = input ("Have you been sleeping well? Enter T/F: ")
        response2 = True if sleepy_response == "T" else False
       
        if sleepy_response == "T":
            fever_response = input ("Do you have a fever? Enter T/F: ")
            response3 = True if fever_response == "T" else False
            
            if fever_response == "T":
                response4 = True if fever_response == "T" else False
                print (name, age, response, response1, response2, response3, response4, sep =",", file = csv_file)
                print ("You have malaria. ")
            else:
                print ("Sorry, we can't help you")
        else:
            print ("You may need to catch some sleep")
    else:
        print ("Get some food")
else:
    print ("Why are you then disturbing")
csv_file.close()

for i in 'bola':
    print (i)

for i in (1,2,3,4,5,6,7,8,9,10,11,12):
    for j in (1,2,3,4,5,6,7,8,9,10,11,12):
        print (str(i*j).center(5)," ", end ='')
    print ()

for i in range(1,13):
    for j in range(1,13):
        print (str(i*j).center(5)," ", end ='')
    print ()

for a in ('bade', 'bolu', 'Shayo', 'Monday'):
    b= len(a)
    #print (a.capitalize().center(10), '=>', b, 'chars')
    print (a.title().ljust(10), '=>', b, 'chars')

