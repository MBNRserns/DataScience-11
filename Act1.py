import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("adult.csv")
data.columns=['age','workclass','ID','education','educational-num','marital-status','occupation','relationship','race','gender','capital-gain','capital-loss','hours-per-week','native-country','income']
data.rename(columns={'capital-gain':'capital gain','capital-loss':'capital loss','native-country':'country','hours-per-week':'hours per week','marital-status':'marital status'}, inplace=True)
print(data.info())
print()
print("-------------------------------------------------")
print()

print(data.isin(['?']).sum(axis=0))
print()
print("-------------------------------------------------")
print()

data.drop(['educational-num','age', 'hours per week', 'ID', 'capital gain','capital loss', 'country'], axis=1, inplace=True)
print(data.head())
print()
print("-------------------------------------------------")
print()

#Income
income=set(data['income'])
print(income)
print()
print()
data['income']=data['income'].map({' <=50K':0, ' >50K': 1}).astype(int)
print(data.head())
print()
print("-------------------------------------------------")
print()

#Gender
gender=set(data['gender'])
print(gender)
print()
print()
data['gender']=data['gender'].map({' Male':0, ' Female': 1}).astype(int)
print(data.head())
print()
print("-------------------------------------------------")
print()

data.groupby('gender').income.mean().plot(kind='bar')
plt.show()

#Race
race=set(data['race'])
print(race)
print()
print()
data['race']=data['race'].map({' Asian-Pac-Islander':0, ' White':1, ' Black':2, ' Amer-Indian-Eskimo':3, ' Other':4}).astype(int)
print(data.head())
print()
print("-------------------------------------------------")
print()

data.groupby('race').income.mean().plot(kind='bar')
plt.show()

#Relationship
relationship=set(data['relationship'])
print(relationship)
print()
print()
data['relationship']=data['relationship'].map({' Own-child':0, ' Wife':1, ' Husband':2, ' Not-in-family':3, ' Other-relative':4, ' Unmarried':5})
print(data.head())
print()
print("-------------------------------------------------")
print()

data.groupby('relationship').income.mean().plot(kind='bar')
plt.show()

#Occupation
occupation=set(data['occupation'])
print(occupation)
print()
print()
data['occupation']=data['occupation'].map({' Exec-managerial':0, ' Machine-op-inspct':1, ' Protective-serv':2, ' ?':3, ' Armed-Forces':4, ' Other-service':5, ' Prof-specialty':6, ' Craft-repair':7, ' Tech-support':8, ' Transport-moving':9, ' Handlers-cleaners':10, ' Farming-fishing':11, ' Priv-house-serv':12, ' Sales':13, ' Adm-clerical':14})
print(data.head())
print()
print("-------------------------------------------------")
print()

data.groupby('occupation').income.mean().plot(kind='bar')
plt.show()

#Marital Status
marital_status=set(data['marital status'])
print(marital_status)
print()
print()
data['marital status']=data['marital status'].map({' Widowed':0, ' Never-married':1, ' Married-spouse-absent':2, ' Divorced':3, ' Married-AF-spouse':4, ' Separated':5, ' Married-civ-spouse':6})
print(data.head())
print()
print("-------------------------------------------------")
print()

data.groupby('marital status').income.mean().plot(kind='bar')
plt.show()

#Education
education=set(data['education'])
print(education)
print()
print()
data['education']=data['education'].map({' 11th':0, ' 12th':1, ' Preschool':2, ' 1st-4th':3, ' Some-college':4, ' 9th':5, ' Assoc-voc':6, ' Prof-school':7, ' Masters':8, ' Bachelors':9, ' 5th-6th':10, ' 7th-8th':11, ' HS-grad':12, ' Assoc-acdm':13, 'Doctorate':14, ' 10th':15})
print(data.head())
print()
print("-------------------------------------------------")
print()

data.groupby('education').income.mean().plot(kind='bar')
plt.show()

#Workclass
workclass=set(data['workclass'])
print(workclass)
print()
print()
data['workclass']=data['workclass'].map({' Local-gov':0, ' ?':1, ' Federal-gov':2, ' Self-emp-inc':3, ' Self-emp-not-inc':4, ' Private':5, ' Without-pay':6, ' Never-worked':7, ' State-gov':8})
print(data.head())
print()
print("-------------------------------------------------")
print()

data.groupby('workclass').income.mean().plot(kind='bar')
plt.show()

