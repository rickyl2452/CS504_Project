#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:44:26 2020

@author: Team Gamma
"""

# Import Modules needed

import pandas as pd
import numpy as np
import seaborn as sns

# Read in two tables needed for analysis

#food and agriculture read in
fao = pd.read_csv("FAO.csv",encoding = 'latin1')

#census table read in
census = pd.read_excel("Census_Cleaned.xlsx")

#read in top 11 countries for food and feed
top11feed = pd.read_csv("wide_Top_11_Feed_yr.csv")

top11food = pd.read_csv("wide_Top_11_Food_yr.csv")


# This is me just checking that it imported correctly
top11food.head(4)
top11feed.head(4)
census.head(4)

# When trying to merge I realize the country names for US and China were different
# So It was easier to change it in the Top11 table as opposed to later
census.loc[census['Abbv Country']== 'US'] # Checking to see what its called in census
census.loc[census['Abbv Country']=='CH']

top11food = top11food.rename(columns ={"United States of America": "United States", "China, mainland": "China"})

# Grabbing Country names to use for the transpose
columns = top11food.columns.tolist()
countries = columns[2:]
print(countries) #Validating I got it right

#Converting to a long table with the country easier for the join later.
top11food_long = top11food.melt(id_vars = ['Element', 'Year'],
                                value_vars= countries, var_name = 'Country',value_name = 'FoodProduction')


# merging the data for food so we get population per year :D
merged_food = pd.merge(top11food_long, census[['Country','Year', 'Population']], on = ['Country','Year'], how = 'left')


#Plotting the data first population over the years then production over the years
sns.lineplot(data=merged_food, x=merged_food['Year'], y=merged_food['Population'], hue=merged_food['Country'])

sns.lineplot(data=merged_food, x=merged_food['Year'], y=merged_food['FoodProduction'], hue=merged_food['Country'])

### This was just to export out the completed table for further analysis so we wouldn't have to repeat the steps above.
merged_food.to_csv('merged_food_pop.csv', index=False, encoding='utf-8')


#Repeat steps above but for feed
top11feed = top11feed.rename(columns ={"United States of America": "United States", "China, mainland": "China"})
columns = top11feed.columns.tolist()
countries = columns[2:]
print(countries) #Validating I got it right

top11feed_long = top11feed.melt(id_vars = ['Element', 'Year'],
                                value_vars= countries, var_name = 'Country',value_name = 'FeedProduction')

merged_feed = pd.merge(top11feed_long, census[['Country','Year', 'Population']], on = ['Country','Year'], how = 'left')

sns.lineplot(data=merged_feed, x=merged_feed['Year'], y=merged_feed['Population'], hue=merged_feed['Country'])

sns.lineplot(data=merged_feed, x=merged_feed['Year'], y=merged_feed['FeedProduction'], hue=merged_feed['Country'])

### This was just to export out the completed table for further analysis so we wouldn't have to repeat the steps above.
merged_feed.to_csv('merged_feed_pop.csv', index=False, encoding='utf-8')

### This next part was us messing with what statistics we wanted to show from the meeting

## This is just creating a subset of the main merged_food_subset where its only grabbing years after 2009
merged_food_subset = merged_food.loc[merged_food['Year']>2009]
merged_feed_subset = merged_feed.loc[merged_feed['Year']>2009]

#This was just pulling one country that we tried to visualize to use for later stats
italy = merged_food.loc[merged_food['Country']=='Italy']

#playing around with correlations and heatmaps with just italy
corr = italy.corr() # correlation matrix without grouping
corrCountries = merged_food_subset.groupby('Country').corr() #correlation matrix of all coutnries

sns.heatmap(corr, annot=True) # Heatmap with above corr for just italy

sns.pairplot(italy) # pairplot of Italy over all the years

sns.pairplot(italy.loc[italy['Year']>2002]) # PairPlot of Italy over the last ten years.
