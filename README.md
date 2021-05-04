# Death Forecast Model Based on Political Decisions COVID-19

## 1. Project Statement and Approach

The intention of the presented project is to explain and understand how restrictions, mobility trends, temperature, demographic and special characteristics of each region affect the spread of Covid-19. In order to achieve this, we will try to predict the reproduction number for each week. We will refer to effective reproduction number or reproduction rate as Rt. Rt tells you the average number of people who will contract a contagious disease from one person with that disease. The basic reproduction number or R0 specifically applies to a population of people who were previously free of infection and haven’t been vaccinated, however for our specific case of study we will take into account people that have been vaccinated or that have contracted the disease in order to make our predictions more precise, therefore predicting Rt.

In general terms, as mentioned, Rt tells you in average how many infections may be caused by one infected individual, this of course is related with mobility trends, restrictions applied by governments and many other factors. 

•	If Rt < 1 one infected person will cause less than one infection. In this case the disease will eventually die out.
•	If Rt > 1 one infected person will cause more than one infection. In this case the disease will increase and eventually cause an outbreak or pandemic.
•	If Rt = 1 one infected person will cause one infection. In this case the disease will still be transmitted and there is a risk of outbreak or pandemic.

Coronavirus data specially cases and deaths reported by governments are not very trustworthy, especially in the toughest times of the epidemic. Taking this into account our proxy variable to detect possible infections will be the excess mortality recorded. Excess mortality is a measure of the excess number of deaths recorded in 2020 and 2021 in relation with previous years by week, such difference will of course, indicate us, the number of deaths caused by coronavirus disease, making the assumption that there are no other causes that may cause an excess of deaths.

Our approach for the presented problem is based on SIR model which is a standard used in epidemiology for a disease spread in the population. 

The standard SIR model in discrete times describes the reproduction rate of a virus based on three components referred as: susceptible (St), infected (It), and recovered (Rt) in time t. βt is the transmission rate, and γt is the transition rate from infected to recovered in time t
Note the difference between Rt which we refer as effective reproduction number and Rt which we refer to as recovered individuals in time t.

Let´s note that N  St + It + Rt. The original SIR problem is stated as shown below:
 

To simplify things, R0 is defined as for whatever defined time period as R0=β/γ. Rt is defined as shown in the equation below. It is referred to as the number of individuals infected in time t.
 
Rt therefore is a value that measures how the virus is increasing or decreasing in time. For our specific problem we will not try to exactly replicate this idea, but our dataset structure will be based on the equation system shown above. Key points taken from this model is that Rt is dependent of infections in the time period defined t, accumulated infections or recovered Rt, and for our specific case the restrictions applied. If all infected individuals were isolated from the rest of the population for γ time, then the disease would disappear.


Excess mortality is recorded weekly on Sundays, and that value is the sum of deaths in the deferred week. In this project we will take excess mortality as an indicator or proxy variable of both accumulated and recovered individuals together with infected individuals. Accumulated will be the sum of excess mortality in time t, such value is calculated by summing deaths for every country until time n. And infections will be estimated as the excess mortality recorded in day n+18. It has been recorded that the average time between a person contracting the virus and dying is 18 days (Verity et al., 2020).

As mentioned, excess mortality data is unfortunately retrieved weekly, hence, every entry in our dataset will be a week estimate of value Rt, which in the end makes our dataset smaller and more aggregated which may affect the results. 

Therefore, our problem is stated as shown below:

Restrictions = Restrictions applied by governments in week n.
Mobility Trend = Mobility trends provide by Google.
Others = Demographic and other variables unique for each country that may affect the spread of the disease.
Recovered = Accumulated excess deaths to week n.
Infected = Excess deaths in next 18 days.

Fweek n (Restrictions, Mobility Trends, Others, Recovered, Infected) = Rtweek n

Once the problem has been stated and what the approach will be for this project will firstly detail our sources of data, features, range of values and description.

## 2. Data Explanation and Preparation
Once the problem has been stated and what the approach will be for this
project will firstly detail our sources of data, features, range of
values and description.

Data has been gathered form different sources:

-   Our World in Data

    -   <https://ourworldindata.org/excess-mortality-covid>

    -   <https://ourworldindata.org/policy-responses-covid>

    -   <https://ourworldindata.org/grapher/international-tourism-number-of-arrivals>

    -   <https://ourworldindata.org/urbanization>

