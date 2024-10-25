import re

def is_valid_name(name):
    return bool(re.match(r"^[A-Za-zÆæ0-9\s\-'‘]+$", name))

def is_valid_age(age):
    return age.isdigit() and int(age) >= 0

entries = []

while True:
    name = input ("Enter Name: ")
    if not is_valid_name(name):
        print("Error! Invalid name. Please enter a name with letters, spaces, and hyphens")
    age = input ("Enter Age: ")
    if not is_valid_age(age):
        print("Error! Invalid age. Please enter a valid age.")
        continue

    entries.append({"name": name, "age": int(age)})

    another = input("Would you like to add another entry? [Yes/No]: ").strip().lower()
    if another != "yes":
        break

