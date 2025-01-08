import sys
from test import *
from graph import *

args = sys.argv

if len(args) != 2:
    print("Provide proper command line arguments")
    exit(1)

stress = args[1]

if stress not in ["light", "medium", "heavy"]:
    print("Provide proper command line arguments")
    exit(1)

hHex, cHex, steps = time_taken(Stress['{}_STRESS'.format(stress.upper())])
plot_results(hHex, cHex, stress)
