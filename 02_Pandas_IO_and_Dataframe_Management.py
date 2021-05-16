###################################################################
## Pandas IO and Dataframe Management
###################################################################

## import libraries
import numpy as np
import pandas as pd

## import dataset
patient_data = \
    pd.read_csv(r'C:\Users\gibsonck\Dropbox\Work\SLU\Courses\data\ex_dm_person_demo.csv')
patient_data 
## examine dataset
patient_data.shape
patient_data.head()
patient_data.tail()

## print all columns by changing the width
pd.set_option('max_columns', 12)
patient_data.head()

## extract the column names
patient_data.columns

## extract the rownames? Called 'index'
patient_data.index

## find lab values from column names
## returns True/false
indicator_1 = patient_data.columns.str.startswith('lab')
patient_data.columns[indicator_1]

## get all column names in lower case
patient_data.columns.str.lower()

## only print 10 rows
pd.set_option('max_rows', 10)
patient_data

## selecting a column (or two)
patient_data['p_id']
patient_data[['p_id','Gender']]

## selecting rows 11 to 20
patient_data[10:20] # because Python starts counting at zero!

## select rows where age < 30
patient_data['Age'] < 30
patient_data[patient_data['Age'] < 30] ## seems complex
patient_data.query('Age < 30') # same effect

## use the .loc[] method to subset by rows and columns
patient_data.loc[patient_data['Age'] < 30,
                 ['p_id','Age','Gender']]
patient_data.loc[:,
                 ['p_id','Age','Gender']]
patient_data.loc[patient_data['Age'] < 30,
                 :]

## sort dataset by age
patient_data.sort_values('Age')
## sort by gender then age
patient_data.sort_values(['Gender','Age'])
## sort by descending/ascending
patient_data.sort_values(by=['Gender','Age'],
                         ascending=[True,False])

## check genders
patient_data['Gender'].value_counts(dropna=False)

## create a subset and investigate index
young_ids = \
    patient_data.loc[patient_data['Age'] < 30,
                     ['p_id','Age','Gender']]
young_ids 

## reset the index
young_ids.reset_index() # keep index as new column
young_ids.reset_index(drop=True) # discard index
young_ids2 = young_ids.reset_index(drop=True)

## export this dataset
young_ids2.to_csv(r'C:\Users\gibsonck\Dropbox\Work\SLU\Courses\data\young_ids.csv',
                 index=False)

## import excel file
sample_data = \
    pd.read_excel(r'C:\Users\gibsonck\Dropbox\Work\SLU\Courses\data\datasets.xlsx')

