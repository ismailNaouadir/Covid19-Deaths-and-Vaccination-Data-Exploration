import numpy as np
import pandas as pd

covid_df = pd.read_csv('CovidDeaths.csv')
vacc_df = pd.read_csv('CovidVaccinations.csv')

# Building table 1
total_cases = covid_df['new_cases'].sum()
total_deaths = covid_df['new_deaths'].sum()
death_percentage = total_deaths / total_cases * 100

d = {'total_cases': total_cases, 'total_deaths': total_deaths, 'death_percentage': death_percentage}
table_1 = pd.DataFrame(data=d, index=[0])

table_1.to_csv('table1.csv', index=False, encoding='utf-8')

del total_cases, total_deaths, death_percentage, d

# Building table 2
# continent is null
d = covid_df[covid_df['continent'] != covid_df['continent']]

unique_location = []
for i in d['location']:
    if i not in ['World', 'European Union', 'International']:
        if i not in unique_location:
            unique_location.append(i)

TotalDeathCount = []
for i in unique_location:
    TotalDeathCount.append(d[d['location'] == str(i)]['new_deaths'].sum())

table_2 = pd.DataFrame()
table_2['location'] = unique_location
table_2['totalDeathCount'] = TotalDeathCount

table_2.to_csv('table2.csv', index=False, encoding='utf-8')

del d, unique_location, TotalDeathCount

# Building table 3
location = covid_df['location'].unique()

population = []
for i in location:
    population.append(covid_df[covid_df['location'] == str(i)]['population'].unique()[0])


highestInfectionCount = []
for i in location:
    highestInfectionCount.append(covid_df[covid_df['location'] == str(i)]['total_cases'].max())

percentPopulationInfected = []
for i, j in zip(population, highestInfectionCount):
    percentPopulationInfected.append(j*100/i)

table_3 = pd.DataFrame()
table_3['location'] = location
table_3['population'] = population
table_3['highestInfectionCount'] = highestInfectionCount
table_3['percentPopulationInfected'] = percentPopulationInfected
table_3 = table_3.fillna(0)
table_3 = table_3.sort_values(by=['percentPopulationInfected'], ascending=False)
table_3.to_csv('table3.csv', index=False, encoding='utf-8')

del location, population, highestInfectionCount, percentPopulationInfected

# Building table 4
percentPopulationInfected = []
for i, j in zip(covid_df['population'], covid_df['total_cases']):
    percentPopulationInfected.append(j*100/i)

table_4 = pd.DataFrame()
table_4['location'] = covid_df['location']
table_4['population'] = covid_df['population']
table_4['date'] = covid_df['date']
table_4['highestInfectionCount'] = covid_df['total_cases']
table_4['percentPopulationInfected'] = percentPopulationInfected
table_4 = table_4.fillna(0)
table_4 = table_4.sort_values(by=['percentPopulationInfected'], ascending=False)
table_4.to_csv('table4.csv', index=False, encoding='utf-8')

