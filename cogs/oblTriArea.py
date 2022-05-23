# cos, sin, tan, atan, asin, acos
# areas of obl tri will also be in here
import math
from cogs.lawOfSinesAndCosines import *

def oblTriArea():
    caseForArea = input('What is the case provided?')
    if caseForArea == 'SSS':
        SSS()
    elif caseForArea == 'SAA':
        SAA()
    elif caseForArea == 'ASA':
        ASA()
    elif caseForArea == 'SAS':
        SAS()
    else:
        print('Error: No valid case was matched to provided case. Please try again and ensure proper transcription.')
        return

def SSS():
    sidea = float(input('What is the length of the first side?'))
    sideb = float(input('What is the length of the second side?'))
    sidec = float(input('What is the length of the third side?'))
    angles = callCosAngle(sidea, sideb, sidec)
    print(SumOfSides(sidea, sideb, sidec))
    print(f'Side A: {sidea} | Side B: {sideb} | Side C: {sidec}')
    print(f'Angle A: {angles[0]} | Angle B: {angles[1]} | Angle C: {angles[2]}')

def SAA():
    print('Assume that the triangle follows the normal naming conventions (A is the angle across from a, etc.)')
    sidea = float(input('What is the length of side a?'))
    angleA = float(input('What is the value of angle A (in deg.)?'))
    angleB = float(input('What is the value of the other given angle (in deg.)?'))
    angleC = 180 - angleA - angleB
    angleARads = math.radians(angleA)
    angleBRads = math.radians(angleB)
    angleCRads = math.radians(angleC)
    sideb = (sidea * math.sin(angleBRads)) / math.sin(angleARads)
    sidec = (sidea * math.sin(angleCRads)) / math.sin(angleARads)
    print(SumOfSides(sidea, sideb, sidec))
    print(f'Side A: {sidea} | Side B: {sideb} | Side C: {sidec}')
    print(f'Angle A: {angleA} | Angle B: {angleB} | Angle C: {angleC}')

def ASA():
    print('Assume that the triangle follows the normal naming conventions (A is the angle across from a, etc.)')
    sidea = float(input('What is the length of the given side?'))
    angleB = float(input('What is the value of one of the given angels (in deg.)?'))
    angleC = float(input('What is the value of the other given angle (in deg.)?'))
    angleA = 180 - angleC - angleB
    angleCRads = math.radians(angleC)
    angleBRads = math.radians(angleB)
    angleARads = math.radians(angleA)
    sideb = (sidea * math.sin(angleBRads)) / math.sin(angleARads)
    sidec = (sidea * math.sin(angleCRads)) / math.sin(angleARads)
    print(SumOfSides(sidea, sideb, sidec))
    print(f'Side A: {sidea} | Side B: {sideb} | Side C: {sidec}')
    print(f'Angle A: {angleA} | Angle B: {angleB} | Angle C: {angleC}')



def SAS():
    print('Assume that the triangle follows the normal naming conventions (A is the angle across from a, etc.)')
    sidea = float(input('What is the length of side a?'))
    sidec = float(input('What is the length of side c?'))
    angleB = float(input('What is the value of angle B (in deg.)?'))
    angleBRads = math.radians(angleB)
    sideb = math.sqrt((sidea ** 2) + (sidec ** 2) - (2 * sidea * sidec * math.cos(angleBRads)))
    print(SumOfSides(sidea, sideb, sidec))
    angles = callCosAngle(sidea, sideb, sidec)
    print(f'Side A: {sidea} | Side B: {sideb} | Side C: {sidec}')
    print(f'Angle A: {angles[0]} | Angle B: {angles[1]} | Angle C: {angles[2]}')




def SumOfSides(sidea, sideb, sidec):
    sumOfSides = sidea + sideb + sidec
    semiperimiter = sumOfSides / 2
    semiSidea = semiperimiter - sidea
    semiSideb = semiperimiter - sideb
    semiSidec = semiperimiter - sidec
    underRadForArea = semiperimiter * semiSideb * semiSidec * semiSidea
    areaOfTri = math.sqrt(underRadForArea)
    return areaOfTri
