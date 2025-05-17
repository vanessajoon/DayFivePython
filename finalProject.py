print('Enter your weight in pounds or kilograms to convert it to the other')
weight = int(input('Enter your weight in either pounds or kilograms '))
convert = input("Enter 'L' to convert to pounds or 'K' to convert to kilograms ").lower()
if convert == 'l':
    pounds = float(weight * 2.2046)
    print(f'Your weight in kilogram converted to pounds is: {weight}kg -> {pounds:.2f} pounds ')
elif convert == 'k':
    kilogram = float(weight * 0.4536)
    print(f'Your weight in pounds converted to kilogram is: {weight}lb -> {kilogram:.2f} kilograms')
else:
    print('Ivalid enter a correct weight')