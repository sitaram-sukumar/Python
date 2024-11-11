import pandas as pd;
import datetime as d;
df1= pd.DataFrame([[10,20,30,40],[1,2,3,4],[60,70,80,90]],columns=["Price","ID","Cost","Growth"], index=["James","Sirius","Remus"]);
#df1= pd.DataFrame<[[10,20,30,40],[1,2,3,4],[60,70,80,90]]>
#df1= pd.DataFrame([[1,2,3]]);

print(df1);
print("_______");
print(df1["Growth"]);
print("_______");
print(df1["Growth"]["Remus"]);
print("_______");
print(df1[2:3]);
print("_______");
print(df1["Sirius":"Remus"]);
print("_______");
print("The vals of df1.Price\n", df1.Price);
print("_______");
print("The type of df1.Price\n", type(df1.Price));
print("_______");
print("Mean of Cols =\n", df1.mean());
print("_______");

print("Grand Mean of Cols =\n", df1.mean().mean());
print("_______");

df2 = pd.DataFrame([{"FN":"James", "LN":"Potter", "Salary":12.3, "DoB":d.date(2013, 2, 20)}, 
                    {"FN":"Lily", "LN":"Potter", "Salary":23.1, "DoB":d.date(2003, 10, 30)}, 
                    {"FN":"Sirius", "LN":"Black", "Salary":45.1, "DoB":d.date(2003, 7, 30)},  
                    {"FN":"Arnab", "LN":"Goswami", "Salary":67.1, "DoB":d.date(1994, 5, 30)}]
                    #, columns=["First_Name", "Last_Name", "Compensation", "BirthDate"], 
                    ,index=["James","Lily","Sirius", "Arnab"]
                     );
#print(df2);
#print("_________");
#print(df2["FN"]);
#columns=[]