import pandas as pd;
import folium as fm;
import numpy as np;

map = fm.Map(tiles='Esri.NatGeoWorldMap', zoom_start=0.1);
fg = fm.FeatureGroup(name="TerrorFeature");

rawData = pd.read_csv(f"U:\MachineLearning\VirtualEnir\Demos\ML_Imputations\Data\DataFiles\\TerrorDist.csv", encoding='latin-1', low_memory=False)
year = rawData['iyear'];
ctry = rawData['country_txt'];
lat = rawData['latitude'];
lng = rawData['longitude'];
atkDesc= rawData['attacktype1_txt'];
cty = rawData['city'];
state = rawData['provstate'];

iCounter = 0;
'''and st=='Tamil Nadu' '''
for y,c,lt,lg,d,ct,st in zip(year,ctry,lat,lng,atkDesc,cty,state):
    if int(y)>=2002 and int(y)<=2024:
        if c=='India' and st=='Gujarat':
            #print(y,c,lt,lg);
            iCounter+=1;
            if pd.isna(lt)==False and pd.isna(lg)==False:
                fg.add_child(fm.Marker(location=[lt,lg], popup=f"{d}\n{ct}/{st}-{y}",
                                        icon=fm.Icon(color="darkred",prefix="fa", icon="exclamation-triangle") ) );
    
map.add_child(fg);
map.save("Terror_BM.html");
