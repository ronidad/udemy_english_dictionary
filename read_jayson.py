import pandas as pd

#you read the json file then pass it as the Dataframe
data = pd.read_json("supermarkets.json")

df = pd.DataFrame(data)

print(df) 