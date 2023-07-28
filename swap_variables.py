# Taking inputs from the user
a = input('Enter value of x: ')
b = input('Enter value of y: ')

# create a temp variable and swap the values of the two variables
temp = a
a = b
b = temp

print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))
