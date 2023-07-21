import os

def extract_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        values = line.strip().split()
        country = values[0]
        station = values[1]
        dates = values[2:]
        data.append((country, station, [int(val) for val in dates]))

    return data

def moving_average(data, window_size=7):
    if len(data) < window_size:
        raise ValueError("Window size is larger than the data.")

    return [sum(data[i:i+window_size])/window_size for i in range(len(data)-window_size+1)]

def filter_sweden_february_data(data):
    sweden_february_data = []
    for country, station, values in data:
        if country.lower() == 'sweden':
            # Assume the last value in 'values' is the date extracted from the filename
            last_date_value = int(values[-1])
            if last_date_value >= 20220201 and last_date_value <= 20220228:
                sweden_february_data.append((country, station, values))
    return sweden_february_data

# Get the absolute path to the file
file_name = 'Task3_flow_20220328.txt'
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))

# Task 1 - Extract ALL values from the file and return a variable containing dates, numerical values, and geographical information.
data = extract_data_from_file(file_path)

# Task 2 - Calculate a seven-day moving average for all stations located in Sweden for February.
sweden_february_data = filter_sweden_february_data(data)
sweden_moving_averages = [(country, station, moving_average(values)) for country, station, values in sweden_february_data]

# Displaying the results
print("Data for stations located in Sweden for February:")
for country, station, values in sweden_february_data:
    print(f"{country}\t{station}\t{values}")

print("\nSeven-day moving averages for stations located in Sweden for February:")
for country, station, moving_avg in sweden_moving_averages:
    print(f"{country}\t{station}\t{moving_avg}")
