#importing pandas
import pandas as pd

#reading file using pandas csv read.
data = pd.read_csv("weather.csv")

#select only required columns. Maximum and Minimum are in 1 and 2 indexes.
data_req = data[[0,1,2]]
print(data_req)

#create the spread field
data_req['SprD'] = data_req['MxT'] - data_req['MnT']

#sorting based on SprD
data_req = data_req.sort_index(by='SprD')

#printing the final data.
print(data_req)
