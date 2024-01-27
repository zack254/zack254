login_pw = "int.I0"

for i in range(3):
    password = input("login_pw: ")
    if password == login_pw:
        print("Successfully logged in.")
        break
    else:
        print("Incorrect password!")

if password != login_pw:
            print("Too many incorrect attempts. Account blocked, contact support for asistance.")

