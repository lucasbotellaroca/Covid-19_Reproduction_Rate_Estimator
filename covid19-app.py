# This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
import pandas as pd
import pickle
import shap
import streamlit.components.v1 as components
st.set_option('deprecation.showPyplotGlobalUse', False)

# Title
st.title('Covid-19 Forecast App')
st.text('Check how Covid-19 spreads weekly based on features')


show_info = st.checkbox('Show Fields Description')
if show_info:
	st.subheader('Fields Description (Mean of week)')
	st.markdown('**Mobility Index**: Refers to the increase or decrease of visitors in retail and recreation, transit stations, grocery, pharmacy and workplaces.')
	st.markdown('**Residential**: Refers to the increase or decrease time spent at home.')
	st.markdown('**Awareness Measures**: Governments action on facial coverings and public information campaigns. (0. None, 1. Low, 2. Medium, 3. High, 4.Very high)')
	st.markdown('**Economic Measures**: Governments support to debt relief and income support. (0. None, 1. Low, 2. Medium, 3. High)')
	st.markdown('**Health Measures**: Governments action on contact tracing and testing policies (0. None, 1. Low, 2. Medium, 3. High)')
	st.markdown('**Mobility Measures**: Governments restrictions in gatherings, lockdowns, restriction in internal movements, close public transport. (0. None, 1. Low, 2. Medium, 3. High)')
	st.markdown('**Closure Measures**: Governments closure of workplaces, school and cancelation of public events. (0. None, 1. Low, 2. Medium, 3. High)')
	st.markdown('**Holiday**: Number of holidays in the past week')
	st.markdown('**Temperature**: Temperature in celsius')
	st.markdown('**Precipitation**: Precipitation in mm/h')
	st.markdown('**Number of arrivals**: Tourism arrivals average (2015-2019)')
	st.markdown('**Urban Population**: Percentaje of the population that lives in urban areas')
	st.markdown('**Vaccinations**: Number of vaccine doses administered per 100')
	st.markdown('**Youth Unemployment**: Percentaje of youth unemployment')
	st.markdown('**Infections**: An indicator of the level of virality in the current week')
	st.markdown('**Accumulated cases**: Percentage of recovered individuals')


st.sidebar.header('Specify Input Parameters')

def user_input_features():
    mobility_index = st.sidebar.slider('Bad Mobility', -100, 100, -20)
    residential = st.sidebar.slider('Residential', -100, 100, 10)
    awareness_measures = st.sidebar.slider('Awareness Measures', 0, 4, 1)
    health_measures = st.sidebar.slider('Health Measures', 0, 3, 1)
    mobility_measures = st.sidebar.slider('Mobility Measures',0, 3, 1)
    economic_measures = st.sidebar.slider('Economic Measures',0, 3, 1)
    closure_measures = st.sidebar.slider('Closure Measures',0, 3, 1)
    holiday = st.sidebar.slider('Holiday', 0, 7, 0)
    temp = st.sidebar.slider('Temperature', -26, 40, 15)
    prcp = st.sidebar.slider('Precipitation', 0, 2, 0)
    number_of_arrivals = st.sidebar.slider('Number of arrivals', 121000, 82570000, 13284934)
    urban_population = st.sidebar.slider('Urban Population', 30, 100, 72)
    total_vaccinations_per_100 = st.sidebar.slider('Total Vaccinations per 100',0, 200, 0)
    youth_unemployment = st.sidebar.slider('Youth Unemployment',0, 35, 10)
    infections_value = st.sidebar.slider('Infections', 0, 200, 20)
    accumulated = st.sidebar.slider('Accumulated', 0, 100, 5)
    data = {'mobility_index': mobility_index,
            'residential': residential,
            'awareness_measures': awareness_measures,
            'health_measures': health_measures,
            'mobility_measures': mobility_measures,
            'economic_measures': economic_measures,
            'closure_measures': closure_measures,
            'holiday': holiday,
            'temp': temp,
            'prcp': prcp,
            'number_of_arrivals': number_of_arrivals,
            'urban_population': urban_population,
            'total_vaccinations_per_100': total_vaccinations_per_100,
            'youth_unemployment':youth_unemployment,
            'infections_value': infections_value,
            'accumulated': accumulated/100}
    features = pd.DataFrame(data, index=[0])
    return features

s = user_input_features()

print(shap.__version__)

def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)

pickle_file = './model_hist_reg'
scaler_file = './scaler'
if st.sidebar.button('Calculate Estimated Reproduction Rate'):
	st.subheader('Specified Input parameters')
	st.write(s)
	scaler = pickle.load(open(scaler_file,'rb'))
	df_scaled=pd.DataFrame(scaler.transform(s), columns=s.columns)
	model = pickle.load(open(pickle_file,'rb'))
	model_predict = (model.predict(df_scaled)).astype(str)
	st.markdown('**Estimated Reproduction Rate:**')
	st.write(model_predict[0])

	st.markdown('**Feature importance based on SHAP values**')
	explainerModel = shap.TreeExplainer(model)
	shap_values_Model = explainerModel.shap_values(df_scaled)
	st_shap(shap.force_plot(explainerModel.expected_value, shap_values_Model[0], df_scaled.iloc[[0]]), 125)
	shap.summary_plot(shap_values_Model, s, plot_type="bar")
	st.pyplot(bbox_inches='tight')


