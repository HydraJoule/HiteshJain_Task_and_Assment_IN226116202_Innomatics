"""
User Login Check
This program verifies username and password.
"""

def login_check():
    correct_username = "admin"
    correct_password = "1234"

    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    if entered_username == correct_username and entered_password == correct_password:
        print("Login Successful")
    else:
        print("Invalid Credentials")


if __name__ == "__main__":
    login_check()
