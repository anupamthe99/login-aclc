def register():
    email=input("Enter your email adress :")
    passwd=input("Enter your password :")
    file=open("email.txt","a")
    file.write(email+'\n')
    pass_file=open("passwd.txt","a")
    pass_file.write(passwd+'\n')
    file.close()
    pass_file.close()
def login():
    emaill=input("Enter your email :")+'\n'
    paswd=input("Enter your password :")+'\n'
    file=open("email.txt","r")
    email=file.readlines()
    pass_file=open("passwd.txt","r")
    password=pass_file.readlines()
    # email check
    e=0
    for email1 in email:
        # print(email1)
        if email1==emaill:
            e+=1
    #password check
    p=0
    for passwd in password:
        # print(passwd)
        if passwd==paswd:
            p+=1
    if (e>=1):
        print("Email matched")
    else:
        print("Email does not matched")
    if(p>=1):
        print("password matched")
    else:
        print("password does not matched")          
#program start
question=input("Do you have aclc account ?(Y/N)").lower()
if question=='y':
    login()
elif question=='n':
    register()
else:
    print("Invalid option")