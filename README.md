# Covid-19 Reproduction Rate Estimator
![Screenshot 2021-05-10 at 20 31 23](https://i.ibb.co/BLDbLqh/Screenshot-2021-05-10-at-18-39-00.png)

The following details is to serve as reference and how to navigate through this repository. In order to find in detail documentation please refer to document memory.pdf found in this repository. 

## Objective

The intention of the presented project is to estimate and understand how **restrictions, mobility trends, temperature, demographic and special characteristics of each country** affect the spread of Covid-19. Features included in the analysis can be grouped in different category definitions as shown below for better understanding.

|Mobility Factors|Population Virus Infections and Immunity Factors|Country Characteristics Factors|Political Measures Factors|
|---|---|---|---|
|<ul><li>retail_and_recreation</li><li>grocery_and_pharmacy</li><li>residential</li><li>transit_stations</li><li>parks</li><li>workplaces</li></ul>|<ul><li>infections_value</li><li>accumulated</li><li>total_vaccinations_per_100</li></ul>|<ul><li>temp</li><li>prcp</li><li>number_of_arrivals</li><li>urban_population</li><li>youth_unemployment</li><li>holiday</li></ul>|<ul><li>debt_relief</li><li>prcp</li><li>income_support</li><li>testing_policy</li><li>international_travel_controls</li><li>restrictions_internal_movements</li><li>close_public_transport</li><li>public_information_campaigns</li><li>facial_coverings</li><li>contact_tracing</li><li>stay_home_requirements</li><li>restriction_gatherings</li><li>cancel_public_events</li><li>workplace_closures</li><li>school_closures</li></ul>|

In order to achieve this, we will try to predict the **reproduction rate number** for each week in a set of 61 countries with data relative from **March 2020 till April 2021**. The value of **reproduction rate** has been retrieved from [Our World In Data](https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-codebook.csv) and the detail of how such value was calculated is detailed in [Arroyo Marioli et al. (2020)](https://doi.org/10.2139/ssrn.3581633), Central Bank of Chile and Humboldt University of Berlin. In general terms, reproduction rate estimates in average how many infections may be caused by one infected individual. Our approach for the presented problem is based on [SIR Model](https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model) which is a **standard used in epidemiology for disease spread in the population**, but we will include the effect and impact of mentioned features in order to understand its impact. 

## Notebooks

#### Data Gathering and Preparation
* [00_weather_data.ipynb](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/00_weather_data.ipynb) - Invokes NOAA Weather Data database using Google Big Query. Matches stations latitude and longitude with country codes using Google Maps API. Generates complete weather_data.csv file containing information of temperature and precipitation for all countries in 2020.
* [01_data_preparation.ipynb](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/01_data_preparation.ipynb) - Collects and processes different files, each corresponding to restrictions, mobility indexes, excess mortality, weather data, tourism, urban population and youth unemployment. All data is processed and merged, generation of artifical variables and final dataset for processing and analysis.
#### Exploratory Data Analysis
* [02_data_exploration.ipynb](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/02_data_exploration.ipynb)  - Exploration and first analysis of features included in our dataset. 
#### Data Modelling and Evaluation
* [03_data_model_evaluation.ipynb](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/03_data_model_evaluation.ipynb) - Modelling and evaluation over approaches and models selected.
  * Three different data configuration approaches.
    1. Raw data.
    2. Feature Engineering grouping variables.
    3. Principal Component Analysis.
  * Models: XGB Regressor, LGBM Regressor, Gradient Boosting Regressor, KNN Regressor, Histogram Boosting Regressor, NuSVR Regressor.
* [04_data_model_shap_values_eval.ipynb](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/04_data_model_shap_values_eval.ipynb) - Shap values analysis over best model and approach.
## Streamlit application
* [covid19-app.py](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/covid19-app.py)

To run the app, place the file covid19-app.py in same folder as the model file contained in this repo "model_lgbm_reg" and execute from command line:

```streamlit run covid19-app.py```


![Screenshot 2021-05-10 at 23 17 51](https://user-images.githubusercontent.com/71489078/117725777-f28ebd00-b1e5-11eb-9c63-978b197be3f8.png)

## Requirements

* To be able to execute notebooks it is required to have access to my Google Cloud Platform Project, if not conceded please contact me at lucasbotellaroca@gmail.com
* All libraries necessary to run this project are listed in file [requirements.txt](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/requirements.txt).
