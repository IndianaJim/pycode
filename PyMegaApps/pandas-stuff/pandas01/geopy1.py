from geopy.geocoders import ArcGIS
import pandas as pd

nom = ArcGIS()

#myLoc = nom.geocode("7723 e 75th st, indianapolis, in")

df=pd.read_csv("D:\py\pycode\PyMegaApps\pandas-stuff\pandas01\supermarkets.csv")


print(df)