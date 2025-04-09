def fahrenheit_to_celsius():
    degrees_fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5/9
    print(f"Temperature: {degrees_fahrenheit}°F = {degrees_celsius}°C")
    
if __name__ == "__main__":
    fahrenheit_to_celsius()    