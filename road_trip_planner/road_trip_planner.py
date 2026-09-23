# Road Trip Planner
# Calculates the estimated gas cost for a round trip.

print("================================")
print("SAN FRAN ROAD TRIP PLANS FALL 2O26")
print("================================")

# Get trip information from the user
user_name = input("What is your name? ")
destination = input("Where are you traveling? ")
one_way_miles = float(input("How many miles is the trip one way? "))
miles_per_gallon = float(input("What is your vehicle's miles per gallon? "))
gas_price = float(input("What is the gas price per gallon? "))
number_of_travelers = int(input("How many travelers are going? "))

# Calculate trip costs
total_miles = one_way_miles * 2
gallons_needed = total_miles / miles_per_gallon
gas_cost = gallons_needed * gas_price
cost_per_traveler = gas_cost / number_of_travelers

# Display the trip summary
print("================================")
print("TRIP SUMMARY")
print("================================")
print(f"Traveler: {user_name.upper()}")
print(f"Destination: {destination}")
print(f"Total miles: {total_miles:.0f}")
print(f"Gallons of gas: {gallons_needed:.2f}")
print(f"Total estimated cost: ${gas_cost:.2f}")
print(f"Estimated cost per traveler: ${cost_per_traveler:.2f}")
print("================================")
print("Have a great trip!")
