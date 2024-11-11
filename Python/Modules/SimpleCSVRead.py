import pandas as pd;
import os;

class CSVReader(object):
    def CalculateMean(self, sFilePath):
        print(os.getcwd());
        if os.path.exists(sFilePath):
            data = pd.read_csv(sFilePath);
            print(data.mean());

oReader = CSVReader();
oReader.CalculateMean(f"..\\Udemy-Course\\Python\\FileIO\\Modules\\Data\\temps_today.csv")