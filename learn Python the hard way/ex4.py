cars=100
space_in_a_cars=4.0
drivers=30
passaengers=90
cars_not_drivern=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_cars
average_passengers_per_car=passaengers/cars_driven


print("There are",cars,"cars availible.")
print("There are only",drivers,"drivers availible")
print("There will be",cars_not_drivern,"empty cars today.")
print("We can transport",carpool_capacity,"people today")
print("We have",passaengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car")
print("Hey %s there"%"you")