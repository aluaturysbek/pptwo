import json

student = {
    "name": "Alua",
    "age": 18,
    "city": "Almaty"
}

json_data = json.dumps(student, indent=4)

print(json_data)


with open("student.json", "w") as file:
    json.dump(student, file, indent=4)


with open("student.json", "r") as file:
    data = json.load(file)

print(data)