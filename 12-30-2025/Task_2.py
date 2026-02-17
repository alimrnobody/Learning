name = input("Enter your name: ")
age_in_str = input("Enter your age: ")

age = int(age_in_str)

print("Name: ", name)
print("Age: ", age)

if age >= 18:
    print("Status: Eligible")

else:
    print("Status: Not-Eligible")    