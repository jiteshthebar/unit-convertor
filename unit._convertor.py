def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def inches_to_meters(inches):
    return inches * 0.0254

def meters_to_inches(meters):
    return meters / 0.0254

print("Unit Converter: Length")
print("1. Meters to Feet")
print("2. Feet to Meters")
print("3. Inches to Meters")
print("4. Meters to Inches")

choice = int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
    meters = float(input("Enter length in meters: "))
    feet = meters_to_feet(meters)
    print(f"{meters:.2f} meters is equal to {feet:.2f} feet")
elif choice == 2:
    feet = float(input("Enter length in feet: "))
    meters = feet_to_meters(feet)
    print(f"{feet:.2f} feet is equal to {meters:.2f} meters")
elif choice == 3:
    inches = float(input("Enter length in inches: "))
    meters = inches_to_meters(inches)
    print(f"{inches:.2f} inches is equal to {meters:.2f} meters")
elif choice == 4:
    meters = float(input("Enter length in meters: "))
    inches = meters_to_inches(meters)
    print(f"{meters:.2f} meters is equal to {inches:.2f} inches")
else:
    print("Invalid choice")
