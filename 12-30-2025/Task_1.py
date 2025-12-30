name = input("Enter your name: ")
marks_in_str = input("Enter your marks: ")

marks = int(marks_in_str)

print("Name: ", name)
print("Total Marks: ", marks)

if marks >= 80:
    print("Grade: A")

elif marks >= 60 and marks < 80:
    print("Grade: B")

elif marks >= 40 and marks < 60:
    print("Grade: C")    

else:
    print("Congratulations! You are Fail")   