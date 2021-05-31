# This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
import pandas as pd
import pickle
import shap
import streamlit.components.v1 as components
st.set_option('deprecation.showPyplotGlobalUse', False)

st.image('https://i.ibb.co/db33gwN/Screenshot-2021-05-09-at-11-15-13.png')

# Title
st.title('Covid-19 Reproduction Rate Estimator')
st.text('Check how Covid-19 spreads based on restrictions and other features (2 weeks time period)')

show_info = st.checkbox('Show Fields Description')
if show_info:
    st.subheader('Fields Description (Mean of 2 weeks)')
    st.markdown('**Reproduction Rate Week n-2**: Reproduction rate of week n-2')
    st.markdown('**Stay home requirements.**: Stay home requirements. No measures - 0, Recommended not to leave the house - 1, Required to not leave the house with exceptions for daily exercise, grocery shopping, and ‘essential’ trips - 2, Required to not leave the house with minimal exceptions (e.g. allowed to leave only once every few days, or only one person can leave at a time, etc.) – 3')
    st.markdown('**Restrictions in gatherings**: No restrictions - 0, Restrictions on very large gatherings (the limit is above 1000 people) - 1, Restrictions on gatherings between 100 to 1000 people - 2,  Restrictions on gatherings between 10 to 100 people - 3, Restrictions on gatherings of less than 10 people – 4')
    st.markdown('**Restrictions in internal movements**: No restrictions - 0, Recommend movement restriction - 1, Restrict movement – 2')
    st.markdown('**International travel controls**: No restrictions - 0, No measures - 0, Screening - 1, Quarantine from high-risk regions - 2, Ban on high-risk regions - 3, Total border closure – 4')
    st.markdown('**Close public transport**: No restrictions - 0, Recommended closing (or reduce volume) - 1, Required closing (or prohibit most using it) – 2')
    st.markdown('**Cancel public events**: No restrictions - 0, Recommended cancellations - 1, Required cancellations – 2')
    st.markdown('**Workplace closure**: No restrictions - 0, Recommended - 1, Required for some - 2, Required for all but key workers – 3')
    st.markdown('**School closures**: No restrictions - 0, Recommended - 1, Required (only at some levels) - 2, Required (all levels) - 3')
    st.markdown('**Accumulated cases**: Indicator of excess deaths up to date, indicator of population inmunity (0. None, 1-3. Low, 3-5. Medium, 5-7. High, 8-10. Very High)')
    st.markdown('**Economic Measures**: Governments support to debt relief and income support. (0. None, 1. Low, 2. Medium, 3. High)')
    st.markdown('**Closure Measures**: Governments closure of workplaces, school and cancelation of public events. (0. None, 1. Low, 2. Medium, 3. High)')
    st.markdown('**Holiday**: Number of holidays in the past week')
    st.markdown('**Temperature**: Temperature in celsius')
    st.markdown('**Precipitation**: Precipitation in mm/h')
    st.markdown('**Number of arrivals**: Tourism arrivals average (2015-2019)')
    st.markdown('**Urban Population**: Percentaje of the population that lives in urban areas')
    st.markdown('**Vaccinations**: Number of vaccine doses administered per 100')
    st.markdown('**Youth Unemployment**: Percentaje of youth unemployment')


st.sidebar.header('Specify Input Parameters')

def user_input_features():

    reproduction_rate_week_n2 = st.sidebar.number_input('Reproduction Rate Week n-2', min_value=0.0, max_value=4.5, step=0.1, value=1.0)
    stay_home_requirements = st.sidebar.slider('Stay home requirements',0, 4, 1)
    restriction_gatherings = st.sidebar.slider('Restrictions in gatherings',0, 2, 1)
    restrictions_internal_movements = st.sidebar.slider('Restrictions in internal movements',0, 4, 1)
    international_travel_controls = st.sidebar.slider('International travel controls',0, 2, 1)
    close_public_transport = st.sidebar.slider('Close public transport',0, 2, 1)
    cancel_public_events = st.sidebar.slider('Cancel public events',0, 3, 1)
    workplace_closures = st.sidebar.slider('Workplace closures',0, 3, 1)
    school_closures = st.sidebar.slider('School closures',0, 3, 1)
    accumulated = st.sidebar.slider('Accumulated', 0, 10, 3)
    temp = st.sidebar.slider('Temperature', -26, 40, 15)
    prcp = st.sidebar.slider('Precipitation', 0, 2, 0)
    economic_measures = st.sidebar.slider('Economic Measures',0, 3, 1)
    awareness_measures = st.sidebar.slider('Awareness Measures',0, 3, 1)
    holiday = st.sidebar.slider('Holiday', 0, 7, 0)
    number_of_arrivals = st.sidebar.slider('Number of arrivals', 121000, 82570000, 13284934)
    health_measures = st.sidebar.slider('Health Measures',0, 3, 1)
    youth_unemployment = st.sidebar.slider('Youth Unemployment',0, 35, 10)
    urban_population = st.sidebar.slider('Urban Population', 30, 100, 72)
    total_vaccinations_per_100 = st.sidebar.slider('Total Vaccinations per 100',0, 200, 0)
    
    data = {
            'awareness_measures': awareness_measures,
            'health_measures': health_measures,
            'mobility_closures_measures': 0.3*stay_home_requirements
                                + 0.3*restriction_gatherings\
                                + 0.2*restrictions_internal_movements\
                                + 0.1*international_travel_controls\
                                + 0.1*close_public_transport\
                                + 0.2*cancel_public_events\
                                + 0.4*workplace_closures\
                                + 0.4*school_closures,\
            'economic_measures': economic_measures,
            'holiday': holiday,
            'temp': temp,
            'prcp': prcp,
            'number_of_arrivals': number_of_arrivals,
            'urban_population': urban_population,
            'total_vaccinations_per_100': total_vaccinations_per_100,
            'youth_unemployment':youth_unemployment,
            'accumulated': accumulated/100,
            'reproduction_rate_week_n-2': reproduction_rate_week_n2}
    features = pd.DataFrame(data, index=[0])
    return features

s = user_input_features()

print(shap.__version__)

def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)

pickle_file = '../models/model_lgbm_reg_lags'
if st.sidebar.button('Calculate Estimated Reproduction Rate'):
    st.subheader('Specified Input parameters')
    st.text('Restrictions are grouped as \'mobility_closures_measures\' in the charts shown')
    st.write(s)
    model = pickle.load(open(pickle_file,'rb'))
    model_predict = (model.predict(s)).astype(str)
    st.markdown('**Estimated Reproduction Rate:**')
    st.write(model_predict[0])

    st.markdown('**Feature importance based on SHAP values**')
    explainerModel = shap.TreeExplainer(model)
    shap_values_Model = explainerModel.shap_values(s)
    st_shap(shap.force_plot(explainerModel.expected_value, shap_values_Model[0], s.iloc[[0]]), 125)
    shap.summary_plot(shap_values_Model, s, plot_type="bar")
    st.pyplot(bbox_inches='tight')


