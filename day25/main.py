# # with open("weather_data.csv", mode="r") as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# # with open("weather_data.csv", mode="r") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #
# #     for row in data:
# #         print(row)
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
#
# # print(data[data.temp == data["temp"].max()])
# # monday = data[data.day == "Monday"]
# # temp = monday.temp[0]
# # print(temp * 1.8 + 32)
# data_dict = {
#     "students": ["Karol", "Lena", "Basia"],
#     "scores": [32, 52, 1]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
#

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray = len(data[data["Primary Fur Color"] == 'Gray'].index)
black = len(data[data["Primary Fur Color"] == 'Black'].index)
red = len(data[data["Primary Fur Color"] == 'Cinnamon'].index)

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, red, black]
}
new_data = pd.DataFrame(data_dict)
print(new_data)
new_data.to_csv("squirrel_count.csv")
