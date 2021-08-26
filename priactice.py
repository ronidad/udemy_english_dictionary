import pandas as pd

data1 = pd.read_excel("sheets.xlsx", sheet_name=0)

data2 = pd.read_excel("sheets.xlsx", sheet_name=1)
print("Excel file 1, sheet 1")
print(data1)
print("Exele fine 1, sheet 2")
print(data2)


#reading txt files. we use csv read method but those separated by ; we use sep=";"

data3 = pd.read_csv("supermarkets-semi-colons.txt", sep=";")

print("Supermarket file data")
print(data3)