# Multiplication table (from 1 to 10) in Python

#Taking number from the user for which table needs to be printed out

num = int(input('What is the number for which you want to enter the table?: '))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

