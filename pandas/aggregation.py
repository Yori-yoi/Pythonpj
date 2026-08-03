import pandas as pd
df=pd.read_csv("C:\\Users\\Viper\Desktop\\C\\python\\pandas\\prac.csv")
#for entire dataframe
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True)) #max mean sum median
print(df.count()) #counts for all except null i think
#for only one column
print(df["Salary"].mean())
print(df["Salary"].median())
print(df["Salary"].count())


group=df.groupby("Experience")
print(group["Salary"].mean())
print(group["Salary"].median())
print(group["Salary"].count())