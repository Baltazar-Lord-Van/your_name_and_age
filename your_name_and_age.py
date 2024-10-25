entries = []

while True:
    name = input ("Enter Name: ")
    age = input ("Enter Age: ")

    entries.append({"name": name, "age": int(age)})

    another = input("Would you like to add another entry? [Yes/No]: ").strip().lower()
    if another != "yes":
        break

