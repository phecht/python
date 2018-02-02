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


my_map = folium.Map(location=[9.326465, -83.744402], zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, na in zip(lat, lon, elev, name):
    MY_POPUP = str(na) + ", elevation:" + str(el)
    MY_COLOR = popup_color(el)


    fgv.add_child(folium.CircleMarker(location=[lt,ln], 
        popup=folium.Popup(MY_POPUP,parse_html=True), 
        color=MY_COLOR,
        fill=True,
        fill_opacity=0.7
        ).add_to(fgv))

fgp = folium.FeatureGroup(name="Population")
LOW_POINT =    5000000
MID_POINT  =  50000000
HIGH_POINT = 100000000

fgp.add_child(folium.GeoJson(data=open('world2.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < LOW_POINT 
    else 'yellow' if LOW_POINT <= x['properties']['POP2005'] < MID_POINT 
    else 'orange' if MID_POINT <= x['properties']['POP2005'] < HIGH_POINT
    else 'blue'}))

my_map.add_child(fgp)
my_map.add_child(fgv)

my_map.add_child(folium.LayerControl())
my_map.save("map2.html")