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

