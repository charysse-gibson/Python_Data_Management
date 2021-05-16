###################################################################
## Pandas Basics
###################################################################

## import lib
import numpy as np
import pandas as pd

## create age variable
age = pd.Series([56,24,35,42])
age
age.count()
age.mean()

## check type
type(age)

## create series for Gender
gender = pd.Series(['M','M','F','M'])
gender.mean() # error!
gender.dtype
gender.value_counts()

## create Series for Salary
salary = pd.Series(['35k','35k','50k','25k'])
salary.mean()

## combine into a dataframe
df1 = pd.DataFrame({'age' : age,
                    'gender' : gender,
                    'salary' : salary})
## check type
type(df1)

## Check shape of dataframe
df1.shape
## check rows
df1.shape[0]
## check columns?
df1.shape[1]
df1
## check dims
df1.ndim

## view the top 2 rows of the data frame
df1.head(2)
## view the bottom 3 rows of the data frame
df1.tail(3)

## check the data types
df1.dtypes

## select a column
df1['age']

## check type
type(df1['age'])

## numeric methods
df1['age'].dtype

## transform functions
np.log(df1['age'])
## summary functions
np.mean(df1['age']) 
df1['age'].mean() #sometimes available as a method to dataframe

## object methods for discrete data
df1['gender'].value_counts()
df1['gender'].unique() #returns numpy array instead of pandas series

## vectorized string methods
df1['gender'].str.lower() #lower case
df1

## extract part of string
?pd.Series.str.replace
df1['salary'].str.replace('k','')
df1['salary'] ## it didn't change the data!
df1['salary_new'] = \
    df1['salary'].str.replace('k','')
df1['salary_new']

## not numeric though, dtype is object
df1['salary_numeric'] = \
    df1['salary_new'].astype('int64')
df1.dtypes
df1['salary_numeric'].mean()
