import pandas as pd
import folium
df1=pd.read_csv("Volcanoes.txt")

m = folium.Map(location=[39.890343205591996, -86.03180675907001])
lats = list(df1["LAT"])
lons = list(df1["LON"])
names = list(df1["NAME"])
statuses = list(df1["STATUS"])

for lt, ln, name, status in zip(lats, lons, names, statuses):
    m.add_child(folium.Marker(location=[lt, ln], popup=(name + ", " + status), icon=folium.Icon(color='orange')))

m.save("map1.html")
