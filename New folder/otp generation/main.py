choice=1
import random
import json

f=open("authentication.txt","w")
authen={"admin":"adminpass"}
otplist=list()
json.dump(authen,f)
f.close()
h=open("otps.txt","a")
h.writelines(otplist)
h.close()
while choice!=0:
   
    print('''
            otp generator:
             1.sign in
             2.sign up
             0.exit
            enter your choice          

         ''')
    try:
        choice=input()
    
        choice=int(choice)
        if choice==1:
            with open("authentication.txt","r")as file:
               authen=json.load(file) 

        
            print("enter the your user name:\n\t")
            user=input()
            print("enter the password:\n\t")
            password=input()
            check=dict()
            check[user]=password

            if user in authen and authen[user]==password:
              print("enter y to generate otp")
              print("To exit enter '0'")
              conf=input()
              if conf=='y':
                 k=0
                 while k==0:
                    otp=random.randint(100000,999999)
                    f=open("otps.txt","r")
                    otplist=f.read().splitlines()
                    f.read()


                    if otp not in otplist:
                     k=1
                     otp=str(otp)
                     otplist.append(otp)
                     print("otp is",otp)
                     with open("otps.txt","w") as f:
                         f.writelines(otplist)
                   

              elif conf=='0':
                 print("program terminated")
                 exit()
              else:
                 print("wrong input")   
            else:
              print("wrong password and username\n")
        elif choice==2:
          print("enter your username\n")
          user=input()
          password="b"
          confpasword="a"
          while password!=confpasword:
             print("enter your password\n")
             password=input()
             print("confirm your password\n")  
             confpasword=input()
             if password!=confpasword:
                print("wrong password confirmation")
             else:
                print("user added")   
                authen[user]=password
                with open('authentication.txt',"r")as file:
                   datapass=json.load(file)
                   datapass.update({user:password})
                with open("authentication.txt","w") as f:
                   json.dump(datapass,f)
           

        elif choice==0:
           print("thank you")
        else:
           print("wrong input")    
    except ValueError:
       print("wrong choice")