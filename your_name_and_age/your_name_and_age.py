import re

def is_valid_name(name):
    # blocks empty names or names with only spaces.
    if not name.strip():
        return False
    
    # blocks names longer than 747 characters.
    if len(name) > 747: # limited name to 747 (person with the longest name had 747 characters).
        return False
    
    # blocks names that start with a number.
    if name[0].isdigit():
        return False
    
    # the standard checker for valid characters.
    # allows inputted names that contain: letters, numbers, spaces, hyphens, apostrophes, and special characters like Ææ
    if not re.match(r"^[A-Za-z Ææ 0-9\s\-'‘]+$", name):
        return False

    # blocks names with multiple consecutive spaces.
    if "  " in name:
        return False
    
    return True

def is_valid_age(age):
    
    # checks if the age is a positive integer.
    return age.isdigit() and 0 <= int(age) <= 122 # limited age to 122 (oldest living person was 122).

entries = []

while True:
    name = input ("Enter Name: ")
    if not is_valid_name(name):
        print("Error! Invalid name. Please enter a name with proper characters")
    age = input ("Enter Age: ")
    if not is_valid_age(age):
        print("Error! Invalid age. Please enter a valid age.")
        continue

    # checks for duplicate entries.    
    new_entry = {"name": name.strip(), "age": int(age)}
    if any(entry['name'] == new_entry['name'] and entry['age'] == new_entry['age'] for entry in entries):
        print("Error! This entry already exists. Please enter a different name and age.")
        continue

    # adds the valid entry to the list.    
    entries.append(new_entry)

    another = input("Would you like to add another entry? [Yes/No]: ").strip().lower()
    if another != "yes":
        break

# finds and displays the oldest person(s).
if entries:
    max_age = max(entry['age'] for entry in entries) 
    oldest_people = [entry for entry in entries if entry['age'] ==max_age]

    oldest_names = ', '.join(person['name'] for person in oldest_people)
    print(f"The oldest person(s): {oldest_names} with {max_age}.") 