import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

print("The number of grey squirrels is", grey_count)
print("The number of cinnamon squirrels is", cinnamon_count)
print("The number of black squirrels is", black_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Number": [grey_count, cinnamon_count, black_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_data.csv")

