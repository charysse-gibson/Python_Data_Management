###################################################################
## Pandas Merging and Group By
###################################################################

## import libraries
import numpy as np
import pandas as pd
import matplotlib as plt

## print more columns by changing the max columns
pd.set_option('max_columns', 15)
## only print 10 rows
pd.set_option('max_rows', 14)

## import dataset
patient_data = \
    pd.read_csv(r'C:\Users\gibsonck\Dropbox\Work\SLU\Courses\data\ex_dm_person_demo.csv')
hospital_data = \
    pd.read_csv(r'C:\Users\gibsonck\Dropbox\Work\SLU\Courses\data\ex_dm_cluster_demo.csv')

## examine datasets
patient_data.shape
patient_data.head()
patient_data.tail()
patient_data.dtypes

hospital_data.shape
hospital_data.head()
hospital_data.tail()
hospital_data.dtypes

#### dataset subsetting and concatenation
## subset data to first 5000 rows
patient_data_1 = patient_data[:5000]
## subset to second 5000 rows
patient_data_2 = patient_data[5000:]
## concatenate data
patient_data_all = pd.concat([patient_data_1,patient_data_2])

#### Dataset merging
## merge on Clust_id
## check overlap
patient_data['Clust_id']\
    .drop_duplicates()\
    .count() #100
hospital_data['Clust_id']\
    .drop_duplicates()\
    .count() #97
## check intersection
## use shape, not count (because numpy array; not pandas series)
np.intersect1d(hospital_data['Clust_id'],
               patient_data['Clust_id']).shape
## 97 overlap 

## perform left join 
merge_left_df = \
    pd.merge(left=patient_data,
             right=hospital_data,
             how='left',
             on='Clust_id')
merge_left_df

## perform inner join
merge_inner_df = \
    pd.merge(left=patient_data,
             right=hospital_data,
             how='inner',
             on='Clust_id')

## perform right join
merge_right_df = \
    pd.merge(left=patient_data,
             right=hospital_data,
             how='right',
             on='Clust_id')

## perform outer join
merge_outer_df = \
    pd.merge(left=patient_data,
             right=hospital_data,
             how='outer',
             on='Clust_id')

## long to wide and back
## focus on lab values for each patient
labs = \
    patient_data.loc[:,['p_id','lab_value_1','lab_value_2','lab_value_3']]
labs
labs_long = \
    pd.melt(labs, 
            id_vars=['p_id'],
            var_name='lab',
            value_name='lab_value')
labs_long 
labs_wide = \
    labs_long.pivot(index='p_id',
                    columns='lab',
                    values='lab_value')
labs_wide

## group by calculations and reshaping
## calculate the mean age by gender and hospital
patient_data[['Clust_id','Gender','Age']]\
    .groupby(['Clust_id','Gender'])\
    ['Age']\
    .mean()
## reshape to gender as column, clust_id as row
patient_data\
    .groupby(['Clust_id','Gender'])\
    ['Age']\
    .mean()\
    .reset_index()\
    .pivot(index='Clust_id',columns='Gender',values='Age')

