# Death Forecast Models Based on Political Responses COVID-19

## 1. Project Approach

The intention of the presented project is to explain how restrictions, mobility trends, temperature, demographic and special characteristics of each region affect the spread of Covid-19. In order to achieve this, we will try to predict the reproduction number (R0) for each week. R0 tells you the average number of people who will contract a contagious disease from one person with that disease. It specifically applies to a population of people who were previously free of infection and haven’t been vaccinated, however for our specific case of study we will take into account people that have been vaccinated or that have contracted the disease in order to make our predictions more precise.

In general terms, as mentioned, R0 tells you in average how many infections may be caused by one infected individual, this of course is related with the restrictions applied by governments. 

•	If **R0 < 1** one infected person will cause less than one infection. In this case the disease will eventually die out.

•	If **R0 > 1** one infected person will cause more than one infection. In this case the disease will increase and eventually cause an outbreak or pandemic.

•	If **R0 = 1** one infected person will cause one infection. In this case the disease will still be transmitted and there is a risk of outbreak or pandemic.

Coronavirus data specially cases and deaths reported by governments are not very trustworthy, especially in the toughest times of the epidemic. Taking this into account our proxy variable to detect possible infections will be the excess mortality recorded. Excess mortality is a measure of the excess number of deaths recorded in 2020 and 2021 in relation with previous years by week, such difference will of course, indicate us, the number of deaths caused by coronavirus disease, making the assumption that there are no other causes that may cause an excess of deaths.

As mentioned, excess mortality data is unfortunately retrieved weekly, which in the end makes our dataset smaller and more aggregated which may affect the results. It has been recorded that the average time between a person contracting the virus and dying is 18.5 days, therefore, in our dataset, we will associate restrictions of n-18 days with the deaths occurred in day 18, in other words, the restrictions applied that day allowed a number of x deaths 18 days later. 

Excess mortality is recorded weekly on Sundays, and that value is the sum of deaths in the deferred week. What we will do is take the average value of restrictions, mobility trends and other features (detailed in table Features used for the Analysis) associated to days of the referred week. In the calendar below there is a scheme for better understanding:

![Screenshot 2021-05-01 at 09 48 25](https://user-images.githubusercontent.com/71489078/116775255-61d81480-aa62-11eb-87b6-b3d4636b8724.png)

As seen day 22 of the referred month contains the tag “1” since it is related with day “5” of the referred month. Every entry of our dataset will contain the average value of restriction/mobility/other of days [1,7] of the days marked in grey.

Once the problem has been stated and what the approach will be for this project will firstly detail our sources of data, features, range of values and description.

Data has been gathered form different sources:
-	Our World in Data
o	https://ourworldindata.org/excess-mortality-covid
o	https://ourworldindata.org/policy-responses-covid
o	https://ourworldindata.org/grapher/international-tourism-number-of-arrivals
o	https://ourworldindata.org/urbanization
o	
-	World Bank of Data
o	https://data.worldbank.org/indicator/SH.MED.NUMW.P3
o	https://data.worldbank.org/indicator/SP.POP.65UP.TO.ZS
o	https://data.worldbank.org/indicator/SH.MED.BEDS.ZS

-	National Oceanic and Atmospheric Administration (NOAA) Us department of commerce. 
o	https://www.noaa.gov/
