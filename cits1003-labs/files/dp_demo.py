# requires a bit of libraries installed, including:
# pydp, pandas, numpy, matplotlib


import pydp as dp # by convention our package is to be imported as dp (dp for Differential Privacy!)
from pydp.algorithms.laplacian import BoundedSum, BoundedMean, Count, Max
import pandas as pd
import statistics 
import numpy as np
import matplotlib.pyplot as plt

#import partitioned database files
df1 = pd.read_csv("01.csv" ,sep=",", engine = "python")
df2 = pd.read_csv("02.csv" ,sep=",", engine = "python")
df3 = pd.read_csv("03.csv" ,sep=",", engine = "python")
df4 = pd.read_csv("04.csv" ,sep=",", engine = "python")
df5 = pd.read_csv("05.csv" ,sep=",", engine = "python")


#combine to create the db
combined_df_temp = [df1, df2, df3, df4, df5]
original_dataset = pd.concat(combined_df_temp)


#create a copy of the db
redact_dataset = original_dataset.copy()

#remove the first row data
redact_dataset = redact_dataset[1:]

##uncomment to see the removed first row
#print(original_dataset.head())
#print(redact_dataset.head())

#now, only use the sales_amount column for calculations
sum_original_dataset = round(sum(original_dataset['sales_amount'].to_list()), 2)
sum_redact_dataset = round(sum(redact_dataset['sales_amount'].to_list()), 2)
sales_amount_Osbourne = round((sum_original_dataset - sum_redact_dataset), 2)

##uncomment below to check the difference, which we can use to identify the person
#print(sales_amount_Osbourne)
#assert sales_amount_Osbourne == original_dataset.iloc[0, 4]



#######################
###    Now use DP   ###
#######################
#This is the sum for the original db
dp_sum_original_dataset = BoundedSum(epsilon= 1.5, lower_bound =  5, upper_bound = 250, dtype ='float') 
dp_sum_og = dp_sum_original_dataset.quick_result(original_dataset['sales_amount'].to_list())
dp_sum_og = round(dp_sum_og, 2)

#this is the sum for the modified db
dp_redact_dataset = BoundedSum(epsilon= 1.5, lower_bound =  5, upper_bound = 250, dtype ='float')
dp_redact_dataset.add_entries(redact_dataset['sales_amount'].to_list())
dp_sum_redact=round(dp_redact_dataset.result(), 2)



#Final output
#note, DP output changes every run since it adds random value
print(f"Sum of sales_value in the orignal dataset: {sum_original_dataset}")
print(f"Sum of sales_value in the orignal dataset with DP: {dp_sum_og}")
print()
print(f"Sum of sales_value in the second dataset: {sum_redact_dataset}")
print(f"Sum of sales_value in the second dataset with DP: {dp_sum_redact}")
print()
print(f"Difference in Sum with DP: {round(dp_sum_og - dp_sum_redact, 2)}")
print(f"Actual Difference in Sum: {sales_amount_Osbourne}")
