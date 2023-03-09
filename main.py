import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('country_vaccination_stats.csv')

print(dataset.isnull().sum())

#To find null values in dataset we use
print(dataset.isnull().sum())

# Assign to null values what value
dataset.daily_vaccinations.fillna(value= "0")


#get info about the developed dataset
#dataset.info()

#dataset.describe()

dataset['daily_vaccinations'].median()