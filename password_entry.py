"""Jemima Giles"""

MIN_LENGTH = 6
password = input("Enter Password: ")
while len(password) < MIN_LENGTH:
    print("Password is too short")
    password = input("Enter Password: ")
for char in password:
    print("*", end=' ')
