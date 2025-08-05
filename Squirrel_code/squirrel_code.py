import pandas

data = pandas.read_csv("/Users/nivedhagowtham/Desktop/BA-docs /python_files/Squirrel_code/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"]== "Gray"])
red_squirrels = len(data[data["Primary Fur Color"]== "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"]== "Black"])

print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dic = {
    "Fur Colour":["Gray","Cinnamon","Black"],
    "Count": [grey_squirrels,red_squirrels,black_squirrels]
}
df = pandas.DataFrame(data_dic)
df.to_csv("/Users/nivedhagowtham/Desktop/BA-docs /python_files/Squirrel_Count.csv")