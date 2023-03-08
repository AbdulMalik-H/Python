# prompt user to enter a mass mass as an integer (in kilograms)
mass = int(input("To calculate the Enrgy using Einstein equation, Please! Enter a mass (in kilogram): "))

# Einstein Equation
enrgy = mass * 300000000

print("The Enrgy by Einstein equation is: ", end='')
print("E=", enrgy, "Joules", sep=' ')