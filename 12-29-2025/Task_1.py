name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")

convert = int(birth_year)

current_year = 2025

age = current_year - convert

print("NAME: ", name)
print("Age", age)
print("Agedata_type: ", type(age))

if age >= 18:
    print("Status: Adult")

else:
    print("Status: Minor")