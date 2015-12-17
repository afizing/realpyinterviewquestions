#import required packages
import pandas as pd

#Reading data
data = pd.read_csv("football.csv")
#print(data)
print(data.columns)

#select only team, Goals, Goals Allowed
data_goals = data[['Team','Goals', 'Goals Allowed']]

#Difference between for and against Goals
data_goals['Diff'] = data_goals['Goals']- data_goals['Goals Allowed']

#Getting absolute values
data_goals['Abs'] = abs(data_goals['Diff'])

#sorting difference goals
data_goals = data_goals.sort_index(by='Abs', ascending= True)

#Top 5 teams with least difference for and against goals
print(data_goals.head(5))


