import pandas as pd
import csv
df=pd.read_csv('/content/dataset.csv')
print(df)

#dropping null values
df.dropna(how='all',axis=1,inplace=True)

#converting file to csv
df.to_csv('dataset.csv',index=False)

#reading the user input
dfr=pd.read_csv('/content/responses_schallenge.csv')

#converting to csv file
dfr.to_csv('responses_schallenge.csv')

#using csv module, read both the files
filef=open('dataset.csv','r')
filer=open('responses_schallenge.csv','r')

csvrf=csv.reader(filef)
csvrr=csv.reader(filer)

#extracting data from the dataset 
rowf=[]
for row in csvrf:
  rowf.append(row)

#extracting data from the user
rowr=[]
for row in csvrr:
  rowr.append(row)


#comparing the data from the dataset with the one given by the user
for x in rowf:
  for y in rowr:
    if x[1]==y[3]:
        expf=x[5]
        expr=y[5]

#converting string values to float
conv_expf=float(expf)
conv_expr=float(expr)

#comparing the required expense and the amount the user has specified
if(conv_expr<(0.5*conv_expf)):
  amount=conv_expf-conv_expr
  print('you need to invest ',amount,' more')
  print('no compatibility,please allocate more responses for the maintenance of the pet')
else:
  print('compatible,you may go ahead with the adoption!')
