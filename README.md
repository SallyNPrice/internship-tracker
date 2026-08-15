# Internship Tracker

A Python command line application for organizing and tracking software engineering internship applications.

## Features

- Add internship applications
- View saved internships
- Search internships by company
- Update internship application status
- Delete internships with confirmation
- Filter internships by application status
- View application statistics through a dashboard
- Automatically record the date an internship is added
- Validate required user input
- Store internship data persistently in JSON

## Application Statuses

The tracker supports five standardized application statuses:

- Interested
- Applied
- Interview
- Offer
- Rejected

## Technologies

- Python
- JSON
- Git
- GitHub

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/SallyNPrice/internship-tracker.git
```
2. Navigate to the project directory:

```bash
cd internship-tracker
```
3. Run the application:

```bash
python app.py
```

## Example

The application provides an interactive menu:

```text
1. Add Internship
2. View Internships
3. Search Internships
4. Update Internship
5. Delete Internship
6. Filter by Status
7. Dashboard
8. Exit
```

## Project Structure

```text
internship-tracker/
├── app.py
├── internships.json
└── README.md
```
- `app.py` — application logic and command-line interface
- `internships.json` — persistent internship application data
- `README.md` — project documentation

## What I Learned
This project gave me practical experience with:
- Building a Python application from the ground up
- Organizing functionality into reusable functions
- Reading and writing structured JSON data
- Implementing CRUD operations
- Validating user input
- Searching and filtering structured data
- Aggregating data to create application statistics
- Debugging Python syntax and runtime errors
- Using Git and GitHub for version control