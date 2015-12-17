#import required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#this functions takes dataset and draws bar chart.
def plotBar(dataSet,plotType,title,xaxis, yaxis):
    plt.rcParams['figure.figsize'] = (15, 5)
    dataSet.plot(kind=plotType)
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.show()


#Reading data
data = pd.read_csv("football.csv")
#print(data)
print(data.columns)

#select only team, Goals, Goals Allowed
data_goals = data[['Team','Goals', 'Goals Allowed']]

dd = data[['Team','Goals', 'Goals Allowed']]
plotBar(dd,"bar", "Goals Made vs Goals Given", "Teams", "Goals")

#Difference between for and against Goals
data_goals['Diff'] = data_goals['Goals']- data_goals['Goals Allowed']

#Getting absolute values
data_goals['Abs'] = abs(data_goals['Diff'])

#sorting difference goals
data_goals = data_goals.sort_index(by='Abs', ascending= True)

#Top 5 teams with least difference for and against goals
print(data_goals.head(5))

