def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit = float(input("фаренгейт: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F = {celsius:.2f}°C")