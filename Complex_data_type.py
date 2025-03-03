# Importing necessary modules
import cmath  # cmath module provides complex number functions
import math   # math module for mathematical functions (like degrees conversion)

# Taking user input for the real and imaginary parts of the complex number
real = float(input("Enter the real part: "))  # Convert input to float for precision
imag = float(input("Enter the imaginary part: "))  # Convert input to float

# Creating a complex number using the real and imaginary parts
z = complex(real, imag)

# Displaying the complex number
print("The complex number:", z)

# Calculating the modulus (magnitude) of the complex number
# Formula: |z| = sqrt(real^2 + imag^2)
modulus = abs(z)  # abs() returns the modulus of the complex number

# Calculating the argument (angle) of the complex number in radians
# Formula: theta = atan(imaginary / real)
argument_radians = cmath.phase(z)  # cmath.phase() returns the argument in radians

# Converting the argument from radians to degrees
argument_degrees = math.degrees(argument_radians)  # Converts radians to degrees

# Displaying the results
print(f"Complex number: {z}")
print(f"Modulus: {modulus}")  # Prints the magnitude of the complex number
print(f"Argument (radians): {argument_radians}")  # Prints the argument in radians
print(f"Argument (degrees): {argument_degrees}")  # Prints the argument in degrees
