
from cogs.oblTriArea import *
from cogs.trigFuncs import *
from cogs.lawOfSinesAndCosines import *


def main():
    typeOfTrig = input('What type of trig is required?\n'
                       'Options are:\n '
                       '| A - Trig functions |\n '
                       '| B - Obl Tris |\n'
                       '| C - Law of Sines |\n '
                       '| D - Law of Cosines |\n'
                       '| E - Check for Ambiguity | \n '
                       'Answer using A, B, C, D, or E.')
    if typeOfTrig == 'A':
        trigFuncs()
    elif typeOfTrig == 'B':
        oblTriArea()
    elif typeOfTrig == 'C':
        sines()
    elif typeOfTrig == 'D':
        cosines()
    elif typeOfTrig == 'E':
        ambiguity()
    else:
        print('Not a valid response. Terminating program.')







main()