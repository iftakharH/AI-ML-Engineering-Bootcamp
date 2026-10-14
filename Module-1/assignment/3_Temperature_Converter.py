#takes input
celsius_raw = input("Enter temperature in Celsius: ")

#converts to float
celsius = float(celsius_raw)

#calculation
fahrenheit = (celsius * 9 / 5) + 32

#printing output in fahrenheit
print(f"Temperature in Fahrenheit is: {fahrenheit:.1f}°F")
