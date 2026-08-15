import json
import os


def load_internships():
    if os.path.exists("internships.json"):
        with open("internships.json", "r") as file:
            return json.load(file)
    return []


def save_internships(internships):
    with open("internships.json", "w") as file:
        json.dump(internships, file, indent=4)


def add_internship(internships):
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
    save_internships(internships)

    print()
    print("Application Added!")
    print("----------------")
    print("Company:", internship["company"])
    print("Position:", internship["position"])
    print("Location:", internship["location"])
    print("Term:", internship["term"])
    print("Status:", internship["status"])


def view_internships(internships):
    print()
    print("Saved Internships")
    print("-----------------")

    if len(internships) == 0:
        print("No internships saved yet.")
        return

    for internship in internships:
        print("Company:", internship["company"])
        print("Position:", internship["position"])
        print("Location:", internship["location"])
        print("Term:", internship["term"])
        print("Status:", internship["status"])
        print()


def search_internships(internships):
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


def update_internship(internships):
    company = input("Enter company to update: ")

    for internship in internships:
        if internship["company"].lower() == company.lower():
            print()
            print("Current Status:", internship["status"])

            new_status = input("New Status: ")
            internship["status"] = new_status

            save_internships(internships)

            print()
            print("Internship Updated!")
            print("-------------------")
            print("Company:", internship["company"])
            print("New Status:", internship["status"])
            return

    print("No internship found for that company.")


def delete_internship(internships):
    company = input("Enter company to delete: ")

    for internship in internships:
        if internship["company"].lower() == company.lower():
            print()
            print("Internship Found")
            print("----------------")
            print("Company:", internship["company"])
            print("Position:", internship["position"])
            print("Status:", internship["status"])

            confirm = input("Delete this internship? (y/n): ")

            if confirm.lower() == "y":
                internships.remove(internship)
                save_internships(internships)
                print("Internship deleted!")
            else:
                print("Deletion cancelled.")

            return

    print("No internship found for that company.")


def main():
    internships = load_internships()

    print("Internship Tracker")
    print("------------------")

    while True:
        print()
        print("1. Add Internship")
        print("2. View Internships")
        print("3. Search Internships")
        print("4. Update Internship")
        print("5. Delete Internship")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_internship(internships)

        elif choice == "2":
            view_internships(internships)

        elif choice == "3":
            search_internships(internships)

        elif choice == "4":
            update_internship(internships)

        elif choice == "5":
            delete_internship(internships)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()