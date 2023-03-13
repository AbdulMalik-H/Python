# prompt user to enter a mass mass as an integer (in kilograms)
mass = int(input("To calculate the Enrgy using Einstein equation, Please! Enter a mass (in kilogram): "))

# Einstein Equation
c2 = pow(300000000,2)
enrgy = mass * c2

print("The Enrgy by Einstein equation is: ", end='')
print("E=", enrgy, "Joules", sep=' ')