-   World Bank of Data

    -   https://data.worldbank.org/indicator/SH.MED.NUMW.P3

    -   <https://data.worldbank.org/indicator/SP.POP.65UP.TO.ZS>

    -   https://data.worldbank.org/indicator/SH.MED.BEDS.ZS

-   National Oceanic and Atmospheric Administration (NOAA) Us department
    of commerce.

    -   https://www.noaa.gov/

Below there is a diagram of how data was retrieved and transformed into the final dataset:
![Untitled Diagram](https://user-images.githubusercontent.com/71489078/116786549-87374380-aa9f-11eb-856b-a8d59816ad75.jpg)

The final table with detailed field description and type can be found below:
<table>
<thead>
<tr class="header">
<th><strong>Features used for the Analysis</strong></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Type</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><strong>Code</strong></td>
<td>String</td>
<td>Country in ISO 3166-1 alpha-2 Code</td>
</tr>
<tr class="odd">
<td><strong>Date</strong></td>
<td>Date</td>
<td>Date in yyyy-mm-dd format. Date contains only Sundays since it is grouped by week, all the rest of features are aggregated under this constraint.</td>
</tr>
<tr class="even">
<td><strong>retail_and_recreation</strong></td>
<td>Float</td>
<td><p>% Shows how the number of visitors to places of retail and recreation has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).</p>
<p>This includes places like restaurants, cafes, shopping centers, theme parks, museums, libraries, and movie theaters.</p>
<p>This index is smoothed to the rolling 7-day average.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>grocery_and_pharmacy</strong></td>
<td>Float</td>
<td><p>% Shows how the number of visitors to grocery and pharmacy stores has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).</p>
<p>This includes places like grocery markets, food warehouses, farmers markets, specialty food shops, drug stores, and pharmacies.</p>
<p>This index is smoothed to the rolling 7-day average.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>residential</strong></td>
<td>Float</td>
<td><p>% Shows how the number of visitors to residential areas has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).</p>
<p>This index is smoothed to the rolling 7-day average.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>transit_stations</strong></td>
<td>Float</td>
<td><p>% Shows how the number of visitors to transit stations has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).</p>
<p>This includes public transport hubs such as subway, bus, and train stations.</p>
<p>This index is smoothed to the rolling 7-day average.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>parks</strong></td>
<td>Float</td>
<td><p>% Shows how the number of visitors to parks and outdoor spaces has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).</p>
<p>This includes places like local parks, national parks, public beaches, marinas, dog parks, plazas, and public gardens.</p>
<p>This index is smoothed to the rolling 7-day average.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>workplaces</strong></td>
<td>Float</td>
<td><p>% Shows how the number of visitors to workplaces has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).</p>
<p>This index is smoothed to the rolling 7-day average.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>contact_tracing</strong></td>
<td>Integer</td>
<td><p>Government policies on contract tracing for COVID-19.</p>
<ul>
<li><p>No tracing – 0</p></li>
<li><p>Limited tracing (Only some cases) - 1</p></li>
<li><p>Comprehensive tracing (All cases) – 2</p></li>
</ul>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>testing_policy</strong></td>
<td>Integer</td>
<td><p>Government policies on testing for COVID-19. Note that this relates to PCR testing for the virus only; it does not include non-PCR, antibody testing.</p>
<ul>
<li><p>No testing policy- 0</p></li>
<li><p>Testing only for those who both (a) have symptoms AND (b) meet specific criteria (e.g. key workers, admitted to hospital, came into contact with a known case, returned from overseas) - 1</p></li>
<li><p>Testing of anyone showing COVID-19 symptoms - 2</p></li>
<li><p>Open public testing (e.g “drive through” testing available to asymptomatic people) – 3</p></li>
</ul>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>international_travel_controls</strong></td>
<td>Integer</td>
<td><p>Government policies on restrictions on international travel controls.</p>
<ul>
<li><p>No measures - 0</p></li>
<li><p>Screening - 1</p></li>
<li><p>Quarantine from high-risk regions - 2</p></li>
<li><p>Ban on high-risk regions - 3</p></li>
<li><p>Total border closure - 4</p></li>
</ul>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>restrictions_internal_movements</strong></td>
<td>Integer</td>
<td><p>Government policies on restrictions on internal movement/travel between regions and cities.</p>
<ul>
<li><p>No measures - 0</p></li>
<li><p>Recommend movement restriction - 1</p></li>
<li><p>Restrict movement – 2</p></li>
</ul>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>close_public_transport</strong></td>
<td>Integer</td>
<td><p>Government policies on public transport closures</p>
<ul>
<li><p>No measures - 0</p></li>
<li><p>Recommended closing (or reduce volume) - 1</p></li>
<li><p>Required closing (or prohibit most using it) – 2</p></li>
</ul>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>public_information_campaigns</strong></td>
<td>Integer</td>
<td><p>Public information campaigns on COVID-19.</p>
<ul>
<li><p>None – 0</p></li>
<li><p>Public officials urging caution – 1</p></li>
<li><p>Coordinated information campaign – 2</p></li>
</ul>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>facial_coverings</strong></td>
<td>Integer</td>
<td><p>Government policies on the use of face coverings outside-of-the-home.</p>
<p>Countries are grouped into five categories:</p>
<ul>
<li><p>No policy - 0</p></li>
<li><p>Recommended - 1</p></li>
<li><p>Required in some specified shared/public spaces outside the home with other people present, or some situations when social distancing not possible - 2</p></li>
<li><p>Required in all shared/public spaces outside the home with other people present or all situations when social distancing not possible - 3</p></li>
<li><p>Required outside the home at all times regardless of location or presence of other people – 4</p></li>
</ul>
<p>Note that there may be sub-national or regional differences in policies on face coverings. The policy categories shown may not apply at all sub-national levels. A country is coded based on its most stringent policy at the sub-national level.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>stay_home_requirements</strong></td>
<td>Integer</td>
<td><p>Government policies on stay-at-home requirements or household lockdowns.</p>
<ul>
<li><p>No measures - 0</p></li>
<li><p>Recommended not to leave the house - 1</p></li>
<li><p>Required to not leave the house with exceptions for daily exercise, grocery shopping, and ‘essential’ trips - 2</p></li>
<li><p>Required to not leave the house with minimal exceptions (e.g. allowed to leave only once every few days, or only one person can leave at a time, etc.) – 3</p></li>
</ul>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>restriction_gatherings</strong></td>
<td>Integer</td>
<td><p>Government policies on restrictions on public gatherings.</p>
<p>Countries are grouped into five categories:</p>
<ul>
<li><p>No restrictions - 0</p></li>
<li><p>Restrictions on very large gatherings (the limit is above 1000 people) - 1</p></li>
<li><p>Restrictions on gatherings between 100 to 1000 people - 2</p></li>
<li><p>Restrictions on gatherings between 10 to 100 people - 3</p></li>
<li><p>Restrictions on gatherings of less than 10 people – 4</p></li>
</ul>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>cancel_public_events</strong></td>
<td>Integer</td>
<td><p>Cancellation of public events.</p>
<p>No measures - 0</p>
<p>Recommended cancellations - 1</p>
<p>Required cancellations – 2</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>workplace_closures</strong></td>
<td>Integer</td>
<td><p>Government policies on workplaces closures.</p>
<p>No measures – 0</p>
<p>Recommended - 1</p>
<p>Required for some - 2</p>
<p>Required for all but key workers – 3</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>school_closures</strong></td>
<td>Integer</td>
<td><p>Government policies on school closures.</p>
<p>No measures - 0</p>
<p>Recommended - 1</p>
<p>Required (only at some levels) - 2</p>
<p>Required (all levels) - 3</p>
<p>Note that there may be sub-national or regional differences in policies on school closures. The policy categories shown may not apply at all sub-national levels. A country is coded as ‘required closures’ if at least some sub-national regions have required closures.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>debt_relief</strong></td>
<td>Integer</td>
<td><p>Governments provide debt or contract relief to citizens during the COVID-19 pandemic.</p>
<p>No relief – 0</p>
<p>Narrow relief – 1</p>
<p>Broad relief – 2</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>income_support</strong></td>
<td>Integer</td>
<td><p>Governments provide income support to workers during the COVID-19 pandemic.</p>
<p>No income support – 0</p>
<p>Covers &lt;50% of lost salary – 1</p>
<p>Covers &gt;50% of lost salary – 2</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>Holiday</strong></td>
<td>Integer</td>
<td><p>Number of holiday in the selected time period</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>temp</strong></td>
<td>Float</td>
<td><p>Average temperature in celsius of all stations in the selected time period.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>prcp</strong></td>
<td>Float</td>
<td><p>Average precipitation in Celsius of all stations in the selected time period</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>doctors_per_1000</strong></td>
<td>Float</td>
<td>Number of doctors per 1000 habitants last year recorded</td>
</tr>
<tr class="even">
<td><strong>nurses_per_1000</strong></td>
<td>Float</td>
<td>Number of nurses per 1000 habitants last year recorded</td>
</tr>
<tr class="odd">
<td><strong>beds_per_1000</strong></td>
<td>Float</td>
<td>Number of hospital beds per 1000 habitants last year recorded</td>
</tr>
<tr class="even">
<td><strong>number_of_arrivals</strong></td>
<td>Float</td>
<td>Number of tourism arrivals last year recorded</td>
</tr>
<tr class="odd">
<td><strong>urban_population</strong></td>
<td>Float</td>
<td>% of urban population last year recorded</td>
</tr>
<tr class="even">
<td><strong>total_vaccinations_per_100</strong></td>
<td>Float</td>
<td><p>Share of the total population that received at least one vaccine dose. This may not equal the shares that are fully vaccinated if the vaccine requires two doses.</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>%youth_unemployment_total</strong></td>
<td>Float</td>
<td>% of youthment unemployment last year recorded</td>
</tr>
<tr class="even">
<td><strong>life_expectancy</strong></td>
<td>Float</td>
<td>Average life expectancy at birth last year recorded</td>
</tr>
<tr class="odd">
<td><strong>%df_population_gr_65</strong></td>
<td>Float</td>
<td>% of population with age 65 or higher last year recorded</td>
</tr>
<tr class="even">
<td><strong>UN Population Division (Median Age) (2017)</strong></td>
<td>Float</td>
<td>Median age last year recorded</td>
</tr>
<tr class="odd">
<td><strong>Excess mortality P-scores, all ages Prev 36 days</strong></td>
<td>Float</td>
<td><p>Excess mortality is a term used in epidemiology and public health that refers to the number of deaths from all causes during a crisis above and beyond what we would have expected to see under ‘normal’ conditions.</p>
<p>P-score = 100* Deaths (2020-2021) - Avg.Deaths (2015-2019) / Avg.Deaths (2015-2019)</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-36<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>Excess mortality P-scores, all ages Prev 18 days</strong></td>
<td>Float</td>
<td><p>Excess mortality is a term used in epidemiology and public health that refers to the number of deaths from all causes during a crisis above and beyond what we would have expected to see under ‘normal’ conditions.</p>
<p>P-score = 100* Deaths (2020-2021) - Avg.Deaths (2015-2019) / Avg.Deaths (2015-2019)</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>Excess mortality P-scores, all ages Prev 7 days</strong></td>
<td>Float</td>
<td><p>Excess mortality is a term used in epidemiology and public health that refers to the number of deaths from all causes during a crisis above and beyond what we would have expected to see under ‘normal’ conditions.</p>
<p>P-score = 100* Deaths (2020-2021) - Avg.Deaths (2015-2019) / Avg.Deaths</p>
<p>(2015-2019)</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-7<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>Excess mortality P-scores, all ages</strong></td>
<td>Float</td>
<td><p>Excess mortality is a term used in epidemiology and public health that refers to the number of deaths from all causes during a crisis above and beyond what we would have expected to see under ‘normal’ conditions.</p>
<p>P-score = 100* Deaths (2020-2021) - Avg.Deaths (2015-2019) / Avg.Deaths (2015-2019)</p>
<p>In our dataset this value is calculated as the average in the selected week.</p></td>
</tr>
<tr class="odd">
<td><strong>average_deaths_2015_2019_all_ages</strong></td>
<td>Float</td>
<td>Average number of deaths in selected period for 2015-2019</td>
</tr>
<tr class="even">
<td><strong>deaths_prev_7</strong></td>
<td>Float</td>
<td><p>Raw number of deaths 7 days prior to selected period</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-7<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>deaths_prev_18</strong></td>
<td>Float</td>
<td><p>Raw number of deaths 18 days prior to selected period</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18<sup>th</sup> day.</p></td>
</tr>
<tr class="even">
<td><strong>deaths_prev_36</strong></td>
<td>Float</td>
<td><p>Raw number of deaths 36 days prior to selected period</p>
<p>In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-36<sup>th</sup> day.</p></td>
</tr>
<tr class="odd">
<td><strong>deaths</strong></td>
<td>Float</td>
<td><p>Raw number of deaths selected period</p>
<p>In our dataset this value is calculated as the average in the selected week.</p></td>
</tr>
<tr class="even">
<td><strong>accumulated</strong></td>
<td>Float</td>
<td>Accumulated percentage of deaths.</td>
</tr>
<tr class="odd">
<td><strong>R0</strong></td>
<td>Float</td>
<td></td>
</tr>
</tbody>
</table>
