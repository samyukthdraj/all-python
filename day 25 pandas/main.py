#import csv
import pandas

data = pandas.read_csv("./day 25 python/weather_data.csv")
print(f"Temperatures are: \n{data["temp"]}")

print (f"Conditions are \n{data.condition}")
print (f"Mean is: {data["temp"].mean()}")
print (f"Mean is also: {data.temp.mean()}")

print (data[data.day == "Monday"])
# with open("./day 25 python/weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = [] 
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
# all these lines of code can be done by just a sinlge line of pandas.read_csv 


