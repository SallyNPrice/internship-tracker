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

print()
print("Application Added!")
print("----------------")
print("Company:", internship["company"])
print("Position:", internship["position"])
print("Location:", internship["location"])
print("Term:", internship["term"])
print("Status:", internship["status"])