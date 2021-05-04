# This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Title
st.title('Covid-19 Forecast App')
st.text('Check how Covid-19 spreads weekly.')


show_info = st.checkbox('Show Fields Description')
if show_info:
	st.subheader('Fields Description (Mean of week)')
	st.markdown('**Bad Mobility**: Refers to the increase of visitors in retail and recreation, transit stations, grocery, pharmacy and workplaces.')
	st.markdown('**Good Mobility**: Refers to the increase of visitors in parks and time spent at home.')
	st.markdown('**Economic Measures**: Governments support to debt relief and income support. (1. Low, 2. Medium, 3. High)')
	st.markdown('**Health Measures**: Governments support to debt relief and income support. (1. Low, 2. Medium, 3. High)')
	st.markdown('**Mobility Measures**: Governments support to debt relief and income support. (1. Low, 2. Medium, 3. High)')
	st.markdown('**Holiday**: Number of holidays in the past week')
	st.markdown('**Temperature**: Temperature in celsius')
	st.markdown('**Precipitation**: Precipitation in mm')
	st.markdown('**Number of arrivals**: Toursim arrivals average (2015-2019)')
	st.markdown('**Urban Population**: Percentaje of the population that lives in urban areas')
	st.markdown('**Vaccinations**: Number of vaccine doses administered per 100')
	st.markdown('**Youth Unemployment**: Percentaje of youth unemployment')
	st.markdown('**Infections**: An indicator of the level of virality in the current week')
	st.markdown('**Accumulated cases**: Percentage of recovered individuals')


st.sidebar.header('Specify Input Parameters')

def user_input_features():
    bad_mobility = st.sidebar.slider('Bad Mobility', -100, 100, -20)
    good_mobility = st.sidebar.slider('Good Mobility', -100, 100, 10)
    government_economic_measures = st.sidebar.multiselect('Economic Measures', [0,1,2], 1)
    health_measures = st.sidebar.multiselect('Health Measures', [0,1,2], 1)
    mobility_measures = st.sidebar.multiselect('Mobility Measures', [0,1,2], 1)
    Holiday = st.sidebar.slider('Holiday', 0, 3, 0)
    temp = st.sidebar.slider('Temperature', -26, 40, 15)
    prcp = st.sidebar.slider('Precipitation', 0, 2, 0)
    number_of_arrivals = st.sidebar.slider('Number of arrivals', 121000, 82570000, 13284934)
    urban_population = st.sidebar.slider('Urban Population', 30, 100, 72)
    total_vaccinations_per_100 = st.sidebar.slider('Total Vaccinations per 100',0, 200, 0)
    youth_unemployment = st.sidebar.slider('Youth Unemployment',0, 35, 10)
    infected_rate = st.sidebar.slider('Infections', 0, 300, 10)
    accumulated = st.sidebar.slider('Accumulated', 0, 100, 5)
    data = {'bad_mobility': bad_mobility,
            'good_mobility': good_mobility,
            'government_economic_measures': government_economic_measures,
            'health_measures': health_measures*100,
            'mobility_measures': mobility_measures,
            'Holiday': Holiday,
            'temp': temp,
            'prcp': prcp,
            'number_of_arrivals': number_of_arrivals,
            'urban_population': urban_population,
            'total_vaccinations_per_100': total_vaccinations_per_100,
            'youth_unemployment':youth_unemployment,
            'infected_rate': infected_rate,
            'accumulated': accumulated}
    features = pd.DataFrame(data, index=[0])
    return features

s = user_input_features()

if st.sidebar.button('Enter Information'):
	st.subheader('Specified Input parameters')
	st.write(s)



