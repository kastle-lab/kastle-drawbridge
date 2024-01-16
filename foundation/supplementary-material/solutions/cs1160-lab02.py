import math

# Input
floor_length = float(input("Enter floor length (feet): "))
floor_width = float(input("Enter floor width (feet): "))
furnace_length_inches = float(input("Enter the furnace length (inches): "))
furnace_width_inches = float(input("Enter the furnace width (inches): "))
water_heater_circumference_inches = float(input("Enter the water heater circumference (inches): "))

# Convert furnace dimensions to feet
furnace_length_feet = furnace_length_inches / 12.0
furnace_width_feet = furnace_width_inches / 12.0

# Calculate the radius of the water heater in feet
water_heater_radius_feet = water_heater_circumference_inches / (2 * math.pi * 12.0)

# Calculate the area of the water heater and furnace in square feet
water_heater_area_square_inches = math.pi * water_heater_radius_feet ** 2 * 144.0
furnace_area_square_inches = furnace_length_feet * furnace_width_feet * 144.0

# Calculate the total paintable area in square feet
total_area_feet = floor_length * floor_width
net_paintable_area_feet = total_area_feet - water_heater_area_square_inches / 144.0 - furnace_area_square_inches / 144.0

# Round the net paintable area to two decimal places
net_paintable_area_rounded = int(1000 * net_paintable_area_feet + 0.5) / 1000


# Output the result
print("Net floor area (square feet):", net_paintable_area_rounded)
