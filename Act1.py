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
#data['occupation']=data['occupation'].map({' Exec-managerial':0, ' Machine-op-inspct':1, ' Protective-serv', ' ?', ' Armed-Forces', ' Other-service', ' Prof-specialty', ' Craft-repair', ' Tech-support', ' Transport-moving', ' Handlers-cleaners', ' Farming-fishing', ' Priv-house-serv', ' Sales', ' Adm-clerical'})
print(data.head())
print()
print("-------------------------------------------------")
print()

data.groupby('occupation').income.mean().plot(kind='bar')
plt.show()

