users = []
loggedin_user = []

def menu():
    print("1. Login")
    print("2. Signup")
    
    menu = input("Enter your choise: ")
    if menu == "1":
        login()
    elif menu == "2":
        signup()
    else:
        print("Invalid Input!")
        menu()
        
        
def signup():
    print("Create new user")
    
    name = input("Enter your name: ")
    
    while True:
        username = input("Enter a unique username: ")
         
        if any(user["username"] == username for user in users):
            print("Username already taken")
        else:
            break
        
    while True:
        password = input("Enter a password: ")
        confirm_password = input("Confirm your password: ")
        
        if password != confirm_password:
            print("Password did not match!")
        else:
            break
    
    users.append({
        "name": name,
        "username": username,
        "password": password
    })
    
    print(users)  # testing.......
    print("Account successfully created")
    menu()
    
    
def login():
    print("Login to your account.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    for user in users:
        if user["username"] == username and user["password"]== password:
            name = user["name"]
            print(f"Welcome, {name}")
            loggedin_user.append({
                "username": username,
                "password": password
            })
            
            print(loggedin_user) # testing...
            usermenu()
            return

    print("Invalid username or password")
    menu()
            
            
def usermenu():
    print("1. Logout")
    print("2. Profile")
    print("3. Change name")
    print("4. Change username")
    print("5. Change password")
    usermenu = input("Enter your choise: ")
    if usermenu == "1":
        logout()
    elif usermenu == "2":
        profile()
    elif usermenu == "3":
        changeName()
    elif usermenu == "4":
        changeUsername()
    elif usermenu == "5":
        changePassword()
    else:
        print("Invalid")
        usermenu()
    
    
def logout():
        loggedin_user.clear()
        print("Successfully logout")
        menu()

def profile():
    current_user = loggedin_user[0]
    current_username = current_user["username"]
    for user in users:
        if current_username == user["username"]:
            print(f"Name: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Password: {user['password']}")
            usermenu()
            return
    print("Something wrong! Please login again.")
    menu()
    

    
def changeName():
    current_user = loggedin_user[0]
    current_username = current_user["username"]
    for user in users:
        if current_username == user["username"]:
            print(f"Name: {user['name']}")
            new_name = input("Enter new name: ")
            user["name"] = new_name
            print("Name successfully changed.")
            usermenu()
            return
    print("Something wrong! Please login again.")
    menu()
    
def changeUsername():
    current_user = loggedin_user[0]
    current_username = current_user["username"]
    for user in users:
        if current_username == user["username"]:
            print(f"Username: {user['username']}")
            while True:
                new_username = input("Enter new username: ")
                if any(user["username"] == new_username for user in users):
                    print("Usename already taken! Try a differnt one.")
                else:
                    user["username"] = new_username
                    print("Username successfully changed.")
                    print("Please login again.")
                    # After chnaging the username is wil be updated inside user=[] but not in loggedin_user=[], that is why logout() operation is help to clear it and store loggin user again.
                    logout()
                    break
            return
    print("Something wrong! Run the the programme again.")
    
            
    
def changePassword():
    current_user = loggedin_user[0]
    current_username = current_user["username"]
    for user in users:
        if current_username == user["username"]:
            print(f"Password: {user['password']}")
            
            while True:
                new_password = input("Enter new password: ")
                confirm_new_password = input("Confirm new password: ")
                if new_password != confirm_new_password:
                    print("New password did not match.")
                else:
                    user["password"] = new_password
                    print("Password successfully changed.")
                    print("Please login again")
                    # After chnaging the password is wil be updated inside user=[] but not in loggedin_user=[], that is why logout() operation is help to clear it and store loggin user again.
                    logout()
                    break
            return
    print("Something wrong! Please run the system again.")
        
                    
        
menu()