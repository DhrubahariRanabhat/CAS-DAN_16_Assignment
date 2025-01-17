import os
import pandas as pd

# Folder containing the CSV files
data_folder = "temperature_data"

# Initialize dictionaries to store data
monthly_data = {month: [] for month in range(1, 13)}
station_temps = {}

# Read all CSV files in the folder
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(data_folder, filename)
        df = pd.read_csv(file_path)
        
        # Iterate over each row and collect temperature data
        for index, row in df.iterrows():
            station = row['STATION_NAME']
            
            if station not in station_temps:
                station_temps[station] = []
                
            for month_idx, month in enumerate(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], start=1):
                temp = float(row[month])
                monthly_data[month_idx].append(temp)
                station_temps[station].append(temp)

# Calculate average temperature for each month
average_temperatures = {month: sum(temps)/len(temps) if temps else 0 for month, temps in monthly_data.items()}

# Define seasons
seasons = {
    "Summer": [12, 1, 2],
    "Autumn": [3, 4, 5],
    "Winter": [6, 7, 8],
    "Spring": [9, 10, 11]
}

# Calculate seasonal averages
seasonal_avg = {}
for season, months in seasons.items():
    temps = [average_temperatures[m] for m in months]
    seasonal_avg[season] = sum(temps) / len(temps)

# Save seasonal average temperatures to file
with open("average_temp.txt", "w") as f:
    for season, avg_temp in seasonal_avg.items():
        f.write(f"{season}: {avg_temp:.2f}\n")

# Find station with largest temperature range
station_ranges = {station: max(temps) - min(temps) for station, temps in station_temps.items()}
largest_range_station = max(station_ranges, key=station_ranges.get)

# Save largest temperature range station
with open("largest_temp_range_station.txt", "w") as f:
    f.write(f"{largest_range_station}: {station_ranges[largest_range_station]:.2f}\n")

# Find warmest and coolest stations
average_station_temps = {station: sum(temps)/len(temps) for station, temps in station_temps.items()}
warmest_station = max(average_station_temps, key=average_station_temps.get)
coolest_station = min(average_station_temps, key=average_station_temps.get)

# Save warmest and coolest stations to file
with open("warmest_and_coolest_station.txt", "w") as f:
    f.write(f"Warmest: {warmest_station} ({average_station_temps[warmest_station]:.2f})\n")
    f.write(f"Coolest: {coolest_station} ({average_station_temps[coolest_station]:.2f})\n")

print("Analysis complete. Results saved to files.")