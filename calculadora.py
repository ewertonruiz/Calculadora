number_1 = int (input('Primeiro numero'))
number_2 = int (input('Primeiro numero'))

print(f'{number_1} + {number_2} =', number_1 + number_2)

#Subtraction
print ('{} - {} = '.format (number_1, number_2))
print (number_1 - number_2)

#Multiplication
print ('{} - {} = '.format (number_1, number_2))
print (number_1 * number_2)

#Division
print ('{} - {} = '.format (number_1, number_2))
print (number_1 / number_2)


Operation = input ('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input ('Enter your first number:'))
number_2 = int(input ('Enter your first number:'))

if Operation == '+':
    print ('{} + {} = '.format(number_1, number_2))
    print (number_1 + number_2)

elif Operation == '-':
     print ('{} - {} = '.format(number_1, number_2))
     print (number_1 - number_2)

elif Operation == '*':
     print ('{} * {} = '.format(number_1, number_2))
     print (number_1 * number_2)

elif Operation == '/':
     print ('{} / {} = '.format(number_1, number_2))
     print (number_1 / number_2)

else:
    print (' you have not typed a valid operator, please run the program again.')




