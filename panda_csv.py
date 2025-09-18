import pandas as pd

brics = pd.read_csv("pandas/brics.csv",index_col=0)

print(brics)

#loc method
print(brics.loc[['BR','RU'],['country','capital']])

#iloc method
print(brics.iloc[[3,4],[1,2]])

#pandas series
print(type(brics.loc['BR']))
#pandas dataframe
print(type(brics.loc[['BR']]))
