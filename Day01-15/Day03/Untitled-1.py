value = float(input('please type in the length:'))
unit=input('please type in unit:')
if unit=="in":
    print('%.2f.2 inch = %.2f cm' % (value,value*2.54))
elif unit=="cm":
    print('%.2f cm = %.2f in' % (value,value/2.54))
else:
    print('please type in valid unit')
