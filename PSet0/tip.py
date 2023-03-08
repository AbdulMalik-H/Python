# main function coded by CS50
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit)
# remove the leading $, and return the amount as a float
def dollars_to_float(d):
    d = float(d.replace('$', ''))
    return d

# percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit)
# remove the trailing %, and return the percentage as a float
def percent_to_float(p):
    p = float(p.replace('%', ''))/100
    return p

main()