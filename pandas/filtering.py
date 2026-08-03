import pandas as pd
df=pd.read_csv("C:\\Users\\Viper\Desktop\\C\\python\\pandas\\prac.csv")
#keeping rows that satisfy condition
rich=df[(df["Salary"]>60000) | (df["Salary"]==46000)]
print(rich)