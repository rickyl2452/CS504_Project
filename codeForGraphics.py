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

#define global variables here

#converting files to list so you could use all of them as needed if that is what you intend.
# also if you have all of these in one path we could leverage that too.

files = ['allFruits_year.csv','allFruits.csv','allGrain_year.csv','allGrain_year.csv','r_county_Fruit_y.csv',
         'r_country_Fruit.csv','r_country_Grain_y.csv','r_country_Grain.csv','merged_food_pop.csv','merged_feed_pop.csv']

#Change to your path where you have your file ensure to paste after the 'r' and in between the quotation marks
countryFile = r'C:\Users\ricky\Documents\Mason MS DAEN\CS504_Project\countrylist.xlsx'

# where you are saving your visualizations
savePath = r'C:\Users\ricky\Documents\Mason MS DAEN\CS504_Project\{}'

# your main DF you are using although if you are gonna use multiple files i could loop this too
# also i just used a full path because i was running this code in my python terminal and not an IDE (was using intelliJ)


#df = pd.read_csv('merged_feed_pop.csv',encoding = 'latin1')

df = pd.read_csv(r'C:\Users\ricky\Documents\Mason MS DAEN\CS504_Project\merged_feed_pop.csv') #this can be a loop too with the list above


###SETUP FOR GRAPHICS###
#do not need bottom 2 for sorting
merged_food_subset = df.loc[df['Year']>1961]
merged_feed_subset = df.loc[df['Year']>1961]


# function that grabs the countries of interest from a csv file
def grab_countries(PathToSource):
    #Read your source file into a data frame or however you want to read it in i had under xlsx
    # when i downloaded it from sheets
    countriesSheet = pd.read_excel(PathToSource)
    #I assumed this was the column you wanted but you can change it to any column you want
    countries = countriesSheet['Countries to collect Food']
    return countries







###Top 10 stuff
#sorted_df = df.sort_values(by='Tons',ascending=False)
#result = sorted_df.head(10)
#print(result)

#Locate the specific country we want to analyze
#Replace the last word with the country we are using in both

## this function calls the other function above to grab the country names
## It then loops through that list and for each country sets the Subset of the df, sns heatmap, pairplot and reg
## viz and then saves it to your local drive. it makes sure it closes the plot too after its done to avoid overlap.
def vizCreator():
    countryNames = grab_countries(countryFile) #calling the other function to get the list
    for country in countryNames: #main loop that will do everything
        Country = df.loc[df['Country']== country]
        #FeedCountry = df.loc[df['Country']== country] # you can uncomment this if you need it but it looked like duplicate
        if Country.empty:
            print(country + ' is not in dataFrame you are working with') # you could also add the file name here
        else:
            ## HeatMap Viz
            corr = Country.corr() # use this in heatmap
            sns.heatmap(corr, annot=True)
            plt.title(str(country)+ ' Correlation')
            #plt.show() You dont need this if its going to save
            plt.savefig(savePath.format(country +'heatMap.png'),format = 'png') #this saves the figure to your path defined above
            plt.close()
            
            #Same thing as above but Pairplot Viz
            sns.pairplot(Country)
            plt.title(str(country)+ ' Pair Plot')
            #plt.show()
            plt.savefig(savePath.format(country +'PairPlot.png'),format = 'png')
            plt.close()
            
            #RegressionPlot Viz
            sns.regplot(x=Country['Year'],y=Country['FeedProduction'],fit_reg = True)
            plt.title(str(country)+' Year v Tons of Feed Production')
            #plt.show()
            plt.savefig(savePath.format(country +'Reg.png'),format = 'png')
            plt.close()

def main(): #just making it the classic python structure
    vizCreator()


if __name__ == "__main__":
    main()
    

## Ran this script like you would any other script 'python <filename.py>' from my local terminal. It should also run
## from your IDE too.



## Left this here for reference.
###GRAPHICS###
# sns.heatmap(corr, annot=True)
# plt.title(str(countryName)+ ' Correlation')
# plt.show()
#
# sns.pairplot(Country)
# plt.title(str(countryName)+ ' Pair Plot')
# plt.show()
#
# sns.regplot(Country['Year'],Country['FeedProduction'],fit_reg = True)
# plt.title(str(countryName)+' Year v Tons of Feed Production')
# plt.show()
