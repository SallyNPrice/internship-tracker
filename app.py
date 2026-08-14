import json
import os

print("Internship Tracker")
print("------------------")

company = input("Company: ")
position = input("Position: ")
location = input("Location: ")
term = input("Term: ")
status = input("Status: ")

internship = {
    "company": company,
    "position": position,
    "location": location,
    "term": term,
    "status": status
}

if os.path.exists("internships.json"):
    with open("internships.json", "r") as file:
        internships = json.load(file)

    if  isinstance(internships, dict):
        internships = [internships]
else:
    internships = []

internships.append(internship)

with open("internships.json", "w") as file:
    json.dump(internships, file, indent=4)

print()
print("Application Added!")
print("----------------")
print("Company:", internship["company"])
print("Position:", internship["position"])
print("Location:", internship["location"])
print("Term:", internship["term"])
print("Status:", internship["status"])