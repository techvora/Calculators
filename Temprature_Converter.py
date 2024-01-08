# Temperature Converter
choice = input("Convert temperature from (F)ahrenheit or (C)elsius? ")
temp = float(input("Enter temperature: "))

if choice == "F":
    celsius = (temp - 32) * 5/9
    print("The temperature in Celsius is", round(celsius, 2))
else:
    fahrenheit = temp * 9/5 + 32
    print("The temperature in Fahrenheit is", round(fahrenheit, 2))