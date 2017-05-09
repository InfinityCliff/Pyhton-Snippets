import pandas as pd
import numpy as np


''' Covnert dictionary to pandas DataFrame
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.from_dict.html
'''
dic = {}
df = pd.DataFrame.from_dict(dic)


'''
replace nan with empty string
'''
df1 = df.replace(np.nan, '', regex=True)
# or
df.replace(np.nan, '', regex=True, inplace=True)

'''
Get list from pandas DataFrame column headers
'''
list(df.columns.values)
# or
list(df)
# or
df.columns.values.tolist()

'''
Get Index from pndas DataFrame as list
'''
df.index.tolist()

'''
Generating a randaom DataFrame
'''
df = pd.DataFrame(np.random.randn(6, 4),
                  index=list(range(0, 12, 2)),
                  columns=list(range(0, 8, 2)))

'''
Generate a Dataframe of set size range and width
'''
width = 4
rng = 6
data = np.array([np.arange(rng)]*width).T
df2 = pd.DataFrame(data)