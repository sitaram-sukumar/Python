import numpy as np;
import pandas as pd;
import folium as fm;

#map1 = fm.Map(Location=[10.8, 78.7], zoom_start=0.2);
map1 = fm.Map();
tile_url = "https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png";
'''
fm.Marker(
    location=[10.8, 78.7],
    popup="Trichy",
    icon=fm.Icon(color="red", icon="star"),
    #tiles="Stamen Terrain",
    #tiles="Mapbox Bright",
    #tiles=tile_url,
    tiles="Cartodb dark_matter",
    zoom_start=10.0
).add_to(map1)
map1.save("LocMap_4.html");
'''
'''map2 = fm.Map(Location=[10.8,78.7], zoom_start=100, 
    tiles="Cartodb dark_matter", popup="Trichy",
    icon=fm.Icon(color="blue",icon="star") );
'''
map2 = fm.Map(tiles="Cartodb dark_matter");
fm.Marker(
    location=[10.8, 78.7],
    popup="Trichy",
    zoom_start=10,
    icon=fm.Icon(color="blue", icon="star")
).add_to(map2);
map2.save("LocMap_Dark2.html");

map3 = fm.Map(tiles="Cartodb dark_matter");
map3.add_child(fm.Marker( location=[60, -120], popup="New Loca",
                            icon=fm.Icon(color='green', icon="star", angle=30) ) );
map3.save("LocMap_Dark3.html");