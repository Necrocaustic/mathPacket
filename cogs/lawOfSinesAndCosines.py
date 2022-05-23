import math


def cosines():
    SSA = input('Is the case SSA? (y/n')
    if SSA != 'y':
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
    else:
        sidea = float(input('What is the measure of side A'))
        angleA = float(input('What is the measure of angle A (in deg.)?'))
        sidec = float(input('What is the measure of side C?'))
        angleC = callSineAngle(sidea, angleA, sidec)
        angleB = 180 - angleA - angleC
        sideb = callSineSide(sidea, angleA, angleB)
        print(f'Side A: {sidea} | Side B: {sideb} | Side C: {sidec}')
        print(f'Angle A: {angleA} | Angle B: {angleB} | Angle C: {angleC}')




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


def callCosAngle(sidea, sideb, sidec):
    angleARads = math.acos(((sideb ** 2) + (sidec ** 2) - (sidea ** 2)) / (2 * sideb * sidec))
    angleBRads = math.acos(((sidea ** 2) + (sidec ** 2) - (sideb ** 2)) / (2 * sidea * sidec))
    angleCRads = math.acos(((sideb ** 2) + (sidea ** 2) - (sidec ** 2)) / (2 * sideb * sidea))
    angleA = math.degrees(angleARads)
    angleB = math.degrees(angleBRads)
    angleC = math.degrees(angleCRads)
    angles = [angleA, angleB, angleC]
    return angles





def callSineSide(sidea, angleA, angleB):
    angleBRads = math.radians(angleB)
    angleARads = math.radians(angleA)
    sideb = (sidea * math.sin(angleBRads)) / math.sin(angleARads)
    return sideb

def callSineAngle(sidea, angleA, sideb):
    angleARads = math.radians(angleA)
    angleBRads = math.asin((sideb * math.sin(angleARads)) / sidea)
    angleB = math.degrees(angleBRads)
    return angleB


def ambiguity():
    # the cases of purely comparing side lengths are commented out because h is fine by itself it to
    # determine how many tringles there are.
    angleA = float(input('What is the measure of Angle A (in deg.)?'))
    sidea = float(input('What is the measure of Side A?'))
    sideb = float(input('What is the measure of Side B?'))
    angleARads = math.radians(angleA)
    h = sideb * math.sin(angleARads)
    if angleA > 90:
        if sidea > sideb:
            print('There is one possible triangle')
        elif sidea <= sideb:
            print('There is no possible triangles.')
    elif angleA < 90:
        if sidea < h:
            print('There is no possible triangle')
        #       elif sidea < sideb:
        #           print('There is no possible triangle')
        elif sidea == h:
            print('There is one possible triangle')
        #      elif sidea >= sideb:
        #          print('There is one possible triangle')
        elif h < sidea:
            print('There are two possible triangles')
#       elif sidea < sideb:
#         print('There are two possible triangles')
