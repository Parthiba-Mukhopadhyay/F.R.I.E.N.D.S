import pandas as pd
import csv
import streamlit as st

df=pd.read_csv('./content./dataset.csv')

#dropping null values
df.dropna(how='all',axis=1,inplace=True)



#reading the user input
pettype=st.selectbox('type of pet:',['Choose your own option']+list(df['PET'].unique()))
breed=st.selectbox('breed:',['Choose your own option']+list(df[df['PET']==pettype]['BREED'].unique()))
age=st.selectbox('age of your pet:',['Choose your own option']+list(df[df['BREED']==breed]['AGE']))
gender=st.selectbox('gender of pet:',['Choose your own option']+list(df['GENDER'].unique()))
expense=st.slider(label='expense per month',min_value=2000,max_value=30000,step=100)

#extracting expense from the dataset 
dfr=df[df['BREED']==breed][['GENDER','EXPENSES','AGE']]
dfrr=dfr[dfr['AGE']==age][['GENDER','EXPENSES']]
exp=dfrr[dfrr['GENDER']==gender]['EXPENSES']

st.text(exp)

'''
#comparing the required expense and the amount the user has specified
if(expense<exp):
  amount=exp-expense
  st.text_area(label='',placeholder='You need to invest'+str(amount)+'more \n No compatibility, please allocate more responses for the maintenance of the pet')
  
else:
  st.text_area(label='',placeholder='Compatible, you may go ahead with the adoption!')
'''

