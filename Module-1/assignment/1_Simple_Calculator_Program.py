#takes user input
num1_inp = input("Enter the first number: ")
num2_inp = input("Enter the second number: ")

#converts into float to calculate integer and decimal calculations
number1 = float(num1_inp)
number2 = float(num2_inp)

#arithmetic operations
additon = number1 + number2
subtraction = number1 -number2
multiplication = number1 * number2
if number2 != 0:
  division = number1 / number2
else:
  division = "Cannot divide by zero"
  
#printing the calculated values
print(f"Addition: {additon}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
