import sys

#if the user puts in any of these inputs anywhere in the input, display help
#could probably be re-implemented to allow piping to files named help or other similar situations
if "-h" in sys.argv or "--help" in sys.argv or "help" in sys.argv:
    print "fractionToBinary.py <fraction> <number of decimals>"
    sys.exit(2)

#check to make sure the user puts in at least 2 arguments if they didn't ask for help
if 1 >= len(sys.argv) or 2 >= len(sys.argv):
    print "fractionToBinary.py <fraction> <number of decimals>"
    sys.exit(2)
try:
    fraction = float(sys.argv[1]) #the fraction/whole number to convert
    k = int(sys.argv[2]) #the number of decimal places for the output binary
except ValueError:
    print "fractionToBinary.py <fraction> <number of decimals>"
    sys.exit(2)

#converts a whole number to binary
def wtb(num):
    out = ''
    while num > 0:
        rem = num % 2
        out = str(rem) + out
        num /= 2
    return out

#converts a fraction to binary
def ftb(num, n):
    out = ''
    for x in range(0, n):
        num *= 2
        string = str(num)
        out = out + string[:1]
        num = float(string[1:])
    return out

#split the input number by the decimal point, then feed both parts into their respective functions and print the output
temp = str(fraction)
parts = temp.split('.')
parts[1] = '.' + parts[1]
#don't print the decimal point if there's no decimal formating
if k > 0:
    print wtb(int(parts[0])) + '.' + ftb(float(parts[1]), k)
else:
    print wtb(int(parts[0])) + ftb(float(parts[1]), k)