import pandas as pd
import folium
df1=pd.read_csv("Volcanoes.txt")

def color_producer(status):
    if status == 'Historical':
        return 'green'
    elif status == 'Tephrochronology':
        return 'pink'
    elif status == 'Dendrochronology':
        return 'orange'
    elif status == 'Radiocarbon':
        return 'blue'
    else:
        return 'red'

m = folium.Map(location=[39.890343205591996, -86.03180675907001])
lats = list(df1["LAT"])
lons = list(df1["LON"])
names = list(df1["NAME"])
statuses = list(df1["STATUS"])

for lt, ln, name, status in zip(lats, lons, names, statuses):
    m.add_child(folium.Marker(location=[lt, ln], popup=(name + ", " + status), icon=folium.Icon(color=color_producer(status))))

m.save("map1.html")
