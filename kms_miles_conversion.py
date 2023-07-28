#Take input from user if he needs to change kms to miles or vice versa
#kms to miles: mode = 1
#miles to kms: mode = 2

print('There are two modes of conversion:mode 1 for kms to miles and mode 2 for miles to kms.')
mode = int(input('Which conversion mode do you wish to perform?: '))
value = float(input('Please enter the value to be converted: '))
mode1fac = 0.62137
mode2fac = 1.60934

if (mode == 1):
    print('%0.5fkms is equal to %0.5f miles' %(value, value*mode1fac))
elif (mode == 2):
    print('%0.5fmiles is equal to %0.5fkms' %(value, value*mode2fac))
else:
    print('You have entered an invalid mode!')
