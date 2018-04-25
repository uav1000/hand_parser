#Final Project for Udhay Vijay, Dan Crowley, John Ward
import argparse
import sys

parser = argparse.ArgumentParser(description='Poker parser')
parser.add_argument('-t', '--text',action='store', help="This option is required and is the hand history text file we will be parsing")
parser.add_argument('-v', '--vpip', action='store_true', help="Statistic")
parser.add_argument('-p','--pfr', action='store_true', help="List of inputs to run program. Seperated by inbox delimiter (Default:None)",)
parser.add_argument('-th','--threebet', action='store_true', help="Outputs a tuple of the program state (counter,calculator,inbox,outbox,memory) on exit to stderr (default: False)" )
parser.add_argument('-a', '--aggressionfactor',action='store_true', help="The delimiter for program statements (default: ;)")
args, unknown = parser.parse_known_args()


if unknown:
    #print("Not a valid option", file=sys.stderr)
    print >>sys.stderr, "fatal error"
    sys.exit()

def parse_hand(hand_file): 
    f = open(hand_file, 'r')
    x = f.readlines()
    hands=0
    newhand=False
    checkblinds=False
    for i in x:
        if "Bovada" in i:
            newhand=True
            hands+=1
        if "[ME]" in i and newhand:
            posi=i.split()[2]
            newhand=False
        if checkblinds==False:
            #print "hi"

            print (i[0]+i[1]+i[2]+i[3]+i[4])
            if i[0] == "Small":
                print (i)
            
    print (hands) 
    print ("position is:" + str(posi))
    f.close()
if args.text:
    parse_hand(args.text)
    
