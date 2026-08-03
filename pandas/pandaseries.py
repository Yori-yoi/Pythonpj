import pandas as pd
data=[100,102,103,104,105,106,107]
series=pd.Series(data,index=["a","b","c","d","e","f","g"])
marks={"Alpha":93,"Beta":92,"cey":91,"day":90,"ey":80}
table=pd.Series(marks)
print(table)
print(table.loc["Alpha"])
print(table[table>84])
print(series)
series.loc["a"]=99
series.iloc[2]=1001
print(series.loc["a"])
print(series.loc["c"])
print(series.iloc[2])
print(series[series>104])