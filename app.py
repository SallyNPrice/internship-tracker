import json
import os
from datetime import date

def get_required_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty. Please try again.")

def get_status():
    statuses = {
        "1": "Interested",
        "2": "Applied",
        "3": "Interview",
        "4": "Offer",
        "5": "Rejected"
    }

    while True:
        print()
        print("Status:")
        print("1. Interested")
        print("2. Applied")
        print("3. Interview")
        print("4. Offer")
        print("5. Rejected")

        choice = input("Choose a status: ").strip()

        if choice in statuses:
            return statuses[choice]

        print("Invalid status. Please choose 1, 2, 3, 4, or 5.")

def load_internships():
    if os.path.exists("internships.json"):
        with open("internships.json", "r") as file:
            return json.load(file)
    return []


def save_internships(internships):
    with open("internships.json", "w") as file:
        json.dump(internships, file, indent=4)


def add_internship(internships):
    company = get_required_input("Company: ")
    position = get_required_input("Position: ")
    location = get_required_input("Location: ")
    term = get_required_input("Term: ")
    status = get_status()

    internship = {
        "company": company,
        "position": position,
        "location": location,
        "term": term,
        "status": status,
        "date_added": str(date.today())
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
    print("Date Added:", internship["date_added"])


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
        print("Date Added:", internship.get("date_added", "Not recorded"))
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
            print("Date Added:", internship.get("date_added", "Not recorded"))
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

            new_status = get_status()
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

def filter_by_status(internships):
    status = input("Enter status to filter by: ")

    print()
    print("Filtered Internships")
    print("--------------------")

    found = False

    for internship in internships:
        if internship["status"].lower() == status.lower():
            print("Company:", internship["company"])
            print("Position:", internship["position"])
            print("Location:", internship["location"])
            print("Term:", internship["term"])
            print("Status:", internship["status"])
            print("Date Added:", internship.get("date_added", "Not recorded"))
            print()
            found = True

    if not found:
        print("No internships found with that status.")

def show_dashboard(internships):
    statuses = {
        "Interested": 0,
        "Applied": 0,
        "Interview": 0,
        "Offer": 0,
        "Rejected": 0
    }

    for internship in internships:
        status = internship["status"]

        if status in statuses:
            statuses[status] += 1

    print()
    print("Internship Dashboard")
    print("--------------------")
    print("Total Internships:", len(internships))
    print("Interested:", statuses["Interested"])
    print("Applied:", statuses["Applied"])
    print("Interview:", statuses["Interview"])
    print("Offer:", statuses["Offer"])
    print("Rejected:", statuses["Rejected"])

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
        print("6. Filter by Status")
        print("7. Dashboard")
        print("8. Exit")

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
            filter_by_status(internships)

        elif choice == "7":
            show_dashboard(internships)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()