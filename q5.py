distance = float(input("Enter the trip distance (miles): "))
speed = float(input("Enter the average speed (mph): "))
mpg = float(input("Enter the fuel efficiency (mpg): "))
price = float(input("Enter the gas price per gallon: "))

time = round(distance/speed, 1)
gallons = round(distance/mpg, 1)
cost = round(price * gallons, 1)

print()

print(f"For a trip of {distance} miles at an average speed of {speed} mph, "
      f"the driving time will be {time} hours.")
print()
print(f"Your car will use {gallons} of gas, and the total fuel cost will be ${cost}")

