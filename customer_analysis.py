import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#load the dataset
data =pd.read_csv(r'C:\Users\Akshara\Downloads\customer_data.csv')
#display the first row of the dataset
print('\nFirst 10 rows of the dataset:')
print(data.head(10))
#check for missing values
print('\nMissing values in each column:')
print(data.isnull().sum())
#dataset information
print('\nDataset Information:')
print(data.info())
#statistical summary of the dataset
print('\nStatistical summary of the dataset:')
print(data.describe())
#customer subscriptions per year
data['Year'] = pd.to_datetime(data['Subscription Date']).dt.year
joined_per_year=data['Year'].value_counts().sort_index()
print('\nNumber of customers subscribed per year:')
print(joined_per_year)
#plotting the number of customers subscribed per year
plt.figure(figsize=(10,6))
plt.bar(joined_per_year.index,joined_per_year.values,color='red')
plt.title('Number of customers subscribed per year')
plt.xlabel('Year')
plt.ylabel('Number of customers')
plt.xticks(joined_per_year.index)
plt.grid(True,linestyle='--',alpha=0.7)
plt.show()
# Number of customers by company
company_counts = data['Company'].value_counts().head(10)

print('\nTop Companies by Customer Count:')
print(company_counts)
#Plotting the top companies by customer count
plt.figure(figsize=(10,6))
plt.barh(company_counts.index,company_counts.values,color='blue')
plt.title('Top Companies by Customer Count')
plt.xlabel('Company')
plt.ylabel('Number of Customers')
plt.grid(True)
plt.gca().invert_yaxis() 
plt.tight_layout()
plt.show()

#Number of customers by country
country_counts=data['Country'].value_counts().head(10)
print('\nTop Countries by Customer Count:')
print(country_counts)
#Plotting the top countries by customer count
plt.figure(figsize=(10,6))
plt.barh(country_counts.index,country_counts.values,color='green')
plt.title('Top Countries by Customer Count')
plt.xlabel('Number of Customers')
plt.ylabel('Countries')
plt.grid(True)
plt.gca().invert_yaxis() 
plt.tight_layout()
plt.show()






