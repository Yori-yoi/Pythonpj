import pandas as pd
#drop irrelevant columns
df=pd.read_csv("C:\\Users\\Viper\Desktop\\C\\python\\pandas\\prac.csv")
df=df.drop(columns=["Experience","Salary"])
print(df)

#Handle missing data
df=df.dropna(subset=["Name"])

#to replace na values
df=df.fillna({"Name":"None"})
print("\n",df.to_string())

df=df.replace({"Marketing":"MARKETING","IT":"it"})
print("\n",df.to_string())  

#standardised text
df["Name"]=df["Name"].str.lower()
print("\n",df.to_string()) 

#remove duplicate elements
df=df.drop_duplicates()