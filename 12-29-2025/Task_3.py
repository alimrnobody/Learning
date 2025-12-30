name = input("Enter your name: ")
monthly_salary = input("Enter your monthly salary: ")

salary = int(monthly_salary)

yearly_salary = salary * 12

print("Name: ", name)
print("Monthly Salary: ", salary)
print("Yearly Salary: ", yearly_salary)

if yearly_salary >= 600000:
    print("Status: Taxable")

else:
    print("Status: NOn-Taxable")