
# Locate the 3 largest values in a data frame.
import pandas as pd 
data={'Name':['Aman','Rohit','Deepika','Kamal','Deva','Ramesh','Adnan'], 
'Sales':[8500,4500,9300,8600,9200,9600,8400]} 
sales=pd.DataFrame(data) 
# Find  3 Largest Value for MarksinlP Column
print(sales.nlargest(3,['Sales']))