# Python Program to find the factors of a number

# This function computes the factor of the argument passed

#Taking the number from the user
num = int(input('What is the number for which you want to check factors?: '))
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

print_factors(num)
