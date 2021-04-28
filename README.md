**Death Forecast Models Based on Political Responses COVID-19**

The intention of the presented project is to explain how restrictions, mobility trends, temperature, demographic and special characteristics of each country affect the spread of Covid-19. In order to achieve this we will try to predict variables such as R0 and excess mortality and afterwards analyze the coefficients of each variable included in the model and see its effect and magnitude.

The intention of the presented project is to explain how restrictions, mobility trends, temperature, demographic and special characteristics of each country affect the spread of Covid-19. In order to achieve this we will try to predict variables such as R0 and excess mortality and afterwards analyze the coefficients of each variable included in the model and see its effect and magnitude.

Data has been gathered form different sources:

- Our World in Data
  - [https://ourworldindata.org/policy-responses-covid](https://ourworldindata.org/policy-responses-covid)
  - [https://ourworldindata.org/excess-mortality-covid](https://ourworldindata.org/excess-mortality-covid)
  -
- World Bank of Data
- National Oceanic and Atmospheric Administration (NOAA) Us department of commerce.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Code** | String | Country in ISO 3166-1 alpha-2 code |
| **Date** | Date | Date in yyyy-mm-dd format. Date contains only Sundays since it is grouped by week, all the rest of features are aggregated under this constraint. |
| **retail\_and\_recreation**| Float | % Shows how the number of visitors to places of retail and recreation has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).
This includes places like restaurants, cafes, shopping centers, theme parks, museums, libraries, and movie theaters.
This index is smoothed to the rolling 7-day average.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **grocery\_and\_pharmacy**
 | Float | % Shows how the number of visitors to grocery and pharmacy stores has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).
This includes places like grocery markets, food warehouses, farmers markets, specialty food shops, drug stores, and pharmacies.
This index is smoothed to the rolling 7-day average.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **residential**
 | Float | % Shows how the number of visitors to residential areas has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).
This index is smoothed to the rolling 7-day average.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **transit\_stations**
 | Float | % Shows how the number of visitors to transit stations has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).
This includes public transport hubs such as subway, bus, and train stations.
This index is smoothed to the rolling 7-day average.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **parks**
 | Float | % Shows how the number of visitors to parks and outdoor spaces has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).
This includes places like local parks, national parks, public beaches, marinas, dog parks, plazas, and public gardens.
This index is smoothed to the rolling 7-day average.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **workplaces**
 | Float | % Shows how the number of visitors to workplaces has changed compared to baseline days (the median value for the 5‑week period from January 3 to February 6, 2020).
This index is smoothed to the rolling 7-day average.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **contact\_tracing**
 | Integer | Government policies on contract tracing for COVID-19.

- No tracing – 0
- Limited tracing (Only some cases) - 1
- Comprehensive tracing (All cases) – 2

In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **testing\_policy**
 | Integer | Government policies on testing for COVID-19. Note that this relates to PCR testing for the virus only; it does not include non-PCR, antibody testing.

- No testing policy- 0
- Testing only for those who both (a) have symptoms AND (b) meet specific criteria (e.g. key workers, admitted to hospital, came into contact with a known case, returned from overseas) - 1
- Testing of anyone showing COVID-19 symptoms - 2
- Open public testing (e.g &quot;drive through&quot; testing available to asymptomatic people) – 3

In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **international\_travel\_controls**
 | Integer | Government policies on restrictions on international travel controls.

- No measures - 0
- Screening - 1
- Quarantine from high-risk regions - 2
- Ban on high-risk regions - 3
- Total border closure - 4

In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **restrictions\_internal\_movements**
 | Integer | Government policies on restrictions on internal movement/travel between regions and cities.

- No measures - 0
- Recommend movement restriction - 1
- Restrict movement – 2

In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **close\_public\_transport**
 | Integer | Government policies on public transport closures
- No measures - 0
- Recommended closing (or reduce volume) - 1
- Required closing (or prohibit most using it) – 2

In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **public\_information\_campaigns**
 | Integer | Public information campaigns on COVID-19.

- None – 0
- Public officials urging caution – 1
- Coordinated information campaign – 2

In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **facial\_coverings**
 | Integer | Government policies on the use of face coverings outside-of-the-home.
Countries are grouped into five categories:

- No policy - 0
- Recommended - 1
- Required in some specified shared/public spaces outside the home with other people present, or some situations when social distancing not possible - 2
- Required in all shared/public spaces outside the home with other people present or all situations when social distancing not possible - 3
- Required outside the home at all times regardless of location or presence of other people – 4

Note that there may be sub-national or regional differences in policies on face coverings. The policy categories shown may not apply at all sub-national levels. A country is coded based on its most stringent policy at the sub-national level.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **stay\_home\_requirements**
 | Integer | Government policies on stay-at-home requirements or household lockdowns.

- No measures - 0
- Recommended not to leave the house - 1
- Required to not leave the house with exceptions for daily exercise, grocery shopping, and &#39;essential&#39; trips - 2
- Required to not leave the house with minimal exceptions (e.g. allowed to leave only once every few days, or only one person can leave at a time, etc.) – 3

