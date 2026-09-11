celsius = float(input("Suhu Celsius: "))
KELVIN_OFFSET = 273.15
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + KELVIN_OFFSET
print(f"Fahrenheit: {fahrenheit:.2f}")
print(f"Kelvin: {kelvin:.2f}")
