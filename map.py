import folium
from folium.plugins import MarkerCluster
import pandas as pd


#Define coordinates of where we want to center our map
boulder_coords = [40.015, -105.2705]

#Create the map
my_map = folium.Map(location = boulder_coords, zoom_start = 13)

#Display the map
my_map


