# This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
import pandas as pd
import pickle
import shap
import streamlit.components.v1 as components
st.set_option('deprecation.showPyplotGlobalUse', False)

st.image('https://i.ibb.co/BLDbLqh/Screenshot-2021-05-10-at-18-39-00.png')

# Title
st.title('Covid-19 Reproduction Rate Estimator')
st.text('Check how Covid-19 spreads every two weeks based on features. Most influential features appear above.')


show_info = st.checkbox('Show Fields Description')
if show_info:

    st.subheader('Fields Description (Mean of 2 weeks)')
    st.markdown('**Infections**: An indicator of the level of virality in the current week.')
    st.markdown('**Accumulated cases**: Indicator of excess deaths up to date, indicator of population inmunity')
    st.markdown('**Mobility Index**: Refers to the increase or decrease of visitors in retail and recreation, transit stations, grocery, pharmacy and workplaces.')
    st.markdown('**Economic Measures**: Governments support to debt relief and income support.')
    st.markdown('**Residential**: Refers to the increase or decrease time spent at home.')
    st.markdown('**Temperature**: Temperature in celsius.')
    st.markdown('**Closure Measures**: Governments closure of workplaces, school and cancelation of public events.')
    st.markdown('**Awareness Measures**: Governments action on facial coverings and publicinformation campaigns.')
    st.markdown('**Number of arrivals**: Tourism arrivals average (2015-2019).')
    st.markdown('**Youth Unemployment**: Percentaje of youth unemployment.')
    st.markdown('**Urban Population**: Percentaje of the population that lives in urban areas.')
    st.markdown('**Health Measures**: Governments action on contact tracing and testing policy.')
    st.markdown('**Precipitation**: Precipitation in mm/h.')
    st.markdown('**Mobility and Closures Measures**: Governments action on limiting mobility and closing workplaces and schools.')
    st.markdown('**Vaccinations**: Number of vaccine doses administered per 100 people.')
    st.markdown('**Holiday**: Number of holidays in the past week.')
	
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    infections_value = st.sidebar.slider('Infections', 0, 400, 18)
    accumulated = st.sidebar.slider('Accumulated', 0, 30, 4)
    mobility_index = st.sidebar.slider('Mobility Index', -85, 50, -20)
    economic_measures = st.sidebar.slider('Economic Measures',0, 2, 1)
    residential = st.sidebar.slider('Residential', -8, 39, 10)
    temp = st.sidebar.slider('Temperature', -19, 36, 15)
    awareness_measures = st.sidebar.slider('Awareness Measures', 0, 4, 2)
    number_of_arrivals = st.sidebar.slider('Number of arrivals', 121000, 82570000, 13284934)
    urban_population = st.sidebar.slider('Urban Population', 30, 100, 72)
    mobility_closures_measures = st.sidebar.slider('Mobility and Closures Measures', 0, 6, 2)
    youth_unemployment = st.sidebar.slider('Youth Unemployment',0, 35, 10)
    health_measures = st.sidebar.slider('Health Measures', 0, 3, 2)
    prcp = st.sidebar.slider('Precipitation', 0, 2, 0)
    holiday = st.sidebar.slider('Holiday', 0, 7, 0)
    total_vaccinations_per_100 = st.sidebar.slider('Total Vaccinations per 100',0, 200, 0)
 
    data = {'mobility_index': mobility_index,
            'residential': residential,
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
            'accumulated': accumulated/100}
    features = pd.DataFrame(data, index=[0])
    return features

s = user_input_features()

print(shap.__version__)

def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)

pickle_file = './model_lgbm_reg'
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


