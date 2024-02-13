import re

def validate_password(password):

    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
    x=re.match(pattern, password)
    if x:
        print("valid password")
    else:
        print("invalid password")    
password = input("Enter your password: ")
validate_password(password)
phn=input("Enter your phone number")
pattern2=r'^\d{10}$'
y=re.match(pattern2,phn)
if y:
    print("valid phone number")
else:
    print('invalid phone number')    
mail=input("enter you'r email")
a,b=mail.split("@")
x=mail.endswith("@gmail.com")
attern = r'^[a-z0-9]+$'
j=re.match(attern,a)
if x and j:
    print("mail is valid")
else:
    print("invalid email")    