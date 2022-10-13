# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)
# CSV is a comma-separated values file. and there is a library called csv that can be used to read and write CSV files.
import pandas
# pandas is a library that can be used to read and write dataframes. A dataframe is a table of data.
data = pandas.read_csv("../weather_data.csv")
print(data)
print(data["temp"])
# Pandas is a data analysis library.
# Dataframes are tables of data, while Series are 1-dimensional arrays of data (columns)
data_dict = data.to_dict()
temp_list = data["temp"].tolist()
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)
print(data["temp"].mean())  # This is the same as the previous 2 lines, but using pandas

print(data["condition"])
print(data.condition)
# To_dict() converts a dataframe to a dictionary.
# To_list() converts a series to a list.

# Getting data from a row involves specifying a condition inside the [] brackets.
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp_F = int(monday["temp"]) * 9 / 5 + 32
print(monday_temp_F)

# Creating a data frame from scratch and saving it to a csv file.
data_dict ={
    "students": ["Bob", "Alice", "Charlie", "David", "Eve"],
    "grades": [90, 85, 75, 80, 95]
}
data_frame = pandas.DataFrame(data_dict)
data.to_csv("grades.csv")

