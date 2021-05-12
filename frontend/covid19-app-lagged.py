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
st.text('Check how Covid-19 spreads based on features (2 weeks time period)')


show_info = st.checkbox('Show Fields Description')
if show_info:
	st.subheader('Fields Description (Mean of week)')
	st.markdown('**Mobility Index**: Refers to the increase or decrease of visitors in retail and recreation, transit stations, grocery, pharmacy and workplaces.')
	st.markdown('**Residential**: Refers to the increase or decrease time spent at home.')
	st.markdown('**Infections**: An indicator of the level of virality in the current week (0. None, 5. Low, 10. Medium, 15. High, 20-25. Very High)')
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
    mobility_closures_measures = st.sidebar.slider('Mobility Closure Measures',0, 6, 1)
    accumulated = st.sidebar.slider('Accumulated', 0, 10, 3)
    temp = st.sidebar.slider('Temperature', -26, 40, 15)
    infections_value = st.sidebar.slider('Infections', 0, 25, 4)
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
            'mobility_closures_measures': mobility_closures_measures,
            'economic_measures': economic_measures,
            'holiday': holiday,
            'temp': temp,
            'prcp': prcp,
            'number_of_arrivals': number_of_arrivals,
            'urban_population': urban_population,
            'total_vaccinations_per_100': total_vaccinations_per_100,
            'youth_unemployment':youth_unemployment,
            'infections_value': infections_value,
            'accumulated': accumulated/100,
            'reproduction_rate_week_n-2': reproduction_rate_week_n2}
    features = pd.DataFrame(data, index=[0])
    return features

s = user_input_features()

print(shap.__version__)

def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)

pickle_file = './model_lgbm_reg_lagged'
if st.sidebar.button('Calculate Estimated Reproduction Rate'):
    st.subheader('Specified Input parameters')
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


