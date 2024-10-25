def is_valid_age(age):
    return age.isdigit() and int(age) >= 0

entries = []

while True:
    name = input ("Enter Name: ")
    age = input ("Enter Age: ")
    if not is_valid_age(age):
        print("Error! Invalid age. Please enter a valid age.")
        continue

    entries.append({"name": name, "age": int(age)})

    another = input("Would you like to add another entry? [Yes/No]: ").strip().lower()
    if another != "yes":
        break

