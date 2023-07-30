#Take input from user if he needs to change celcius to farenheit or vice versa
#celcius to fahrenheit: mode = 1
#fahrenheit to celcius: mode = 2

print('There are two modes of conversion:mode 1 for celcius to fahrenheit and mode 2 for fahrenheit to celcius.')
mode = int(input('Which conversion mode do you wish to perform?: '))
value = float(input('Please enter the value to be converted: '))
mode1formula = (value * 1.8) + 32
mode2formula = (5/9) * (value - 32)

if (mode == 1):
    print('%0.5fcelcius is equal to %0.5ffahrenheit' %(value, mode1formula))
elif (mode == 2):
    print('%0.5ffahrenheit is equal to %0.5fcelcius' %(value, mode2formula))
else:
    print('You have entered an invalid mode!')