In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **restriction\_gatherings**
 | Integer | Government policies on restrictions on public gatherings.
Countries are grouped into five categories:

- No restrictions - 0
- Restrictions on very large gatherings (the limit is above 1000 people) - 1
- Restrictions on gatherings between 100 to 1000 people - 2
- Restrictions on gatherings between 10 to 100 people - 3
- Restrictions on gatherings of less than 10 people – 4

In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **cancel\_public\_events**
 | Integer | Cancellation of public events.
No measures - 0Recommended cancellations - 1Required cancellations – 2
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **workplace\_closures**
 | Integer | Government policies on workplaces closures.
No measures – 0Recommended - 1Required for some - 2Required for all but key workers – 3
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **school\_closures**
 | Integer | Government policies on school closures.
No measures - 0Recommended - 1 Required (only at some levels) - 2Required (all levels) - 3

Note that there may be sub-national or regional differences in policies on school closures. The policy categories shown may not apply at all sub-national levels. A country is coded as &#39;required closures&#39; if at least some sub-national regions have required closures.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **debt\_relief**
 | Integer | Governments provide debt or contract relief to citizens during the COVID-19 pandemic.
No relief – 0Narrow relief – 1Broad relief – 2
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **income\_support**
 | Integer | Governments provide income support to workers during the COVID-19 pandemic.No income support – 0Covers \&lt;50% of lost salary – 1Covers \&gt;50% of lost salary – 2
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **Holiday**
 | Integer | Number of holiday in the selected time period
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **temp**
 | Float | Average temperature in celsius of all stations in the selected time period.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **prcp**
 | Float | Average precipitation in Celsius of all stations in the selected time period
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **doctors\_per\_1000**
 | Float | Number of doctors per 1000 habitants last year recorded
 |
| **nurses\_per\_1000**
 | Float | Number of nurses per 1000 habitants last year recorded
 |
| **beds\_per\_1000**
 | Float | Number of hospital beds per 1000 habitants last year recorded |
| **number\_of\_arrivals**
 | Float | Number of tourism arrivals last year recorded |
| **urban\_population**
 | Float | % of urban population last year recorde |
| **total\_vaccinations\_per\_100**
 | Float | Share of the total population that received at least one vaccine dose. This may not equal the share that are fully vaccinated if the vaccine requires two doses.
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **%youth\_unemployment\_total**
 | Float | % of youthment unemployment last year recorded |
| **life\_expectancy**
 | Float | Average life expectancy at birth last year recorded |
| **%df\_population\_gr\_65**
 | Float | % of population with age 65 or higher last year recorded |
| **UN Population Division (Median Age) (2017)**
 | Float | Median age last year recorded |
| **Excess mortality P-scores, all ages Prev 36 days**
 | Float | Excess mortality is a term used in epidemiology and public health that refers to the number of deaths from all causes during a crisis above and beyond what we would have expected to see under &#39;normal&#39; conditions.
P-score = 100\* Deaths (2020-2021) - Avg.Deaths (2015-2019) / Avg.Deaths (2015-2019)
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-36th day.
 |
| **Excess mortality P-scores, all ages Prev 18 days**
 | Float | Excess mortality is a term used in epidemiology and public health that refers to the number of deaths from all causes during a crisis above and beyond what we would have expected to see under &#39;normal&#39; conditions.
P-score = 100\* Deaths (2020-2021) - Avg.Deaths (2015-2019) / Avg.Deaths (2015-2019)
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **Excess mortality P-scores, all ages Prev 7 days**
 | Float | Excess mortality is a term used in epidemiology and public health that refers to the number of deaths from all causes during a crisis above and beyond what we would have expected to see under &#39;normal&#39; conditions.
P-score = 100\* Deaths (2020-2021) - Avg.Deaths (2015-2019) / Avg.Deaths (2015-2019)
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-7th day.
 |
| **Excess mortality P-scores, all ages**
 | Float | Excess mortality is a term used in epidemiology and public health that refers to the number of deaths from all causes during a crisis above and beyond what we would have expected to see under &#39;normal&#39; conditions.
P-score = 100\* Deaths (2020-2021) - Avg.Deaths (2015-2019) / Avg.Deaths (2015-2019)
In our dataset this value is calculated as the average in the selected week.
 |
| **average\_deaths\_2015\_2019\_all\_ages**
 | Float | Average number of deaths in selected period for 2015-2019 |
| **deaths\_prev\_7**
 | Float | Raw number of deaths 7 days prior to selected period
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-7th day.
 |
| **deaths\_prev\_18**
 | Float | Raw number of deaths 18 days prior to selected period
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-18th day.
 |
| **deaths\_prev\_36**
 | Float | Raw number of deaths 36 days prior to selected period
In our dataset this value is calculated as the average in the selected week. For each day we retrieve the value of this same feature in the n-36th day.
 |
| **deaths**
 | Float | Raw number of deaths selected period
In our dataset this value is calculated as the average in the selected week.
 |
| **accumulated**
 | Float | Accumulated percentage of deaths.
 |
| **R0**
 | Float |
 |
