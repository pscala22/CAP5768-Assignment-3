#Running on python 3.9.13

import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
df = pd.read_csv('online_retail.csv')
print('File is Observed')
print (df)

def changes():
    #Removing rows whose StockCode or Invoice values contain non-digit characters
    print ('Removing rows whose StockCode or Invoice values contain non-digit characters')
    print (df[df.StockCode.apply(lambda x: x.isnumeric())& df.Invoice.apply(lambda x: x.isnumeric())])
    #removing rows whose Price values are less than 10
    print ('removing rows whose Price values are less than 10')
    print (df[df['Price'] > 10]) 
    #removing rows whose country values are not equal to "United Kingdom", "Italy", "France", "Germany", "Norway", "Finland", "Austria", "Belgium", "European Community", "Cyprus", "Greece", "Iceland", "Malta", "Netherlands", "Portugal", "Spain", "Sweden", or "Switzerland"
    print ('removing rows whose country values are not equal to "United Kingdom", "Italy", "France", "Germany", "Norway", "Finland", "Austria", "Belgium", "European Community", "Cyprus", "Greece", "Iceland", "Malta", "Netherlands", "Portugal", "Spain", "Sweden", or "Switzerland"')
    countries = ["United Kingdom", "Italy", "France", "Germany", "Norway", "Finland", "Austria", "Belgium", "European Community", "Cyprus", "Greece", "Iceland", "Malta", "Netherlands", "Portugal", "Spain", "Sweden", "Switzerland"]
    print (df[df.Country.isin(countries)])
    
changes()