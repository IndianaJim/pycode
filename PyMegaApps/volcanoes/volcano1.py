import pandas as pd
import folium
df1=pd.read_csv("Volcanoes.txt")

m = folium.Map(location=[39.890343205591996, -86.03180675907001])
lats = list(df1["LAT"])
lons = list(df1["LON"])
for lt, ln in zip(lats, lons):
    m.add_child(folium.Marker(location=[lt, ln], popup="Volcano!", icon=folium.Icon(color='orange')))

m.save("map1.html")
