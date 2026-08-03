import pandas as pd
df=pd.read_csv("C:\\Users\\Viper\Desktop\\C\\python\\pandas\\prac.csv")
print(df.to_string()) # prints everything 
df2=pd.read_json("C:\\Users\\Viper\Desktop\\C\\python\\pandas\\js.json")
print("\n" ,df2.to_string())

#selection by column
print(df["Name"].to_string()) # .to string makes almost no difference only for very big data use string to print everything whichc normally doesnt
print(df[["Name","Salary"]].to_string())

#selection by row
print(df.loc[1,["Name","Salary"]])
print(df.iloc[0:11:2,0:3]) #start:end:step, which columns

df3=pd.read_csv("C:\\Users\\Viper\Desktop\\C\\python\\pandas\\prac.csv",index_col="Name")
name=input("Name enter: ")
try:
    print(df3.loc[name])
except KeyError:
    print(f"{name}not found")