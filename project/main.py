import json

def save_data():
    
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    
    key = input("What information do you want to add (e.g., degree, age)? ")
    value = input(f"Enter the value for {key}: ")

    
    data[key] = value

    # Save back to file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Information saved successfully!")

def retrieve_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No data found yet.")
        return

    key = input("What information do you want to retrieve? ")
    if key in data:
        print(f"{key}: {data[key]}")
    else:
        print("That information isn’t stored yet.")


while True:
    choice = input("Do you want to (1) add info or (2) retrieve info? (q to quit): ")
    if choice == "1":
        save_data()
    elif choice == "2":
        retrieve_data()
    elif choice.lower() == "q":
        break
    else:
        print("Invalid choice, try again.")
