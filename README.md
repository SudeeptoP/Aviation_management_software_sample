Aviation Management System
A simple GUI-based Python application built using Tkinter to manage airlines, flights, and passengers efficiently.

Features
Add Airline
Register new airlines with name and country.

Add Flight
Create flights associated with an airline, including flight number, source and destination, and timings.

Add Passenger
Add passengers by name, passport number, and link them to a flight.

View Records
View all added Airlines, Flights, and Passengers in a clean format.

Technologies Used
Python 3

Tkinter for GUI

messagebox for alerts

(Optional: ttk imported for future enhancements)

Project Structure
graphql
Copy
Edit
aviation_system/
│
├── aviation_system.py     # Main GUI application file
└── README.md              # Project overview

How to Run
Make sure Python is installed on your system.

Clone or download the repository.

Run the application:

bash
Copy
Edit
python aviation_system.py
How It Works
Data is stored in in-memory Python lists:

airlines[], flights[], passengers[]

When you add a flight or passenger, IDs are linked to their respective airline/flight using simple relational logic.

The UI dynamically updates for each operation using clear_frame() to refresh the window contents.

Future Enhancements
Save and load data using JSON or SQLite

Add edit/delete functionality

Use dropdowns for selecting airline/flight instead of manual ID entry

Improve styling with ttk widgets or custom themes

Author
Developed by Sudeepto
A beginner-friendly project to understand how to build complete GUI apps using Tkinter.
