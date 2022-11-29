#Running on python 3.9.13

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
df = pd.read_csv('online_retail.csv')
print ("File is observed")
df.head()