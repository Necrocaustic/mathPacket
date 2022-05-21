# trig funcs through user gateway here
import math

def trigFuncs():
    trigOrUnitCircle = input('Do you need a unit circle or exact trig?')
    if trigOrUnitCircle == 'trig' or 'exact trig':
        typeOfFunc = input('What type of trig is required?\n'
                           '(Please answer in one word, using arc___ to express an inverse trig func.)')
        if typeOfFunc == 'cos':
            num = float(input('What is the angle needed to take the COS of?'))
            degOrRad = input('Was this number entered in Degs? (Y / N)')
            if degOrRad == 'Y':
                num = math.radians(num)
            print(math.cos(num))
        elif typeOfFunc == 'sin':
            num = float(input('What is the angle needed to take the SIN of?'))
            degOrRad = input('Was this number entered in Degs? (Y / N)')
            if degOrRad == 'Y':
                num = math.radians(num)
            print(math.sin(num))
        elif typeOfFunc == 'tan':
            num = float(input('What is the angle needed to take the SIN of?'))
            degOrRad = input('Was this number entered in Degs? (Y / N)')
            if degOrRad == 'Y':
                num = math.radians(num)
            print(math.tan(num))
        elif typeOfFunc == 'arccos':
            num = float(input('What is the angle needed to take the SIN of?'))
            degOrRad = input('Was this number entered in Degs? (Y / N)')
            if degOrRad == 'Y':
                num = math.radians(num)
            print(math.acos(num))
        elif typeOfFunc == 'arcsin':
            num = float(input('What is the angle needed to take the SIN of?'))
            degOrRad = input('Was this number entered in Degs? (Y / N)')
            if degOrRad == 'Y':
                num = math.radians(num)
            print(math.asin(num))
        elif typeOfFunc == 'arctan':
            num = float(input('What is the angle needed to take the SIN of?'))
            degOrRad = input('Was this number entered in Degs? (Y / N)')
            if degOrRad == 'Y':
                num = math.radians(num)
            print(math.atan(num))
    else:
        typeOfFunc = input('What type of trig is required?')
        if typeOfFunc == 'cos':
            num = int(input('What is the angle you need the cos of, in deg?'))
            if num == 30 or 330:
                print('The {b} value for {a} is:\n'
                      'rt(3)/2'.format(a=num, b=typeOfFunc))
            elif num == 45 or 315:
                print('The {b} value for {a} is:\n'
                      'rt(2)/2'.format(a=num, b=typeOfFunc))
            elif num == 60 or 300:
                print('The {b} value for {a} is:\n'
                      '1/2'.format(a=num,b=typeOfFunc))
            elif num == 150 or 210:
                print('The {b} value for {a} is:\n'
                      '-rt(3)/2'.format(a=num, b=typeOfFunc))
            elif num == 135 or 225:
                print('The {b} value for {a} is:\n'
                      '-rt(2)/2'.format(a=num,b=typeOfFunc))
            elif num == 240 or 120:
                print('The {b} value for {a} is:\n'
                      '-1/2'.format(a=num, b=typeOfFunc))
            elif num == 0 or 360:
                print('The {b} value for {a} is:\n'
                      '1'.format(a=num, b=typeOfFunc))
            elif num == 90:
                print('The {b} value for {a} is:\n'
                      '0'.format(a=num, b=typeOfFunc))
            elif num == 180:
                print('The {b} value for {a} is:\n'
                      '-1'.format(a=num, b=typeOfFunc))
            elif num == 270:
                print('The {b} value for {a} is:\n'
                      '0'.format(a=num, b=typeOfFunc))
            else:
                print('Not a valid Unit Circle angle. Terminating program.')
                return
        elif typeOfFunc == 'sin':
            num = int(input('What is the angle you need the cos of, in deg?'))
            if num == 30 or 150:
                print('The {b} value for {a} is:\n'
                      '1/2'.format(a=num, b=typeOfFunc))
            elif num == 45 or 135:
                print('The {b} value for {a} is:\n'
                      'rt(2)/2'.format(a=num, b=typeOfFunc))
            elif num == 60 or 120:
                print('The {b} value for {a} is:\n'
                      'rt(3)/2'.format(a=num,b=typeOfFunc))
            elif num == 330 or 210:
                print('The {b} value for {a} is:\n'
                      '-1/2'.format(a=num, b=typeOfFunc))
            elif num == 315 or 225:
                print('The {b} value for {a} is:\n'
                      '-rt(2)/2'.format(a=num,b=typeOfFunc))
            elif num == 240 or 300:
                print('The {b} value for {a} is:\n'
                      '-rt(3)/2'.format(a=num, b=typeOfFunc))
            elif num == 0 or 360:
                print('The {b} value for {a} is:\n'
                      '0'.format(a=num, b=typeOfFunc))
            elif num == 90:
                print('The {b} value for {a} is:\n'
                      '1'.format(a=num, b=typeOfFunc))
            elif num == 180:
                print('The {b} value for {a} is:\n'
                      '0'.format(a=num, b=typeOfFunc))
            elif num == 270:
                print('The {b} value for {a} is:\n'
                      '-1'.format(a=num, b=typeOfFunc))
            else:
                print('Not a valid Unit Circle angle. Terminating program.')
                return
