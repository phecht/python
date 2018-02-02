import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def popup_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'blue'
    else:
        return 'red'

map = folium.Map(location=[lat[0],lon[0]],zoom_start=6 )

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, na in zip(lat, lon, elev, name):
    MY_POPUP = str(na) + ", elevation:" + str(el)
    MY_COLOR = popup_color(el)


    fg.add_child(folium.CircleMarker(location=[lt,ln], 
        popup=folium.Popup(MY_POPUP,parse_html=True), 
        color=MY_COLOR,
        fill=True,
        fill_opacity=0.7
        ).add_to(fg))

map.add_child(fg)
map.save("map1.html")