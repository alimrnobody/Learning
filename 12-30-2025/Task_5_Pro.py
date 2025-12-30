name = input("Enter your name: ")
birth_year_in_str = input("Enter your birth year: ")
marks_in_str = input("Enter your marks: ")
monthly_fee_in_str = input("Enter your monthly fee:")

birth_year = int(birth_year_in_str)
marks = int(marks_in_str)
monthly_fee = int(monthly_fee_in_str)

current_year = 2025

age = current_year - birth_year

print("Name: ", name)
print("Age: ", age)
print("Marks: ", marks)

#staus ki line hai yia
if age >= 18 and marks >= 50:
    print("Status: Eligible")

else:
    print("Status: Not-Eligible")    


#marks ki line hai 
if marks >= 80:
    print("Grade: A")

elif marks >= 60 and marks < 80:
    print("Grade: B")

elif marks >= 40 and marks < 60:
    print("Grade: C")

else:
    print("Fail")    

#monthly fee ki line
if monthly_fee >= 20000:
    print("Fee Category: High Fee")

elif monthly_fee >= 10000  and monthly_fee < 20000:
    print("Fee Category: Medium Fee")

else:
    print("Fee Category: Low Fee")

#check data types of age and marks
print("Age Data Type: ", type(age))    
print("Marks Data Type: ", type(marks))  
        