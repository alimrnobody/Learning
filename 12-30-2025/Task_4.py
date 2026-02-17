name = input("Enter your name: ")
age_in_str = input("Enter your age: ")

age = int(age_in_str)

print("Name: ", name)
print("Age: ", age)

if age >= 60:
    print("Category: Senior")

elif age >= 30 and age < 60:
    print("Category: Adult")    

elif age >= 18 and age < 30:
    print("Category: Young")   

else:
    print("Category: Minor")       

