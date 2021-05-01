**Death Forecast Model Based on Political Decisions COVID-19**

Lucas Botella Roca

The intention of the presented project is to explain how restrictions,
mobility trends, temperature, demographic and special characteristics of
each region affect the spread of Covid-19. In order to achieve this, we
will try to predict the reproduction number (R0) for each week. R0 tells
you the average number of people who will contract a contagious disease
from one person with that disease. It specifically applies to a
population of people who were previously free of infection and haven't
been vaccinated, however for our specific case of study we will take
into account people that have been vaccinated or that have contracted
the disease in order to make our predictions more precise.

In general terms, as mentioned, R0 tells you in average how many
infections may be caused by one infected individual, this of course is
related with the restrictions applied by governments.

-   If R0 \< 1 one infected person will cause less than one infection.
    In this case the disease will eventually die out.

-   If R0 \> 1 one infected person will cause more than one infection.
    In this case the disease will increase and eventually cause an
    outbreak or pandemic.

-   If R0 = 1 one infected person will cause one infection. In this case
    the disease will still be transmitted and there is a risk of
    outbreak or pandemic.

Coronavirus data specially cases and deaths reported by governments are
not very trustworthy, especially in the toughest times of the epidemic.
Taking this into account our proxy variable to detect possible
infections will be the excess mortality recorded. Excess mortality is a
measure of the excess number of deaths recorded in 2020 and 2021 in
relation with previous years by week, such difference will of course,
indicate us, the number of deaths caused by coronavirus disease, making
the assumption that there are no other causes that may cause an excess
of deaths.

As mentioned, excess mortality data is unfortunately retrieved weekly,
which in the end makes our dataset smaller and more aggregated which may
affect the results. It has been recorded that the average time between a
person contracting the virus and dying is 18.5 days, therefore, in our
dataset, we will associate restrictions of n-18 days with the deaths
occurred in day 18, in other words, the restrictions applied that day
allowed a number of x deaths 18 days later.

Excess mortality is recorded weekly on Sundays, and that value is the
sum of deaths in the deferred week. What we will do is take the average
value of restrictions, mobility trends and other features (detailed in
table Features used for the Analysis) associated to days of the referred
week. In the calendar below there is a scheme for better understanding:

+---------+---------+---------+---------+---------+---------+---------+
| **M     | **Tu    | **Wedn  | **Thu   | **F     | **Sat   | **S     |
| onday** | esday** | esday** | rsday** | riday** | urday** | unday** |
+=========+=========+=========+=========+=========+=========+=========+
| **25**  | **26**  | **27**  | **28**  | **29**  | **30**  | **31**  |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         | **R0    |
|         |         |         |         |         |         | p       |
|         |         |         |         |         |         | revious |
|         |         |         |         |         |         | 28      |
|         |         |         |         |         |         | days**  |
+---------+---------+---------+---------+---------+---------+---------+
| **1**   | **2**   | **3**   | **4**   | **5**   | **6**   | **7**   |
|         |         |         |         |         |         |         |
|         |         |         |         | 1       | 2       | 3       |
+---------+---------+---------+---------+---------+---------+---------+
| **8**   | **9**   | **10**  | **11**  | **12**  | **13**  | **14**  |
|         |         |         |         |         |         |         |
| 4       | 5       | 6       | 7       |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| **15**  | **16**  | **17**  | **18**  | **19**  | **20**  | **21**  |
+---------+---------+---------+---------+---------+---------+---------+
| **22**  | **23**  | **24**  | **25**  | **26**  | **27**  | **28**  |
|         |         |         |         |         |         |         |
| 1       | 2       | 3       | 4       | 5       | 6       | **R0 to |
|         |         |         |         |         |         | pr      |
|         |         |         |         |         |         | edict** |
|         |         |         |         |         |         |         |
|         |         |         |         |         |         | 7       |
+---------+---------+---------+---------+---------+---------+---------+

As seen day 22 of the referred month contains the tag "1" since it is
related with day "5" of the referred month. Every entry of our dataset
will contain the average value of restriction/mobility/other of days
\[1,7\] of the days marked in grey.

Once the problem has been stated and what the approach will be for this
project will firstly detail our sources of data, features, range of
values and description.

