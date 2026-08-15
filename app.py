import json
import os

print("Internship Tracker")
print("------------------")

if os.path.exists("internships.json"):
    with open("internships.json", "r") as file:
        internships = json.load(file)
else:
    internships = []

while True:
    print()
    print("1. Add Internship")
    print("2. View Internships")
    print("3. Search Internships")
    print("4. Update Internship")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
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

    elif choice == "2":
        print()
        print("Saved Internships")
        print("-----------------")

        if len(internships) == 0:
            print("No internships saved yet.")
        else:
            for internship in internships:
                print("Company:", internship["company"])
                print("Position:", internship["position"])
                print("Location:", internship["location"])
                print("Term:", internship["term"])
                print("Status:", internship["status"])
                print()

    elif choice == "3":
        search = input("Search by company: ")

        print()
        print("Search Results")
        print("--------------")

        found = False

        for internship in internships:
            if search.lower() in internship["company"].lower():
                print("Company:", internship["company"])
                print("Position:", internship["position"])
                print("Location:", internship["location"])
                print("Term:", internship["term"])
                print("Status:", internship["status"])
                print()
                found = True

        if not found:
            print("No internships found.")

    elif choice == "4":
        company = input("Enter company to update: ")

        found = False

        for internship in internships:
            if internship["company"].lower() == company.lower():
                print()
                print("Current Status:", internship["status"])

                new_status = input("New Status: ")
                internship["status"] = new_status

                with open("internships.json", "w") as file:
                    json.dump(internships, file, indent=4)

                print()
                print("Internship Updated!")
                print("-------------------")
                print("Company:", internship["company"])
                print("New Status:", internship["status"])

                found = True
                break

        if not found:
            print("No internship found for that company.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")