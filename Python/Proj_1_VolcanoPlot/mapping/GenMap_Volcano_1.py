import numpy as np;
import pandas as pd;
import folium as fm;
'''
custattr = (
    '&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data) | &copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
)
custtiles = 'Stadia.StamenTerrain';
'''
#map = fm.Map(tiles=custtiles, attr=custattr );
#map = fm.Map(tiles="Esri.WorldImagery"); <-- works

def ColorPicker(elevation):
    if elevation<=1000:
        return 'green';
    elif 1001<elevation<3000:
        return 'orange';
    else:
        return 'red';

rawData = pd.read_csv(f"U:\\MachineLearning\\VirtualEnir\\Demos\\ML_Imputations\\Data\\2.ExploratoryDataAnalysis\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\Proj_1_VolcanoPlot\\mapping\\Volcanoes.txt")
lat = rawData["LAT"];
lng = rawData["LON"];
name = rawData["NAME"];
loca = rawData["LOCATION"];
status = rawData["STATUS"];
elevation = rawData["ELEV"];

map = fm.Map(tiles='OpenStreetMap', zoom_start=8); # ''' 'Esri.NatGeoWorldMap' '''
fg = fm.FeatureGroup(name="Volcano Feature");
  
for lt,lg,nm,loc,sta,el in zip(lat,lng,name,loca,status,elevation):
    if sta=='Radiocarbon':
        fg.add_child(fm.CircleMarker(location=[lt, lg], radius=10, fill=True, fill_color=ColorPicker(el), icon=fm.Icon(color=ColorPicker(el), prefix='fa', icon="paper-plane"), 
                            popup=f"{nm}\n {loc}\n {sta}", ext='jpg', fill_opacity=0.6) );
    else:
        fg.add_child(fm.Marker(location=[lt, lg], icon=fm.Icon(color=ColorPicker(el), prefix='fa', icon="paper-plane"), 
                            popup=f"{nm}\n {loc}\n {sta}", ext='jpg') );

fg1 = fm.FeatureGroup(name="Population Features")

fg1.add_child( fm.GeoJson(data= (open('U:\\MachineLearning\\VirtualEnir\\Demos\\ML_Imputations\\Data\\DataFiles\\World\\world.json', 'r', encoding='utf-8-sig')).read(),
                         style_function= lambda x: { 'fillColor':'yellow' if x['properties']['POP2005']<10000000
                                                                            else 'blue' if 10000000<=x['properties']['POP2005']<=100000000
                                                                            else 'black'
                          }  ) );
map.add_child(fg);  map.add_child(fg1);
map.add_child(fm.LayerControl());
map.save("VolcanoMap.html");