import pandas as pd


df = pd.read_csv("wines.csv")

# How many wines have been given a rating of 100 points?
len(df.loc[df['points'] == 100])

# What is the name of the most expensive wine?
df.loc[df['price'] == df['price'].max()]["name"].squeeze()

# Calculate a new column where you show the ratings in a scale from 0 to 5. Floats are allowed.
df["rate"] = df["points"] / 20
df

# Create a price histogram for wines that cost less than 100
df.loc[df["price"] < 100]["price"].hist()

# Plot price horizontally against points vertically. Do you think ratings increase by price? 
df.plot(x='price', y="points", figsize=(15, 3), kind="scatter")