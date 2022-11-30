#Running on python 3.9.13

import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
df = pd.read_csv('online_retail.csv')
print('File is Observed')
print (df)

#Removing rows whose StockCode or Invoice values contain non-digit characters
print ('Removing rows whose StockCode or Invoice values contain non-digit characters')

# Checking values
result = df[df.StockCode.apply(lambda x: x.isnumeric())& df.Invoice.apply(lambda x: x.isnumeric())]
# Display result
print("Result:\n",result)