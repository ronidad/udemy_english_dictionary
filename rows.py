import pandas as pd
#we are going to add columns and row

data = pd.read_excel("sheets.xlsx", sheet_name=1)
print(data)


print(len(data.index))
#we use shape or length to multiply the number
data["Value"]=data.shape[0]*["High"]
data["category"]=len(data.index)*["Entertainment"]
print(data)

#Adding new row means we have to Transpose and make it a column then do the opration

data1 = data.T
print(data1)

#lets first add column names to the new data frame 
data1.columns=["one", "two"]
print(data1)
#add  columns 3
data1["three"] = ["chair",10000,"medium","comfort"]
print(data1)
data = data1.T
print(data)

