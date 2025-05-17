import csv
import random 

rows = int(input("Enter the number of rows: "))
min_val = float(input("Enter the minimum value: "))
max_val = float(input("Enter the maximum value: "))
decimal_places = int(input("Enter the number of decimal places: "))

# Create and write to CSV file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # define number of columns (n) and name them 
    writer.writerow(['x', 'y']) 
    
    for _ in range(rows):
        # Depending on number of columns, for each row generate 'n' values
        x = round(random.uniform(min_val, max_val), decimal_places)
        y = round(random.uniform(min_val, max_val), decimal_places)
        writer.writerow([x, y])

print(f"CSV file 'data.csv' with {rows} rows has been created.")