import pandas as pd;
df1 = pd.DataFrame([[1,2,3,4],[10,20,30,40]], columns=["SNo", "StudentID", "MathSc", "SciSc"], index=["Prahalya", "Dhwani"]);
print(df1);

df2 = pd.DataFrame([{"id":"1", "Name":"James", "Sub":"Physics"}, 
                    {"id":"2", "Name":"Lily", "Sub":"Magic"}, 
                    {"id":"3", "Name":"Snape", "Sub":"Sark Arts"}],
                    index=["Stu1", "Stu2", "stu3"]);
print(df2);

print(df1.mean(), type(df1.mean()));
print("_____________")
print(df1["MathSc"]);
print("_____________")
print(df1["MathSc"], df1["MathSc"].mean(), type(df1["MathSc"]), type(df1["MathSc"].mean()));
#print(df2.mean())