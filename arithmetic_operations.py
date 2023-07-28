#Taking two numbers as input from the user, and prints out the result based on the operation code chosen
# addition = 1
# subtraction = 2
# multiplication = 3
# division = 4
# modulus = 5
num1 = float(input('What is the first number?: '))
num2 = float(input('What is the second number?: '))

operation = int(input('What is the operation you want to perform?: '))

if (operation == 1):
  print('You have chosen addition operation!')
  print('Sum of %0.1f and %0.1f is %0.1f' %(num1, num2, num1+num2))
elif (operation == 2):
  print('You have chosen subtraction operation!')
  print('Difference of %0.1f and %0.1f is %0.1f' %(num1, num2, num1-num2))
elif (operation == 3):
  print('You have chosen multiplication operation!')
  print('Product of %0.1f and %0.1f is %0.1f' %(num1, num2, num1*num2))
elif (operation == 4):
  print('You have chosen division operation!')
  print('Division of %0.1f and %0.1f is %0.1f' %(num1, num2, num1/num2))
elif (operation == 5):
  print('You have chosen modulus operation!')
  print('Remainder of %0.1f by %0.1f is %0.1f' %(num1, num2, num1%num2))
else:
  print('You have chosen an invalid operation!')
