import math


def cosines():
    goal = input('Are you looking for a side or a angle?')
    if goal == 'angle':
        sidea = float(input('What is the length of side A?'))
        sideb = float(input('What is the length of side B?'))
        sidec = float(input('What is the length of side C?'))
        angleARads = math.acos(((sideb ** 2) + (sidec ** 2) - (sidea ** 2)) / (2 * sideb * sidec))
        angleBRads = math.acos(((sidea ** 2) + (sidec ** 2) - (sideb ** 2)) / (2 * sidea * sidec))
        angleCRads = math.acos(((sideb ** 2) + (sidea ** 2) - (sidec ** 2)) / (2 * sideb * sidea))
        angleA = math.degrees(angleARads)
        angleB = math.degrees(angleBRads)
        angleC = math.degrees(angleCRads)
        print(f'Side A: {sidea} | Side B: {sideb} | Side C: {sidec}')
        print(f'Angle A: {angleA} | Angle B: {angleB} | Angle C: {angleC}')

    else:
        sidea = float(input('What is the length of side A?'))
        sideb = float(input('What is the length of side B?'))
        angleC = float(input('What is the value of Angle C (in deg.)?'))
        angleCRads = math.radians(angleC)
        sidec = math.sqrt((sidea ** 2) + (sideb ** 2) - (2 * sidea * sideb * math.cos(angleCRads)))
        angles = callCosSide(sidea, sideb, sidec)
        print(f'Side A: {sidea} | Side B: {sideb} | Side C: {sidec}')
        print(f'Angle A: {angles[0]} | Angle B: {angles[1]} | Angle C: {angles[2]}')


def sines():
    goal = input('Are you looking for a side or a angle?')
    if goal == 'angle':
        sidea = float(input('What is the length of side A?'))
        angleA = float(input('What is the value of angle A (in deg.)?'))
        sideb = float(input('What is the length of side B?'))
        angleARads = math.radians(angleA)
        angleBRads = math.asin((sideb * math.sin(angleARads)) / sidea)
        angleB = math.degrees(angleBRads)
        print(f'The value of the remaining angle is: {angleB}')
    else:
        sidea = float(input('What is the length of side A?'))
        angleA = float(input('What is the value of angle A (in deg.)?'))
        angleB = float(input('What is the value of angle B (in deg.)?'))
        angleARads = math.radians(angleA)
        angleBRads = math.radians(angleB)
        sideb = (sidea * math.sin(angleBRads)) / math.sin(angleARads)
        print(f'The length of the side is: {sideb}.')


def callCosSide(sidea, sideb, sidec):
    angleARads = math.acos(((sideb ** 2) + (sidec ** 2) - (sidea ** 2)) / (2 * sideb * sidec))
    angleBRads = math.acos(((sidea ** 2) + (sidec ** 2) - (sideb ** 2)) / (2 * sidea * sidec))
    angleCRads = math.acos(((sideb ** 2) + (sidea ** 2) - (sidec ** 2)) / (2 * sideb * sidea))
    angleA = math.degrees(angleARads)
    angleB = math.degrees(angleBRads)
    angleC = math.degrees(angleCRads)
    angles = [angleA, angleB, angleC]
    return angles
