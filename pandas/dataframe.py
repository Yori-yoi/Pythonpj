import pandas as pd
animal_lives={
    "animals":["Lion","tiger","squirrel","hippo","rhino"],"lives":[ 30,35,10,30,50]
    }
df=pd.DataFrame(animal_lives,index=[1,2,3,4,5])

print(df.loc[1])
print(df.iloc[1])
print(df)

#to add a new column

df["income"]=[1000,2000,30,800,1000]
print(df)

#adding a new row

new_row=pd.DataFrame([{"animals":"mosquito","lives":1,"income":0},{"animals":"piranha","lives":1,"income":1}],index=[6,7])
df=pd.concat([df,new_row])  
print(df)