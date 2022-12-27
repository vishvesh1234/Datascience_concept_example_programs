# Write a Pandas program to join the two given dataframes along rows and assign all data.
import pandas as pd
import numpy as np

exam_dic1  = {'name': ['Aman', 'Kamal', 'Amjad', 'Rohan', 'Amit', 'Sumit', 'Matthew', 'Kartik', 'Kavita', 'Pooja'],
        'perc': [79.5, 29, 90.5, np.nan, 32, 65, 56, np.nan, 29, 89],
          'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

exam_data1 = pd.DataFrame(exam_dic1)

exam_dic2  = {'name': ['Parveen', 'Ahil', 'Ashaz', 'Shifin', 'Hanash'],
        'perc': [89.5, 92, 90.5, 91.5, 90],
          'qualify': ['yes', 'yes', 'yes', 'yes', 'yes']}

exam_data2 = pd.DataFrame(exam_dic2)

print("Original DataFrames:")
print(exam_data1)
print("-------------------------------------")
print(exam_data2)
print("\nJoin the said two dataframes along rows:")
result_data = pd.concat([exam_data1, exam_data2])
print(result_data)