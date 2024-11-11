import time as t;
import os;
import pandas as pd;

iCounter = 2;

while True and iCounter>0:
    if os.path.exists("..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\Modules\\Data\\temps_today.csv"):
        data = pd.read_csv("..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\Modules\\Data\\temps_today.csv");
        print(data.mean(), type(data), data.mean()["st1"] );
        print( type(data.mean()["st1"]) );
    else:
        print("File Does not exist");
    
    iCounter = iCounter-1;
    t.sleep(3);
