# Program to check if a string is palindrome or not
#Taking input string from the user
my_str = input('What is the string you want to check?: ')

# making it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
