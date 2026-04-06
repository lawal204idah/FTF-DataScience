# Day 2: 30 Days of python programming
# str first_name, Last_name, country_name, city, Full_name
# int year, age
# bool Is_married, is_true, is_light_on
first_name , Last_name, full_name = "Abdurrahman" , "Lawal Idah", "Abdurrahman Lawal idah"
full_name = first_name + Last_name
country = "Nigeria"
city = "Katsina"
Age = 20
Year = 2026
is_married = False
is_true = True
is_Light_on = False
# Level 2
print(type(first_name))
print(type(Last_name))
print(type(full_name))
print(len(first_name))
if len(first_name) > len(Last_name):
    print("First Name is Longer than Last Name ")
elif len(first_name) < len(Last_name):
    print("Last Name is Longer than Firts Name ")
else:
    print("Both have the same Length ")
# Adding num_one and num_two
num_one = 5
num_two = 4
Total = num_one + num_two
print(Total)
# Subtracting num_one and num_two
diff = num_two - num_one
print(diff)
# Multiplying num_one and num_two
product = num_two * num_one
print(product)
# Dividing num_one and num_two
division = num_two / num_two
print(division)
# Modulus Division of num_one and num_two
reminder = num_two % num_one
print(reminder)
# Power of num_one to num_two
variable_exp = num_one ^ num_two
print(variable_exp)
# Finding Floor division
floor_division = num_one // num_two
print(floor_division)
# Calculating Area of circle 
radius = 30
area_of_cicle = 3.1429 * radius * radius
print(area_of_cicle)
# calculating circumference of a circle
circum_of_cicle = 2 * 3.1429 * radius
print(circum_of_cicle)
# Calculating area by accepting user input
circum_of_cicle = int(input("Enter the radius of the circle "))
area_of_cicle = circum_of_cicle * 2 * 3.1429
# Getting Personal detals from user
first_name = input("Enter your First Name ")
print(first_name)
Last_name = input("Enter Your Last Name ")
print(Last_name)
country = input("Enter Your Country ")
print(country)
Age = input("Enter Your Age ")
print(Age)