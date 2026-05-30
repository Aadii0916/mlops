class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""welcome to chat  ! how would you like to proceed
                         1.Press 1 for signup
                         2.Press 2 for signin
                         3.Press 3 for writting post 
                         4.Press 4  to message to friend
                         5.Press any key for exit 
                         
                         
                         -> """)    
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.post()
        elif user_input=="4":
            self.sendmsg()
        else:
            exit()


    def signup(self):  
        email=input("enter your email--->")
        pwd=input("enter your password")  
        self.username=email
        self.password=pwd
        print("you have signed in succesfully")
        print("\n")
        self.menu()


    def signin(self):
        if self.username=='' and self.password=='':
            print( "please signup first and press 1 in the main menu")    

        else:
            uname=input("enter the email/username ")
            pwd=input("enter your password")

            if self.username==uname and self.password==pwd:
                print("you siggned succesfully")
                self.loggedin=True
            else:
                print("enter the credential")    

        print("\n")
        self.menu()  


    def post(self):
        if self.loggedin==True:
            txt=input("enter your message here") 
            print(f" following content has been posted in {txt}")
        else:
            print("you need to signin first for post something")


        print("\n")
        self.menu()    


    def sendmsg(self):
        if self.loggedin==True:
            txt=input("enter the message here")
            frnd=input("whom to send message")   
            print(f"your message is sent to your  {frnd}")  

        else:
            print("you need to signup first for post something")


        print("\n")
        self.menu()                 



user=chatbook()         