import tkinter as tk
from tkinter import messagebox, ttk


class AviationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Aviation Management System")
        self.root.geometry("800x600")
        self.airlines = []
        self.flights = []
        self.passengers = []

        self.create_home_page()

    def create_home_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Aviation Management System", font=("Arial", 24, "bold"), fg="blue").pack(pady=20)

        buttons = [
            ("Add Airline", self.add_airline_page),
            ("Add Flight", self.add_flight_page),
            ("Add Passenger", self.add_passenger_page),
            ("View Airlines", self.view_airlines_page),
            ("View Flights", self.view_flights_page),
            ("View Passengers", self.view_passengers_page),
        ]

        for text, command in buttons:
            tk.Button(self.root, text=text, font=("Arial", 16), command=command, width=20, bg="lightblue").pack(pady=10)

    def add_airline_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Add Airline", font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(self.root, text="Airline Name:", font=("Arial", 14)).pack()
        airline_name_entry = tk.Entry(self.root, font=("Arial", 14))
        airline_name_entry.pack(pady=5)

        tk.Label(self.root, text="Country:", font=("Arial", 14)).pack()
        country_entry = tk.Entry(self.root, font=("Arial", 14))
        country_entry.pack(pady=5)

        def save_airline():
            name = airline_name_entry.get()
            country = country_entry.get()
            if name and country:
                self.airlines.append({"id": len(self.airlines) + 1, "name": name, "country": country})
                messagebox.showinfo("Success", "Airline added successfully!")
                self.create_home_page()
            else:
                messagebox.showerror("Error", "All fields are required.")

        tk.Button(self.root, text="Save", font=("Arial", 14), command=save_airline, bg="lightgreen").pack(pady=20)
        tk.Button(self.root, text="Back", font=("Arial", 14), command=self.create_home_page, bg="lightcoral").pack()

    def add_flight_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Add Flight", font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(self.root, text="Flight Number:", font=("Arial", 14)).pack()
        flight_number_entry = tk.Entry(self.root, font=("Arial", 14))
        flight_number_entry.pack(pady=5)

        tk.Label(self.root, text="Airline ID:", font=("Arial", 14)).pack()
        airline_id_entry = tk.Entry(self.root, font=("Arial", 14))
        airline_id_entry.pack(pady=5)

        tk.Label(self.root, text="Source Airport:", font=("Arial", 14)).pack()
        source_entry = tk.Entry(self.root, font=("Arial", 14))
        source_entry.pack(pady=5)

        tk.Label(self.root, text="Destination Airport:", font=("Arial", 14)).pack()
        destination_entry = tk.Entry(self.root, font=("Arial", 14))
        destination_entry.pack(pady=5)

        tk.Label(self.root, text="Departure Time (HH:MM):", font=("Arial", 14)).pack()
        departure_entry = tk.Entry(self.root, font=("Arial", 14))
        departure_entry.pack(pady=5)

        tk.Label(self.root, text="Arrival Time (HH:MM):", font=("Arial", 14)).pack()
        arrival_entry = tk.Entry(self.root, font=("Arial", 14))
        arrival_entry.pack(pady=5)

        def save_flight():
            flight_number = flight_number_entry.get()
            airline_id = airline_id_entry.get()
            source = source_entry.get()
            destination = destination_entry.get()
            departure = departure_entry.get()
            arrival = arrival_entry.get()

            if flight_number and airline_id and source and destination and departure and arrival:
                self.flights.append({
                    "id": len(self.flights) + 1,
                    "flight_number": flight_number,
                    "airline_id": airline_id,
                    "source": source,
                    "destination": destination,
                    "departure": departure,
                    "arrival": arrival,
                })
                messagebox.showinfo("Success", "Flight added successfully!")
                self.create_home_page()
            else:
                messagebox.showerror("Error", "All fields are required.")

        tk.Button(self.root, text="Save", font=("Arial", 14), command=save_flight, bg="lightgreen").pack(pady=20)
        tk.Button(self.root, text="Back", font=("Arial", 14), command=self.create_home_page, bg="lightcoral").pack()

    def add_passenger_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Add Passenger", font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(self.root, text="Passenger Name:", font=("Arial", 14)).pack()
        name_entry = tk.Entry(self.root, font=("Arial", 14))
        name_entry.pack(pady=5)

        tk.Label(self.root, text="Passport Number:", font=("Arial", 14)).pack()
        passport_entry = tk.Entry(self.root, font=("Arial", 14))
        passport_entry.pack(pady=5)

        tk.Label(self.root, text="Flight ID:", font=("Arial", 14)).pack()
        flight_id_entry = tk.Entry(self.root, font=("Arial", 14))
        flight_id_entry.pack(pady=5)

        def save_passenger():
            name = name_entry.get()
            passport = passport_entry.get()
            flight_id = flight_id_entry.get()

            if name and passport and flight_id:
                self.passengers.append({
                    "id": len(self.passengers) + 1,
                    "name": name,
                    "passport_number": passport,
                    "flight_id": flight_id,
                })
                messagebox.showinfo("Success", "Passenger added successfully!")
                self.create_home_page()
            else:
                messagebox.showerror("Error", "All fields are required.")

        tk.Button(self.root, text="Save", font=("Arial", 14), command=save_passenger, bg="lightgreen").pack(pady=20)
        tk.Button(self.root, text="Back", font=("Arial", 14), command=self.create_home_page, bg="lightcoral").pack()

    def view_airlines_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Airlines", font=("Arial", 20, "bold")).pack(pady=20)

        for airline in self.airlines:
            tk.Label(self.root, text=f"ID: {airline['id']}, Name: {airline['name']}, Country: {airline['country']}",
                     font=("Arial", 14)).pack(pady=5)

        tk.Button(self.root, text="Back", font=("Arial", 14), command=self.create_home_page, bg="lightcoral").pack(pady=20)

    def view_flights_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Flights", font=("Arial", 20, "bold")).pack(pady=20)

        for flight in self.flights:
            airline_name = next((a["name"] for a in self.airlines if a["id"] == int(flight["airline_id"])), "Unknown")
            tk.Label(self.root, text=f"ID: {flight['id']}, Flight Number: {flight['flight_number']}, Airline: {airline_name}, "
                                      f"Source: {flight['source']}, Destination: {flight['destination']}, "
                                      f"Departure: {flight['departure']}, Arrival: {flight['arrival']}",
                     font=("Arial", 14)).pack(pady=5)

        tk.Button(self.root, text="Back", font=("Arial", 14), command=self.create_home_page, bg="lightcoral").pack(pady=20)

    def view_passengers_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Passengers", font=("Arial", 20, "bold")).pack(pady=20)

        for passenger in self.passengers:
            flight_number = next((f["flight_number"] for f in self.flights if f["id"] == int(passenger["flight_id"])),
                                 "Unknown")
            tk.Label(self.root, text=f"ID: {passenger['id']}, Name: {passenger['name']}, Passport: {passenger['passport_number']}, "
                                      f"Flight: {flight_number}",
                     font=("Arial", 14)).pack(pady=5)

        tk.Button(self.root, text="Back", font=("Arial", 14), command=self.create_home_page, bg="lightcoral").pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the application
root = tk.Tk()
app = AviationSystem(root)
root.mainloop()
