import pandas as pd
import os.path

#read file
file = pd.read_csv(r"C:\Users\Sahil Shiwakoti\Documents\classwork\Intro to python\labs\city_temperature.csv", sep = ",")

#grouping  highest avg temp by  region
group = file.loc[file.groupby(['Region'])['AvgTemperature'].idxmax()]

#printing the output to check for our reference
print(group)

# exporing the fil to csv format in the same folder
group.to_csv(os.path.join(r"C:\Users\Sahil Shiwakoti\Documents\classwork\Intro to python\labs\city_temperature.csv",'city_maxtemp.csv'))