Data has been gathered form different sources:

-   Our World in Data

    -   <https://ourworldindata.org/excess-mortality-covid>

    -   <https://ourworldindata.org/policy-responses-covid>

    -   <https://ourworldindata.org/grapher/international-tourism-number-of-arrivals>

    -   <https://ourworldindata.org/urbanization>

    -   

-   World Bank of Data

    -   https://data.worldbank.org/indicator/SH.MED.NUMW.P3

    -   <https://data.worldbank.org/indicator/SP.POP.65UP.TO.ZS>

    -   https://data.worldbank.org/indicator/SH.MED.BEDS.ZS

-   National Oceanic and Atmospheric Administration (NOAA) Us department
    of commerce.

    -   https://www.noaa.gov/

+----------------------------+----------+----------------------------+
| **Features used for the    |          |                            |
| Analysis**                 |          |                            |
+============================+==========+============================+
| **Name**                   | **Type** | **Description**            |
+----------------------------+----------+----------------------------+
| **Code**                   | String   | Country in ISO 3166-1      |
|                            |          | alpha-2 Code               |
+----------------------------+----------+----------------------------+
| **Date**                   | Date     | Date in yyyy-mm-dd format. |
|                            |          | Date contains only Sundays |
|                            |          | since it is grouped by     |
|                            |          | week, all the rest of      |
|                            |          | features are aggregated    |
|                            |          | under this constraint.     |
+----------------------------+----------+----------------------------+
| **retail_and_recreation**  | Float    | \% Shows how the number of |
|                            |          | visitors to places of      |
|                            |          | retail and recreation has  |
|                            |          | changed compared to        |
|                            |          | baseline days (the median  |
|                            |          | value for the 5‑week       |
|                            |          | period from January 3 to   |
|                            |          | February 6, 2020).         |
|                            |          |                            |
|                            |          | This includes places like  |
|                            |          | restaurants, cafes,        |
|                            |          | shopping centers, theme    |
|                            |          | parks, museums, libraries, |
|                            |          | and movie theaters.        |
|                            |          |                            |
|                            |          | This index is smoothed to  |
|                            |          | the rolling 7-day average. |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **grocery_and_pharmacy**   | Float    | \% Shows how the number of |
|                            |          | visitors to grocery and    |
|                            |          | pharmacy stores has        |
|                            |          | changed compared to        |
|                            |          | baseline days (the median  |
|                            |          | value for the 5‑week       |
|                            |          | period from January 3 to   |
|                            |          | February 6, 2020).         |
|                            |          |                            |
|                            |          | This includes places like  |
|                            |          | grocery markets, food      |
|                            |          | warehouses, farmers        |
|                            |          | markets, specialty food    |
|                            |          | shops, drug stores, and    |
|                            |          | pharmacies.                |
|                            |          |                            |
|                            |          | This index is smoothed to  |
|                            |          | the rolling 7-day average. |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **residential**            | Float    | \% Shows how the number of |
|                            |          | visitors to residential    |
|                            |          | areas has changed compared |
|                            |          | to baseline days (the      |
|                            |          | median value for the       |
|                            |          | 5‑week period from January |
|                            |          | 3 to February 6, 2020).    |
|                            |          |                            |
|                            |          | This index is smoothed to  |
|                            |          | the rolling 7-day average. |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **transit_stations**       | Float    | \% Shows how the number of |
|                            |          | visitors to transit        |
|                            |          | stations has changed       |
|                            |          | compared to baseline days  |
|                            |          | (the median value for the  |
|                            |          | 5‑week period from January |
|                            |          | 3 to February 6, 2020).    |
|                            |          |                            |
|                            |          | This includes public       |
|                            |          | transport hubs such as     |
|                            |          | subway, bus, and train     |
|                            |          | stations.                  |
|                            |          |                            |
|                            |          | This index is smoothed to  |
|                            |          | the rolling 7-day average. |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **parks**                  | Float    | \% Shows how the number of |
|                            |          | visitors to parks and      |
|                            |          | outdoor spaces has changed |
|                            |          | compared to baseline days  |
|                            |          | (the median value for the  |
|                            |          | 5‑week period from January |
|                            |          | 3 to February 6, 2020).    |
|                            |          |                            |
|                            |          | This includes places like  |
|                            |          | local parks, national      |
|                            |          | parks, public beaches,     |
|                            |          | marinas, dog parks,        |
|                            |          | plazas, and public         |
|                            |          | gardens.                   |
|                            |          |                            |
|                            |          | This index is smoothed to  |
|                            |          | the rolling 7-day average. |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **workplaces**             | Float    | \% Shows how the number of |
|                            |          | visitors to workplaces has |
|                            |          | changed compared to        |
|                            |          | baseline days (the median  |
|                            |          | value for the 5‑week       |
|                            |          | period from January 3 to   |
|                            |          | February 6, 2020).         |
|                            |          |                            |
|                            |          | This index is smoothed to  |
|                            |          | the rolling 7-day average. |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **contact_tracing**        | Integer  | Government policies on     |
|                            |          | contract tracing for       |
|                            |          | COVID-19.                  |
|                            |          |                            |
|                            |          | -   No tracing -- 0        |
|                            |          |                            |
|                            |          | -   Limited tracing (Only  |
|                            |          |     some cases) - 1        |
|                            |          |                            |
|                            |          | -   Comprehensive tracing  |
|                            |          |     (All cases) -- 2       |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **testing_policy**         | Integer  | Government policies on     |
|                            |          | testing for COVID-19. Note |
|                            |          | that this relates to PCR   |
|                            |          | testing for the virus      |
|                            |          | only; it does not include  |
|                            |          | non-PCR, antibody testing. |
|                            |          |                            |
|                            |          | -   No testing policy- 0   |
|                            |          |                            |
|                            |          | -   Testing only for those |
|                            |          |     who both (a) have      |
|                            |          |     symptoms AND (b) meet  |
|                            |          |     specific criteria      |
|                            |          |     (e.g. key workers,     |
|                            |          |     admitted to hospital,  |
|                            |          |     came into contact with |
|                            |          |     a known case, returned |
|                            |          |     from overseas) - 1     |
|                            |          |                            |
|                            |          | -   Testing of anyone      |
|                            |          |     showing COVID-19       |
|                            |          |     symptoms - 2           |
|                            |          |                            |
|                            |          | -   Open public testing    |
|                            |          |     (e.g "drive through"   |
|                            |          |     testing available to   |
|                            |          |     asymptomatic people)   |
|                            |          |     -- 3                   |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **inter                    | Integer  | Government policies on     |
| national_travel_controls** |          | restrictions on            |
|                            |          | international travel       |
|                            |          | controls.                  |
|                            |          |                            |
|                            |          | -   No measures - 0        |
|                            |          |                            |
|                            |          | -   Screening - 1          |
|                            |          |                            |
|                            |          | -   Quarantine from        |
|                            |          |     high-risk regions - 2  |
|                            |          |                            |
|                            |          | -   Ban on high-risk       |
|                            |          |     regions - 3            |
|                            |          |                            |
|                            |          | -   Total border closure - |
|                            |          |     4                      |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **restric                  | Integer  | Government policies on     |
| tions_internal_movements** |          | restrictions on internal   |
|                            |          | movement/travel between    |
|                            |          | regions and cities.        |
|                            |          |                            |
|                            |          | -   No measures - 0        |
|                            |          |                            |
|                            |          | -   Recommend movement     |
|                            |          |     restriction - 1        |
|                            |          |                            |
|                            |          | -   Restrict movement -- 2 |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **close_public_transport** | Integer  | Government policies on     |
|                            |          | public transport closures  |
|                            |          |                            |
|                            |          | -   No measures - 0        |
|                            |          |                            |
|                            |          | -   Recommended closing    |
|                            |          |     (or reduce volume) - 1 |
|                            |          |                            |
|                            |          | -   Required closing (or   |
|                            |          |     prohibit most using    |
|                            |          |     it) -- 2               |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **publ                     | Integer  | Public information         |
| ic_information_campaigns** |          | campaigns on COVID-19.     |
|                            |          |                            |
|                            |          | -   None -- 0              |
|                            |          |                            |
|                            |          | -   Public officials       |
|                            |          |     urging caution -- 1    |
|                            |          |                            |
|                            |          | -   Coordinated            |
|                            |          |     information campaign   |
|                            |          |     -- 2                   |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **facial_coverings**       | Integer  | Government policies on the |
|                            |          | use of face coverings      |
|                            |          | outside-of-the-home.       |
|                            |          |                            |
|                            |          | Countries are grouped into |
|                            |          | five categories:           |
|                            |          |                            |
|                            |          | -   No policy - 0          |
|                            |          |                            |
|                            |          | -   Recommended - 1        |
|                            |          |                            |
|                            |          | -   Required in some       |
|                            |          |     specified              |
|                            |          |     shared/public spaces   |
|                            |          |     outside the home with  |
|                            |          |     other people present,  |
|                            |          |     or some situations     |
|                            |          |     when social distancing |
|                            |          |     not possible - 2       |
|                            |          |                            |
|                            |          | -   Required in all        |
|                            |          |     shared/public spaces   |
|                            |          |     outside the home with  |
|                            |          |     other people present   |
|                            |          |     or all situations when |
|                            |          |     social distancing not  |
|                            |          |     possible - 3           |
|                            |          |                            |
|                            |          | -   Required outside the   |
|                            |          |     home at all times      |
|                            |          |     regardless of location |
|                            |          |     or presence of other   |
|                            |          |     people -- 4            |
|                            |          |                            |
|                            |          | Note that there may be     |
|                            |          | sub-national or regional   |
|                            |          | differences in policies on |
|                            |          | face coverings. The policy |
|                            |          | categories shown may not   |
|                            |          | apply at all sub-national  |
|                            |          | levels. A country is coded |
|                            |          | based on its most          |
|                            |          | stringent policy at the    |
|                            |          | sub-national level.        |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **stay_home_requirements** | Integer  | Government policies on     |
|                            |          | stay-at-home requirements  |
|                            |          | or household lockdowns.    |
|                            |          |                            |
|                            |          | -   No measures - 0        |
|                            |          |                            |
|                            |          | -   Recommended not to     |
|                            |          |     leave the house - 1    |
|                            |          |                            |
|                            |          | -   Required to not leave  |
|                            |          |     the house with         |
|                            |          |     exceptions for daily   |
|                            |          |     exercise, grocery      |
|                            |          |     shopping, and          |
|                            |          |     'essential' trips - 2  |
|                            |          |                            |
|                            |          | -   Required to not leave  |
|                            |          |     the house with minimal |
|                            |          |     exceptions (e.g.       |
|                            |          |     allowed to leave only  |
|                            |          |     once every few days,   |
|                            |          |     or only one person can |
|                            |          |     leave at a time, etc.) |
|                            |          |     -- 3                   |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **restriction_gatherings** | Integer  | Government policies on     |
|                            |          | restrictions on public     |
|                            |          | gatherings.                |
|                            |          |                            |
|                            |          | Countries are grouped into |
|                            |          | five categories:           |
|                            |          |                            |
|                            |          | -   No restrictions - 0    |
|                            |          |                            |
|                            |          | -   Restrictions on very   |
|                            |          |     large gatherings (the  |
|                            |          |     limit is above 1000    |
|                            |          |     people) - 1            |
|                            |          |                            |
|                            |          | -   Restrictions on        |
|                            |          |     gatherings between 100 |
|                            |          |     to 1000 people - 2     |
|                            |          |                            |
|                            |          | -   Restrictions on        |
|                            |          |     gatherings between 10  |
|                            |          |     to 100 people - 3      |
|                            |          |                            |
|                            |          | -   Restrictions on        |
|                            |          |     gatherings of less     |
|                            |          |     than 10 people -- 4    |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **cancel_public_events**   | Integer  | Cancellation of public     |
|                            |          | events.                    |
|                            |          |                            |
|                            |          | No measures - 0            |
|                            |          |                            |
|                            |          | Recommended cancellations  |
|                            |          | - 1                        |
|                            |          |                            |
|                            |          | Required cancellations --  |
|                            |          | 2                          |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **workplace_closures**     | Integer  | Government policies on     |
|                            |          | workplaces closures.       |
|                            |          |                            |
|                            |          | No measures -- 0           |
|                            |          |                            |
|                            |          | Recommended - 1            |
|                            |          |                            |
|                            |          | Required for some - 2      |
|                            |          |                            |
|                            |          | Required for all but key   |
|                            |          | workers -- 3               |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **school_closures**        | Integer  | Government policies on     |
|                            |          | school closures.           |
|                            |          |                            |
|                            |          | No measures - 0            |
|                            |          |                            |
|                            |          | Recommended - 1            |
|                            |          |                            |
|                            |          | Required (only at some     |
|                            |          | levels) - 2                |
|                            |          |                            |
|                            |          | Required (all levels) - 3  |
|                            |          |                            |
|                            |          | Note that there may be     |
|                            |          | sub-national or regional   |
|                            |          | differences in policies on |
|                            |          | school closures. The       |
|                            |          | policy categories shown    |
|                            |          | may not apply at all       |
|                            |          | sub-national levels. A     |
|                            |          | country is coded as        |
|                            |          | 'required closures' if at  |
|                            |          | least some sub-national    |
|                            |          | regions have required      |
|                            |          | closures.                  |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **debt_relief**            | Integer  | Governments provide debt   |
|                            |          | or contract relief to      |
|                            |          | citizens during the        |
|                            |          | COVID-19 pandemic.         |
|                            |          |                            |
|                            |          | No relief -- 0             |
|                            |          |                            |
|                            |          | Narrow relief -- 1         |
|                            |          |                            |
|                            |          | Broad relief -- 2          |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **income_support**         | Integer  | Governments provide income |
|                            |          | support to workers during  |
|                            |          | the COVID-19 pandemic.     |
|                            |          |                            |
|                            |          | No income support -- 0     |
|                            |          |                            |
|                            |          | Covers \<50% of lost       |
|                            |          | salary -- 1                |
|                            |          |                            |
|                            |          | Covers \>50% of lost       |
|                            |          | salary -- 2                |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **Holiday**                | Integer  | Number of holiday in the   |
|                            |          | selected time period       |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **temp**                   | Float    | Average temperature in     |
|                            |          | celsius of all stations in |
|                            |          | the selected time period.  |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **prcp**                   | Float    | Average precipitation in   |
|                            |          | Celsius of all stations in |
|                            |          | the selected time period   |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **doctors_per_1000**       | Float    | Number of doctors per 1000 |
|                            |          | habitants last year        |
|                            |          | recorded                   |
+----------------------------+----------+----------------------------+
| **nurses_per_1000**        | Float    | Number of nurses per 1000  |
|                            |          | habitants last year        |
|                            |          | recorded                   |
+----------------------------+----------+----------------------------+
| **beds_per_1000**          | Float    | Number of hospital beds    |
|                            |          | per 1000 habitants last    |
|                            |          | year recorded              |
+----------------------------+----------+----------------------------+
| **number_of_arrivals**     | Float    | Number of tourism arrivals |
|                            |          | last year recorded         |
+----------------------------+----------+----------------------------+
| **urban_population**       | Float    | \% of urban population     |
|                            |          | last year recorded         |
+----------------------------+----------+----------------------------+
| **to                       | Float    | Share of the total         |
| tal_vaccinations_per_100** |          | population that received   |
|                            |          | at least one vaccine dose. |
|                            |          | This may not equal the     |
|                            |          | shares that are fully      |
|                            |          | vaccinated if the vaccine  |
|                            |          | requires two doses.        |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **%                        | Float    | \% of youthment            |
| youth_unemployment_total** |          | unemployment last year     |
|                            |          | recorded                   |
+----------------------------+----------+----------------------------+
| **life_expectancy**        | Float    | Average life expectancy at |
|                            |          | birth last year recorded   |
+----------------------------+----------+----------------------------+
| **%df_population_gr_65**   | Float    | \% of population with age  |
|                            |          | 65 or higher last year     |
|                            |          | recorded                   |
+----------------------------+----------+----------------------------+
| **UN Population Division   | Float    | Median age last year       |
| (Median Age) (2017)**      |          | recorded                   |
+----------------------------+----------+----------------------------+
| **Excess mortality         | Float    | Excess mortality is a term |
| P-scores, all ages Prev 36 |          | used in epidemiology and   |
| days**                     |          | public health that refers  |
|                            |          | to the number of deaths    |
|                            |          | from all causes during a   |
|                            |          | crisis above and beyond    |
|                            |          | what we would have         |
|                            |          | expected to see under      |
|                            |          | 'normal' conditions.       |
|                            |          |                            |
|                            |          | P-score = 100\* Deaths     |
|                            |          | (2020-2021) - Avg.Deaths   |
|                            |          | (2015-2019) / Avg.Deaths   |
|                            |          | (2015-2019)                |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-36^th^ day.              |
+----------------------------+----------+----------------------------+
| **Excess mortality         | Float    | Excess mortality is a term |
| P-scores, all ages Prev 18 |          | used in epidemiology and   |
| days**                     |          | public health that refers  |
|                            |          | to the number of deaths    |
|                            |          | from all causes during a   |
|                            |          | crisis above and beyond    |
|                            |          | what we would have         |
|                            |          | expected to see under      |
|                            |          | 'normal' conditions.       |
|                            |          |                            |
|                            |          | P-score = 100\* Deaths     |
|                            |          | (2020-2021) - Avg.Deaths   |
|                            |          | (2015-2019) / Avg.Deaths   |
|                            |          | (2015-2019)                |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **Excess mortality         | Float    | Excess mortality is a term |
| P-scores, all ages Prev 7  |          | used in epidemiology and   |
| days**                     |          | public health that refers  |
|                            |          | to the number of deaths    |
|                            |          | from all causes during a   |
|                            |          | crisis above and beyond    |
|                            |          | what we would have         |
|                            |          | expected to see under      |
|                            |          | 'normal' conditions.       |
|                            |          |                            |
|                            |          | P-score = 100\* Deaths     |
|                            |          | (2020-2021) - Avg.Deaths   |
|                            |          | (2015-2019) / Avg.Deaths   |
|                            |          |                            |
|                            |          | (2015-2019)                |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-7^th^ day.               |
+----------------------------+----------+----------------------------+
| **Excess mortality         | Float    | Excess mortality is a term |
| P-scores, all ages**       |          | used in epidemiology and   |
|                            |          | public health that refers  |
|                            |          | to the number of deaths    |
|                            |          | from all causes during a   |
|                            |          | crisis above and beyond    |
|                            |          | what we would have         |
|                            |          | expected to see under      |
|                            |          | 'normal' conditions.       |
|                            |          |                            |
|                            |          | P-score = 100\* Deaths     |
|                            |          | (2020-2021) - Avg.Deaths   |
|                            |          | (2015-2019) / Avg.Deaths   |
|                            |          | (2015-2019)                |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week.                      |
+----------------------------+----------+----------------------------+
| **average_d                | Float    | Average number of deaths   |
| eaths_2015_2019_all_ages** |          | in selected period for     |
|                            |          | 2015-2019                  |
+----------------------------+----------+----------------------------+
| **deaths_prev_7**          | Float    | Raw number of deaths 7     |
|                            |          | days prior to selected     |
|                            |          | period                     |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-7^th^ day.               |
+----------------------------+----------+----------------------------+
| **deaths_prev_18**         | Float    | Raw number of deaths 18    |
|                            |          | days prior to selected     |
|                            |          | period                     |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-18^th^ day.              |
+----------------------------+----------+----------------------------+
| **deaths_prev_36**         | Float    | Raw number of deaths 36    |
|                            |          | days prior to selected     |
|                            |          | period                     |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week. For each day we      |
|                            |          | retrieve the value of this |
|                            |          | same feature in the        |
|                            |          | n-36^th^ day.              |
+----------------------------+----------+----------------------------+
| **deaths**                 | Float    | Raw number of deaths       |
|                            |          | selected period            |
|                            |          |                            |
|                            |          | In our dataset this value  |
|                            |          | is calculated as the       |
|                            |          | average in the selected    |
|                            |          | week.                      |
+----------------------------+----------+----------------------------+
| **accumulated**            | Float    | Accumulated percentage of  |
|                            |          | deaths.                    |
+----------------------------+----------+----------------------------+
| **R0**                     | Float    |                            |
+----------------------------+----------+----------------------------+
