###################################################################
## Pandas Data Cleaning and Dtypes 
###################################################################

## import libraries
import numpy as np
import pandas as pd
import matplotlib as plt

## print more columns by changing the max columns
pd.set_option('max_columns', 16)
## only print 10 rows
pd.set_option('max_rows', 16)

## import dataset
patient_data = \
    pd.read_csv(r'C:\Users\gibsonck\Dropbox\Work\SLU\Courses\data\ex_dm_person_demo.csv')

## examine dataset
patient_data.shape
patient_data.head()
patient_data.tail()
patient_data.dtypes

## perform type conversions
## change p_id to object
patient_data['p_id'] = \
    patient_data['p_id'].astype('object')

## change gender to be categorical
patient_data['Gender'].astype('category')
patient_data['Gender_cat'] = \
    patient_data['Gender'].astype('category',categories=['Male','Female'])
patient_data['Gender_cat'].value_counts(dropna=False)

## investiage education
patient_data['Education']\
    .value_counts(dropna=False)
patient_data['Education']\
    .str.lower()\
    .value_counts(dropna=False)
## convert to category
patient_data['Education_cat'] = \
    patient_data['Education']\
    .str.lower()\
    .astype('category',
            ordered = True,
            categories=['high school','college','graduate degree'])
## check new variable
patient_data['Education_cat'].value_counts() # correct order

## investigate age 
patient_data['Age']
patient_data['Age'].describe()
patient_data['Age'].hist(bins=40)

## check cluster of implausible ages
## set to missing
patient_data.loc[patient_data['Age'] > 110,
                 'Age'] = np.NaN
## check ages
patient_data['Age'].describe()
patient_data['Age'].hist(bins=40)

## check income
patient_data['Income'].describe()
patient_data['Income'].hist(bins=40)

## convert the date variable - month-day-year
patient_data['Baseline_date_dt'] = \
    pd.to_datetime(patient_data['Baseline_date'])

## check conversion
patient_data[['Baseline_date_dt','Baseline_date']]

## extract year from date
patient_data['Baseline_date_year'] = \
    patient_data['Baseline_date_dt'].dt.year

patient_data
