import pandas as pd


from geopy.geocoders import ArcGIS
nom = ArcGIS()

data = pd.read_json("supermarkets.json")

df = pd.DataFrame(data)

n =nom.geocode("3666 21st St, San Francisco, CA 94114 ")
m = nom.geocode("North start building, lenana road, Nairobi")
# print(m.latitude)
# print(m.longitude)


df["Adress"]=df["Address"]+", " + df["City"]+ ", "+ df["State"]+ ", " + df["Country"]
df["Coordinates"] = df["Address"].apply(nom.geocode)
print(df["Coordinates"][0].latitude)

df["Latitude"]= df["Coordinates"].apply(lambda x: x.latitude if x!=None else None)
df["Longitude"]= df["Coordinates"].apply(lambda x: x.longitude if x!=None else None)
print(df["Longitude"])
