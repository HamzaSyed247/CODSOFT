import secrets
import string

def password():
    a = int(input("Enter desired length of your password: "));
    password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range (a))
    print(password)

password();