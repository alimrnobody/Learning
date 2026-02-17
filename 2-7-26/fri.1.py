def analyse_password(password):
    alphabets = 0
    digits = 0

    for chr in password:
        if chr.isdigit():
            digits += 1
        else:
            alphabets +=1   

    password_type = 0

    if alphabets >= 5 and digits >= 2:
        password_type = "Strong Password" 
    else:
        password_type = "Weak Password"

    return password_type

password = input("Enter your password: ")
password_type = analyse_password(password)

print(f"Password Strength: {password_type}")