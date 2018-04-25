import argparse
import sys

bun="bun"
burger="burger"

parser = argparse.ArgumentParser(description='Burger')
parser.add_argument('-s seseame', action='store_true', help="Including this option gives you a sesame bun")
parser.add_argument('-p', action='store_true', help="Including this option gives you a pickle")
parser.add_argument('-k', action='store_true', help="Including this option gives you a ketchup")
parser.add_argument('-m', action='store_true', help="Including this option gives you a mustard")
parser.add_argument('-c', nargs='?', help="Including this option gives you a type of cheese with the type following the option")
parser.add_argument('-e', action='store_true', help="Including this option gives you a cheddar cheese burger with all previous options also included")
args, unknown = parser.parse_known_args()

if unknown:
    #print("Not a valid option", file=sys.stderr)
    print >>sys.stderr, "fatal error"
    sys.exit()

if args.s == True:
    bun="sesame bun"
if args.e == True:
    bun="sesame bun"
    args.p = True
    args.k = True
    args.m = True
    args.c = "cheddar"



print (bun)
if args.p == True:
    print ("pickle")
if args.k == True:
    print ("ketchup")
if args.m == True:
    print ("mustard")
if args.c:
    print (args.c.lower() + " cheese")

print (burger)
print (bun)

