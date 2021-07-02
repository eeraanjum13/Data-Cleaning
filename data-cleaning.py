# -*- coding: utf-8 -*-
"""xx.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17EAp_XHAY-WwTLnfvNL38d-dzQcwYTa3
"""

import numpy as np
import pandas as pd

df= pd.read_csv("Products.csv")

df.head(10)

df.info()

"""Seems like the Weight, Length, Width and Heights are all in "string" instead of integer type.

**Turning all the string values to Integer values as these features should be in Integer type. The number characters will turn to integer, any other invalid strings will convert to NaN**



"""

df[["height_int","weight_int","width_int","length_int"]]= df[["Height (m)", "Weight (kg)", "Width (m)", "Length (m)" ]].apply(pd.to_numeric, errors='coerce')
# errors='coerce' is used for handling any string data that cannot be converted to int. The invalid string will be 
#replaced as NaN.

df.head(5)

"""Checking for Rows with all 0 values """

outputofzerovals_all= df[(df['height_int']==0) | (df['weight_int']==0) | (df['length_int']==0) | (df['width_int']==0)]
outputofzerovals_all

"""**More than 1500 rows are consisting of all zeroes value columns. Hence, case deletion will not be ideal.**

Dropping the Previous columns with invalid strings and invalid type data, keeping only the converted ones.
"""

df.drop(columns=['Weight (kg)', 'Length (m)', 'Width (m)', 'Height (m)'], inplace=True)
df.head(2)

"""Rows with **any** NaN in their columns"""

df[df.isna().any(axis=1)] #Rows with any NaN in their columns

df[df.isna().all(axis=1)]  #There are no rows with all 'NaN' Value

df_copy= df.copy() #making sure the original clean data is not accidentally altered

df_copy.head()

"""Keeping a Copy to ensure no data is accidently lost, hampered etc.

**For handling NaN Values, I have chosen the Forward and Backward Fill Solution.**
"""

df_copy['height_int_no_na'] = df['height_int'].fillna(method='ffill').fillna(method='bfill')
df_copy['height_int_no_na'].isnull().values.any()

df_copy['weight_int_no_na'] = df['weight_int'].fillna(method='ffill').fillna(method='bfill')
df_copy['weight_int_no_na'].isnull().values.any()  #Checking if the NaN values exist after forward-backward fill

df_copy['length_int_no_na'] = df['length_int'].fillna(method='ffill').fillna(method='bfill')
df_copy['length_int_no_na'].isnull().values.any()  #Checking if the NaN values exist after forward-backward fill

df_copy['width_int_no_na'] = df['width_int'].fillna(method='ffill').fillna(method='bfill')
df_copy['width_int_no_na'].isnull().values.any()  #Checking if the NaN values exist after forward-backward fill

"""Dropping columns that are not needed"""

df_copy.drop(columns=['height_int', 'weight_int', 'width_int', 'length_int'], inplace=True)

df_copy.head(10)

df_copy.isnull().values.any() #Checking if the Dataframe has any NaN values left

"""**The Data is clean of NaN values entirely. Now to handle zero  entries. To replace the zero values, mean of the column is taken and replaced.**"""

df_copy.all() #Checking if zero value does not exist

"""Above code shows that apart from the Product ID, all columns have 0 values

Taking all the 0 values from the respective columns and replacing them with the Median value of the Column.
"""

df_copy[['height', 'weight', 'length', 'width']]=df_copy[['height_int_no_na', 'weight_int_no_na', 'length_int_no_na', 'width_int_no_na']].mask(df_copy[['height_int_no_na', 'weight_int_no_na', 'length_int_no_na', 'width_int_no_na']]==0).fillna(df_copy[['height_int_no_na', 'weight_int_no_na', 'length_int_no_na', 'width_int_no_na']].median())
df_copy

df_copy.all() #Shows the previous columns have 0 values and new columns does not contain 0 values.

#Dropping the previous columns with 0 values
df_copy.drop(columns=['height_int_no_na', 'weight_int_no_na', 'length_int_no_na', 'width_int_no_na'], inplace=True)
df_copy

df_copy.all() # affirming that none of the columns have 0 values

df_copy.isnull().values.any() #Checking if the Dataframe has any NaN values left

"""Hence all NaN values, Invalid data and zero values have been handled."""

