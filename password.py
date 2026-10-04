password = input("Enter your password: ")
credentials = {
    "password": password
}

if credentials['password'] == "Agent123":
    print("Access granted. Welcome, Agent!")
else:
    print("Access denied.")