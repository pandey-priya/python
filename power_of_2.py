# Display the powers of 2 using anonymous function

# Taking input from the user
terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))
print(result)

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
