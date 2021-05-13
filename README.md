# Covid-19 Reproduction Rate Estimator
![Screenshot 2021-05-10 at 20 31 23](https://i.ibb.co/BLDbLqh/Screenshot-2021-05-10-at-18-39-00.png)

The following summary is to serve as reference and how to navigate through this repository. In order to find in detail documentation of this project please refer to document [memory.pdf](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/memory.pdf) found in this repository. 

The presented repository consists of the following folder and documents:
* [frontend](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/tree/main/frontend) - Contains applications developed.
* [models](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/tree/main/models) - Stored models generated using pickle.
* [notebooks](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/tree/main/notebooks) - Jupyter Notebooks for data preparation, analysis and evaluation.
* [memory.pdf](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/memory.pdf) - Full documentation and project description.
* [requirements.txt](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/requirements.txt) - Necessary libraries to run the code.

## Objective

The intention of the presented project is to estimate and understand how **restrictions, mobility trends, temperature, demographic and special characteristics of each country** affect the spread of Covid-19. Features included in the analysis can be grouped in different **category definitions** as shown below for better understanding.

|Mobility Factors|Population Virus Infections and Immunity Factors|Country Characteristics Factors|Political Measures Factors|
|---|---|---|---|
|<ul><li>retail_and_recreation</li><li>grocery_and_pharmacy</li><li>residential</li><li>transit_stations</li><li>parks</li><li>workplaces</li></ul>|<ul><li>infections_value</li><li>accumulated</li><li>total_vaccinations_per_100</li></ul>|<ul><li>temp</li><li>prcp</li><li>number_of_arrivals</li><li>urban_population</li><li>youth_unemployment</li><li>holiday</li></ul>|<ul><li>debt_relief</li><li>prcp</li><li>income_support</li><li>testing_policy</li><li>international_travel_controls</li><li>restrictions_internal_movements</li><li>close_public_transport</li><li>public_information_campaigns</li><li>facial_coverings</li><li>contact_tracing</li><li>stay_home_requirements</li><li>restriction_gatherings</li><li>cancel_public_events</li><li>workplace_closures</li><li>school_closures</li></ul>|

In order to achieve this, we will try to predict the **reproduction rate number** for each week in a set of 61 countries with data relative from **March 2020 till April 2021**. The value of **reproduction rate** has been retrieved from [Our World In Data](https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-codebook.csv) and the detail of how such value was calculated is detailed in [Arroyo Marioli et al. (2020)](https://doi.org/10.2139/ssrn.3581633), Central Bank of Chile and Humboldt University of Berlin. In general terms, reproduction rate estimates in average **how many infections may be caused by one infected individual**. Our approach for the presented problem is based on [SIR Model](https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model) which is a **standard used in epidemiology for disease spread in the population**, but we will include the effect and impact of mentioned features in order to understand how the spread of the virus behaves on different situations. 

## Notebooks

### Data Gathering and Preparation
* [00_weather_data.ipynb](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/notebooks/00_weather_data.ipynb) - Invokes NOAA Weather Data database using Google Big Query. Matches stations latitude and longitude with country codes using Google Maps API. Generates complete weather_data.csv file containing information of temperature and precipitation for all countries in 2020.
* [01_data_preparation.ipynb](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/notebooks/01_data_preparation.ipynb) - Collects and processes different files, each corresponding to restrictions, mobility indexes, excess mortality, weather data, tourism, urban population and youth unemployment. All data is processed and merged, generation of artifical variables and final dataset for processing and analysis.
### Exploratory Data Analysis
* [02_data_exploration.ipynb](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/notebooks/02_data_exploration.ipynb)  - Exploration and first analysis of features included in our dataset. 
### Data Modelling and Evaluation

Modelling and evaluation over approaches and models selected using two methodologies.
  * **Methodologies**
    1. Model 1: No Lag Methodology
    2. Model 2: Lag Methodology
    
  * **Three different data configuration approaches**
    1. Raw data.
    2. Feature Engineering grouping variables.
    3. Principal Component Analysis.
    
  * **Models:** XGB Regressor, LGBM Regressor, Gradient Boosting Regressor, KNN Regressor, Histogram Boosting Regressor, NuSVR Regressor.

#### Model 1: No Lag Methodology, feature explanatory
* [03_data_model_evaluation.ipynb](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/notebooks/03_data_model_evaluation.ipynb) - Modelling and evaluation of selected aproaches and models.
* [04_data_model_shap_values_eval.ipynb](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/notebooks/04_data_model_shap_values_eval.ipynb) - SHAP values analysis over best model and approach.

#### Model 2: Lag Methodology
* [03_data_model_evaluation_lags.ipynb](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/notebooks/03_data_model_evaluation_lags.ipynb) - Modelling and evaluation of selected aproaches and models.
* [04_data_model_shap_values_eval_lags.ipynb](https://github.com/lucasbotellaroca/Covid-19_Reproduction_Rate_Estimator/blob/main/notebooks/04_data_model_shap_values_eval_lags.ipynb) - SHAP values analysis over best model and approach.

## Streamlit applications
Two applications for two models presented have been developed:

* [covid19-app.py](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/covid19-app.py)
* [covid19-app-lags.py](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/covid19-app-lags.py)

To run apps execute from command line:

```cd frontend/streamlit```
```streamlit run covid19-app.py```

```cd frontend/streamlit```
```streamlit run covid19-app-lags.py```


![Screenshot 2021-05-13 at 08 52 08](https://user-images.githubusercontent.com/71489078/118089335-815b2f80-b3c8-11eb-848f-19665f385c9d.png)
The image shown refers to [covid19-app-lags.py](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/covid19-app-lags.py)

## Requirements

* To be able to execute notebooks it is required to have access to my Google Cloud Platform Project and a clients_secrets.json files, if not already conceded please contact me at lucasbotellaroca@gmail.com
* All libraries necessary to run this project are listed in file [requirements.txt](https://github.com/lucasbotellaroca/Death-Forecast-Models-Based-on-Political-Responses-COVID-19/blob/main/requirements.txt).
