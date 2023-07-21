from datetime import datetime, timedelta
from task1 import *

def extract_data_from_file(file_path):
  with open(file_path, 'r') as file:
    lines = file.readlines()

  # Get the date from the filename
  date_str = file_path.split('_')[1]
  year = int(date_str[:4])
  month = int(date_str[4:6])
  day = int(date_str[6:8])
  last_date = datetime(year, month, day)

  data = []
  for line in lines:
    values = line.strip().split()
    country = values[0]
    station = values[1]
    dates = values[2:]
      
    # Reformat the values array to a dictionary with keys numbering from 1 to 60 (60 days) and values as tuples of (date, value).
    formatted_data = {}
    for i, value in enumerate(dates):
      date = last_date - timedelta(days=len(dates)- i - 1)
      formatted_data[i+1] = (date.strftime("%Y/%m/%d"), int(value))
    data.append((country, station, formatted_data))
  return data

def filter_sweden_february_data(data):
    sweden_february_data = []
    for country, station, formatted_data in data:
        if country.lower() == 'sweden':
          sweden_february_data.append((country, station, formatted_data))
    return sweden_february_data

# Task 1 - Extract ALL values from the file and return a variable containing dates, numerical values, and geographical information.
file_path = 'Task3 flow_20220328.txt'
data = extract_data_from_file(file_path)

# Task 2 - Calculate a seven-day moving average for all stations located in Sweden for February.
sweden_february_data = filter_sweden_february_data(data)
sweden_moving_averages = [(country, station, movavg([value for _, value in list(formatted_data.values())], 7)) for country, station, formatted_data in sweden_february_data]

# Displaying the results
print("Data for stations located in Sweden for February:")
for country, station, formatted_data in sweden_february_data:
    print(f"{country}\t{station}\t{formatted_data}\n")

print("\nSeven-day moving averages for stations located in Sweden for February:")
for country, station, moving_avg in sweden_moving_averages:
    print(f"{country}\t{station}\t{moving_avg}\n")
