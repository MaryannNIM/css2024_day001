# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:12:57 2024

@author: User
"""

import pandas

file = pandas.read_csv("country_data.csv")
print(file)


print(file.info())

import pandas as pd

df = pd.DataFrame(file)

print(df.describe())

file = pandas.read_csv("iris.csv")
print(file)

print(file.info())

import pandas as pd

df = pd.DataFrame(file)

print(df.describe())


file = pandas.read_csv("diab_data.csv")
print(file)

print(file.info())

import pandas as pd

df = pd.DataFrame(file)

print(df.describe())

file = pandas.read_csv("housing_data.csv")
print(file)

print(file.info())

import pandas as pd

df = pd.DataFrame(file)


print(df.describe())

file = pandas.read_csv("insurance_data.csv", skiprows=4)
print(file)

print(file.info())

import pandas as pd

df = pd.DataFrame(file)

print(df.describe())





