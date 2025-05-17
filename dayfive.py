# #IF STATEMENT
is_hot = False
is_cold = False

if is_hot:
    print('It is a hot day')
    print('Drink alot of water')
elif is_cold:
    print('It is a  cold day')
    print('Wear warm clothes')
else:
    print('It is a lovely day')


# classwork
price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: ${down_payment}')

# # Project one
# This project is to check the ticket price available to you according to your age
print('To know your ticket movie price')
age = int(input('Enter your age '))

if age < 0:
    print('Age must not be negative')
elif age <= 12:
    print('Your Ticket is free ')
elif 12 < age <= 17:
    print('Your Ticket is 500 Naira')
elif 17 < age <= 64:
    print('Your Ticket is 1000 naira')
elif age >64:
    print('Your Ticket is 700 naira')
else:
    print('You have to enter a valid age')


# #Project two
# This project allow you to input the weather conditions and gives you suggestion on what to do
print('To decide what to wear based on the weather')
weather = input('Enter the weather eg sunny, rainy, or cold ').capitalize()

if weather == 'Cold':
    print('The weather is cold please use your jacket or hoodie and dont forget your gloves')
elif weather == 'Hot':
    print('The weather is hot please wear light soft clothes, and stay away from black clothes')
elif weather == 'Rainy':
    print('Dont forget to go out with your umbrella and jacket')
else:
    print('ENTER A VALID WEATHER!!!')

# # project three
# This project lets you input your username and checks whether you are allowed or not
username = input('Enter user name ').lower()

if username == 'Admin' or username == 'Staff':
    print('Access Granted')
else:
    print('Access denied')

# Project four
# This project allows you to input two subject and checks wether you passed atleast one
first_subject = int(input('Enter your first suject score ' ))
second_subject = int(input('Enter your second subject score '))

if first_subject >= 50 or second_subject >=50:
    print('You passed atleast one subject or both')
else:
    print('Work harder')

# project 5
# This project is to check what you should be doing each day of the week.
day = input('Enter a day in the week ').lower()
if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thurday' or day == 'friday':
    print('It is a week day, Try to be productive and achieve your daily goal.')
elif day == 'saturday' or day =='sunday':
    print('It is the weekend! Time to relax and have fun.')
else:
    print('Enter a valid day')


#project 6
# This project is to check whether you are eligible for the ticket discount, if you are a student or
# senior citizen, then you are
age = int(input('Enter your age '))
student = input("Enter 'YES' if student and 'NO' if you are not a student ").lower()
seniorcitizen = input("Enter 'YES' if senior citizen and 'NO' if you are not a senior citizen ").lower()
if age < 18 or age > 60:
    if student == 'yes' or  seniorcitizen == 'yes':
      print('You are eligible for the discount')
    else:
      print('You are not eligible for this discount')
else:
    print('You are not eligible for this discount')

# Project 7
# This projects decides if a customer can enter a club based on their age and dress code
age = int(input('Enter your age ' ))
formalClothes = input('Are you wearing formal clothes (yes/no) ').lower()
if age >= 18:
    if formalClothes == 'yes':
        print('You are allowed to enter the club')
    elif formalClothes == 'no':
        print('You are not allowed to enter the club without formal clothes')
    else:
        print('Enter a valid answer')
else:
    print('You are not allowed in the club if you are less than 18 years.')

