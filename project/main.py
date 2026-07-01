import json

print("ENTER YOUR FOLLOWING INFO \n NAME \n AGE \n Degree You are pursuing")
name = input("name:")
age = int(input("Age:"))
cource = input("Degree You did or pursuing")

data = {
    "name" : name ,
    "age"  : age,
    "cource": cource
}



with open("project/data.json", "w") as file:
    json.dump(data, file, indent=4)

 