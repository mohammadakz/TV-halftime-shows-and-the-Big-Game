# Import pandas
import pandas as pd

# Load the CSV data into DataFrames
super_bowls = pd.read_csv("super_bowls.csv")
tv = pd.read_csv("tv.csv")
halftime_musicians = pd.read_csv("halftime_musicians.csv")

# display five rows of each DataFrame
# print(super_bowls.head())
# print(tv.head())
# print(halftime_musicians.head())

# Summary of the TV daya to inspect
print(tv.info())
# Summary of the halftime musician data to inspect
print(halftime_musicians.info())
