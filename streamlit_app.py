import streamlit as st
import numpy as np
import time
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image



st.sidebar.title (" Proyecto Individual #2")
st.sidebar.subheader ("1.Cinco Estados con mayor ocupación hospitalaria por COVID")
st.sidebar.subheader("2.Ocupación de camas (Común) por COVID en el Estado de Nueva York")
st.sidebar.subheader("3. Los cinco Estados que más camas UCI -Unidades de Cuidados Intensivos- utilizaron durante el año 2020")
st.sidebar.subheader("4. Cantidad de camas se utilizaron, por Estado, para pacientes pediátricos con COVID durante el 2020")
st.sidebar.subheader("5. Porcentaje de camas UCI corresponden a casos confirmados de COVID-19")
st.sidebar.subheader("6. Muertes por covid hubo, por Estado, durante el año 2021")
st.sidebar.subheader("7. Relación presenta la falta de personal médico, con la cantidad de muertes por covid durante el año 2021")
st.sidebar.subheader("8. ¿cuál fue el peor mes de la pandemia para USA en su conjunto? Puede utilizar otras medidas que considere necesarias.")
st.sidebar.subheader("9.¿Qué recomendaciones haría, ex post, con respecto a los recursos hospitalarios y su uso?")


st.image("https://aqpagenda.com/headerhenry.png")

st.title ("Proyecto Individual #2")
st.header("Resultados del desarrollo del trabajo basado en el COVID 19 EN EEUU")
container= st.container()

container.write('Toda la data fue llenada con 0 si eran NANs')
container.write('La fecha fue transformada a otro formato como fecha por año, mes y día')

code ='''
# Convert Date from Dtype 'Object' (or String) to Dtype 'Datetime'
USCov["date"] = pd.to_datetime(USCov["date"])
# Replace missing values '' with NAN and then 0
USCov = USCov.replace('', np.nan).fillna(0)


# Replace missing values '' with NAN and then 0
USCov1 = USCov.replace('', np.nan).fillna(0)

USCov1['date'] = pd.to_datetime(USCov1['date'], format='%Y-%m-%d')

'''
st.code(code, language='python')

####################################################
#                 PREGUNTA 1                       #
####################################################


st.subheader("Cinco Estados con mayor ocupación hospitalaria por COVID")
container= st.container()
container.write('La etiqueta utilizada fue: inpatient_beds_used_covid /n	Reported patients currently hospitalized in an inpatient bed who have suspected or confirmed COVID-19 in this state')

urlCov = "https://healthdata.gov/resource/g62h-syeh.csv"

USCov = pd.read_csv(urlCov)

list_1819=USCov['previous_day_admission_adult_covid_confirmed_18_19'].tolist()

# Convert Date from Dtype 'Object' (or String) to Dtype 'Datetime'
USCov["date"] = pd.to_datetime(USCov["date"])
# Replace missing values '' with NAN and then 0
USCov = USCov.replace('', np.nan).fillna(0)

# Drop unnecessary columns

# Replace missing values '' with NAN and then 0
USCov1 = USCov.replace('', np.nan).fillna(0)

###########fecha para 6 meses #################
# Convert the date to datetime64
USCov1['date'] = pd.to_datetime(USCov1['date'], format='%Y-%m-%d')
  
# Filter data between two dates
USCov2 = USCov1.loc[(USCov1['date'] >= '2020-01-01')
                     & (USCov1['date'] < '2020-06-01')]
# Display
####################################################
#falta por rango etario

list_states = sorted(pd.unique(USCov2['state']))
####dff=pd.DataFrame(list_states)




dff2=USCov2.groupby("state", as_index=False)["inpatient_beds_used_covid"].sum()
dff2=dff2.sort_values('inpatient_beds_used_covid', ascending=False)
dff23= pd.DataFrame(dff2)
dff5=dff23.head(5)
dff23= pd.DataFrame(dff2)

##########
cleanup = {'state':{
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}
}
dff23= dff23.replace(cleanup)

list_statess = dff5['state'].tolist()
list_states = sorted(pd.unique(USCov2['state']))
fig = px.colors.sequential.swatches_continuous()

#######################


####for dataname in USCov1.columns:
##    print(dataname)
fig = px.choropleth(dff5,
                    title= 'PREGUNTA NRO 1',
                    locations=list_statess, 
                    locationmode="USA-states", 
                    scope="usa",
                    color= 'inpatient_beds_used_covid',
                    color_continuous_scale="Viridis", 
                            
                    )


fig.update_layout(
    title={'text':'Cinco Estados con mayor ocupación hospitalaria por COVID',
           'xanchor':'center',
           'yanchor':'top',
           'x':0.5})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)





