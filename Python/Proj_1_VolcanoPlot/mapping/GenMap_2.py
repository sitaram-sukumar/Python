import numpy as np;
import pandas as pd;
import folium as fm;
'''
OpenTopoMap = fm.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    max: 17,
	attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
});
'''

map1 = fm.Map();
#map1 = fm.Map(tiles='https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png', attr='CartoDB.Voyager');
fg1 = fm.FeatureGroup(name="MapFeat");
fg1.add_child(fm.Marker(location=[10.9, 78.7], popup="TN, India", zoom_start=20,
                        icon=fm.Icon(color='green', icon='star')) );
map1.add_child(fg1);
map1.save("Map_Feat_1.html");