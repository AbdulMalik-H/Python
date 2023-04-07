# function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is
# in column 70 of the display

def right_justify(s):
    # len() fucnction use to count letters on str
    # (70-len(s)) subtracktion 70 from length of s str
    print(' '*(70-len(s)) + s)

right_justify('monty')