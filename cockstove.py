import random

# Function to generate random African names
def generate_african_name():
    first_names = ["Kwame", "Fatima", "Aisha", "John", "Jane", "Michael", "Musa", "Nadia", "Abdul", "Sara"]
    last_names = ["Mensah", "Mohamed", "Kamara", "Doe", "Smith", "Brown", "Abdullahi", "Ouedraogo", "Sow", "Nkosi"]
    return random.choice(first_names) + " " + random.choice(last_names)

# Function to generate random liters of ethanol gel purchased
def generate_liters_purchased():
    return random.randint(20, 100)

# Function to calculate carbon offset based on liters of ethanol gel purchased
def calculate_carbon_offset(liters):
    # Assuming each liter of ethanol gel offsets 2 kg of CO2 emissions
    return liters * 2

# Generate 500 entries
entries = []
for i in range(1, 501):
    entry = {
        "Cock Stove ID": f"CS{i:03}",
        "African Name": generate_african_name(),
        "Ethanol Gel Liters Purchased (1 Year)": generate_liters_purchased(),
    }
    entry["Carbon Offset (kg CO2)"] = calculate_carbon_offset(entry["Ethanol Gel Liters Purchased (1 Year)"])
    entries.append(entry)

# Write data to a CSV file
import csv

with open('cock_stove_data.csv', mode='w', newline='') as file:
    fieldnames = ['Cock Stove ID', 'African Name', 'Ethanol Gel Liters Purchased (1 Year)', 'Carbon Offset (kg CO2)']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for entry in entries:
        writer.writerow(entry)
