from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


master_password = input("Please enter your Master Password: ")

def view():
    with open("Passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("USERNAME:" , user,"| Password:",  fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    password = input("Your Password: ")

    with open("Passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("What would you like to do ... add a new password or view a password (view or add)? or (q to quit)").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        quit()


