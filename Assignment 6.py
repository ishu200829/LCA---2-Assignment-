
import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Bhavna", "Chetan", "Diya", "Amit"],
    "Marks": [85, 90, np.nan, 75, 85],
    "City": ["Pune", "Mumbai", "Pune", "Nashik", "Pune"],
    "Age": [18, 19, 18, 20, 18]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter Handling Missing Values:")
print(df)

df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

df = df.drop(columns=["Age"])

print("\nAfter Removing Age Column:")
print(df)

print("\nStudents with Marks Above 80:")
print(df.loc[df["Marks"] > 80])

print("\nStatistical Description:")
print(df.describe())
