###IMPORTS###
import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels as sm

###READ CSV FILES###
#File names: copy & paste file name in to df line (21)

#file = 'Kaggle_Data_Updated.csv' ##not needed b/c of below files
#file = 'allFruits_year.csv'
#file = 'allFruits.csv'
#file = 'allGrain_year.csv'
#file = 'allGrain.csv'
#file = 'r_county_Fruit_y.csv'
#file = 'r_country_Fruit.csv'
#file = 'r_country_Grain_y.csv'
#file = 'r_country_Grain.csv'
#file = 'merged_food_pop.csv'
#file = 'merged_feed_pop.csv'

df = pd.read_csv('merged_feed_pop.csv',encoding = 'latin1')


###SETUP FOR GRAPHICS###
#do not need bottom 2 for sorting
merged_food_subset = df.loc[df['Year']>1961]
merged_feed_subset = df.loc[df['Year']>1961]

###Top 10 stuff
#sorted_df = df.sort_values(by='Tons',ascending=False)
#result = sorted_df.head(10)
#print(result)

#Locate the specific country we want to analyze
#Replace the last word with the country we are using in both


countryName = 'United States'
Country = df.loc[df['Country']== countryName]
FeedCountry = df.loc[df['Country']== countryName]

corr = Country.corr() # use this in heatmap

###GRAPHICS###
sns.heatmap(corr, annot=True)
plt.title(str(countryName)+ ' Correlation')
plt.show()

sns.pairplot(Country)
plt.title(str(countryName)+ ' Pair Plot')
plt.show()

sns.regplot(Country['Year'],Country['FeedProduction'],fit_reg = True)
plt.title(str(countryName)+' Year v Tons of Feed Production')
plt.show()
