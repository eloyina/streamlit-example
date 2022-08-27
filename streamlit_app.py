import streamlit as st
import matplotlib.pyplot as plt
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



###################################################


####################################################
#                 PREGUNTA 2                       #
####################################################

st.subheader ("Ocupación de camas (Común) por COVID en el Estado de Nueva York")
urlCov = "https://healthdata.gov/resource/g62h-syeh.csv"

USCov = pd.read_csv(urlCov)

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
  


####################################################

USCov5 = USCov1.loc[(USCov1['state']=='NY')]

""""""
USCov7= pd.DataFrame(USCov5)

USCov7['date']=USCov1['date']
USCov7['year'] = pd.DatetimeIndex(USCov7['date']).year
USCov7['month'] = pd.DatetimeIndex(USCov7['date']).month
USCov7['day'] = pd.DatetimeIndex(USCov7['date']).day


USCov7= USCov7[['state','date','year','month','day','inpatient_beds_used_covid']]
print(USCov7.sort_values(by='inpatient_beds_used_covid', ascending=False))
USCov7.reset_index(inplace=True)

# Prepare data
USCov7['month'] = [d.month for d in USCov7.date]
USCov7['day'] = [d.day for d in USCov7.date]
years = USCov7['month'].unique()



USCov7=USCov7.sort_values('date', ascending=False)


dia_mes = USCov7['day'].tolist() 
              

#plt.text(0.07, 1.07, 'TEXTO', fontsize=14)
print(USCov7['month'])
plt.plot(USCov7['month'], USCov7['inpatient_beds_used_covid'])
plt.plot(USCov7['month'], USCov7['inpatient_beds_used_covid'], 'o')

USCov7Sort = USCov7.sort_values('inpatient_beds_used_covid', ascending=False)

ymax = (USCov7Sort['inpatient_beds_used_covid'].tolist())[0]
xmax = (USCov7Sort['month'].tolist())[0]
ymin = (USCov7Sort['inpatient_beds_used_covid'].tolist())[-1]
xmin = (USCov7Sort['month'].tolist())[-1]

plt.annotate('max: '+str(ymax), xy=(xmax, ymax), xytext=(xmax, ymax+5)
            )
plt.annotate('min: '+str(ymin), xy=(xmin, ymin), xytext=(xmin, ymin+5)
            )

plt.xlabel('Month of the year 2020')
plt.ylabel('inpatient_beds_used_covid')
plt.xticks(USCov7['month'],  rotation=90)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.pyplot(fig=plt)

print("Intervalo de Crecimiento fue de Setiembre a Diciembre")
print("Intervalo de descrecimiento fue de Abril a Julio")



####################################################
#                 PREGUNTA 3                       #
####################################################

st.subheader ("Los cinco Estados que más camas UCI -Unidades de Cuidados Intensivos- utilizaron durante el año 2020")


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

USCov1 = USCov1.loc[(USCov1['date'] >= '2020-01-01')
                     & (USCov1['date'] < '2020-12-31')]
# Display

####################################################


dffT=USCov1.groupby("state", as_index=False)[["total_staffed_adult_icu_beds",
                                             "total_staffed_adult_icu_beds_coverage",
                                             "total_staffed_pediatric_icu_beds",
                                             "total_staffed_pediatric_icu_beds_coverage",
                                             "adult_icu_bed_covid_utilization",
                                             "adult_icu_bed_covid_utilization_coverage",
                                             "staffed_pediatric_icu_bed_occupancy",
                                             "staffed_pediatric_icu_bed_occupancy_coverage"]].apply(sum)


dffT['total_adult_beds_icu'] = dffT['total_staffed_adult_icu_beds'] + dffT['total_staffed_adult_icu_beds_coverage'] 
dffT['total_pedriatic_beds_icu'] = dffT['total_staffed_pediatric_icu_beds'] + dffT['total_staffed_pediatric_icu_beds_coverage']
dffT['total_beds_icu'] = dffT['total_adult_beds_icu'] + dffT['total_pedriatic_beds_icu']

dffT['total_adult_beds_icu_oc'] = dffT['adult_icu_bed_covid_utilization'] + dffT['adult_icu_bed_covid_utilization_coverage'] 
dffT['total_pedriatic_beds_icu_oc'] = dffT['staffed_pediatric_icu_bed_occupancy'] + dffT['staffed_pediatric_icu_bed_occupancy_coverage']
dffT['total_beds_icu_oc'] = dffT['total_adult_beds_icu_oc'] + dffT['total_pedriatic_beds_icu_oc']

# porcentaje de eso = (Total_camas_UCI - Camas_usada_COVID) 
dffT['percentage_beds_icu_oc'] = ((dffT['total_beds_icu'] - dffT['total_beds_icu_oc'])) 

dffT=dffT.sort_values('total_beds_icu_oc', ascending=False)

dffT= dffT.head(5)

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
dffTT = dffT[['state', 'total_beds_icu_oc']]
dffTT = pd.DataFrame(dffTT)
dffTT= dffTT.replace(cleanup)


list_statess = dffT['state'].tolist()
list_states = sorted(pd.unique(USCov1['state']))
fig3 = px.colors.sequential.swatches_continuous()

fig3 = px.choropleth(dffTT,
                    title= 'PREGUNTA NRO 3',
                    locations=list_statess, 
                    locationmode="USA-states", 
                    scope="usa",
                    color="total_beds_icu_oc",
                    color_continuous_scale="Viridis_r",
                    labels={'total_beds_icu_oc' : "Total de camas uci"} 
                    )


fig3.update_layout(
    title={'text':'Cantidad de camas pediátricas',
           'xanchor':'center',
           'yanchor':'top',
           'x':0.5})

fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig3)

st.subheader (" Cantidad de camas se utilizaron, por Estado, para pacientes pediátricos con COVID durante el 2020")

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
                     & (USCov1['date'] < '2020-12-31')]
# Display
####################################################
#falta por rango etario

list_states = sorted(pd.unique(USCov2['state']))

dff2=USCov2.groupby("state")["staffed_icu_pediatric_patients_confirmed_covid"].sum().sort_values(ascending=False)
  
# Filter data between two dates
USCov2 = USCov1.loc[(USCov1['date'] >= '2020-01-01')
                     & (USCov1['date'] < '2020-12-31')]
# Display

####################################################
#falta por rango etario

list_states = sorted(pd.unique(USCov2['state']))
####dff=pd.DataFrame(list_states)

dff2=USCov2.groupby("state", as_index=False)["staffed_icu_pediatric_patients_confirmed_covid"].sum()
#dff2= dff2.sort_values(ascending=False)

dff23= pd.DataFrame(dff2)

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


list_states = sorted(pd.unique(USCov2['state']))

fig44 = px.choropleth(dff23,
                    title= 'PREGUNTA NRO 4',
                    locations=list_states, 
                    locationmode="USA-states", 
                    scope="usa",
                    color= 'staffed_icu_pediatric_patients_confirmed_covid',
                    color_continuous_scale="Viridis_r", 
                    labels={'staffed_icu_pediatric_patients_confirmed_covid' : "Nª Cama Ocupada por pacientes pediátricos"}
                            
                    )


fig44.add_scattergeo(
    locations=list_states,
    locationmode='USA-states',
    text=dff23['state'],
    mode='text')
fig44.update_layout(
    title={'text':'Camas pediátricas',
           'xanchor':'center',
           'yanchor':'top',
           'x':0.5})
print("termine")
st.plotly_chart(fig44)

####################################################
####################################################
#                 PREGUNTA 5                      #
####################################################
st.subheader ("Porcentaje de camas UCI correspondiente a casos confirmados de COVID-19")

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
  
# Display

####################################################

USCov1 = USCov1.loc[(USCov1['date'] >= '2020-01-01')
                     & (USCov1['date'] < '2020-12-31')]

dffT=USCov1.groupby("state", as_index=False)[["total_staffed_adult_icu_beds",
                                             "total_staffed_adult_icu_beds_coverage",
                                             "total_staffed_pediatric_icu_beds",
                                             "total_staffed_pediatric_icu_beds_coverage",
                                             "adult_icu_bed_covid_utilization",
                                             "adult_icu_bed_covid_utilization_coverage",
                                             "staffed_pediatric_icu_bed_occupancy",
                                             "staffed_pediatric_icu_bed_occupancy_coverage"]].apply(sum)


dffT['total_adult_beds_icu'] = dffT['total_staffed_adult_icu_beds'] + dffT['total_staffed_adult_icu_beds_coverage'] 
dffT['total_pedriatic_beds_icu'] = dffT['total_staffed_pediatric_icu_beds'] + dffT['total_staffed_pediatric_icu_beds_coverage']
dffT['total_beds_icu'] = dffT['total_adult_beds_icu'] + dffT['total_pedriatic_beds_icu']

dffT['total_adult_beds_icu_oc'] = dffT['adult_icu_bed_covid_utilization'] + dffT['adult_icu_bed_covid_utilization_coverage'] 
dffT['total_pedriatic_beds_icu_oc'] = dffT['staffed_pediatric_icu_bed_occupancy'] + dffT['staffed_pediatric_icu_bed_occupancy_coverage']
dffT['total_beds_icu_oc'] = dffT['total_adult_beds_icu_oc'] + dffT['total_pedriatic_beds_icu_oc']

# porcentaje de eso = (Total_camas_UCI - Camas_usada_COVID) / Total_camas_UCI
dffT['percentage_beds_icu_oc'] = ((dffT['total_beds_icu'] - dffT['total_beds_icu_oc']) / dffT['total_beds_icu']) * 100

dffT=dffT.sort_values('percentage_beds_icu_oc', ascending=False)

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
dffTT = dffT[['state', 'percentage_beds_icu_oc']]
dffTT = pd.DataFrame(dffTT)
dffTT= dffTT.replace(cleanup)


list_statess = dffT['state'].tolist()
list_states = sorted(pd.unique(USCov1['state']))
fig55 = px.colors.sequential.swatches_continuous()

fig55 = px.choropleth(dffTT,
                    title= 'PREGUNTA NRO 5',
                    locations=list_statess, 
                    locationmode="USA-states", 
                    scope="usa",
                    color="percentage_beds_icu_oc",
                    color_continuous_scale="Viridis_r",
                    labels={'percentage_beds_icu_oc' : "Porcentaje"} 
                    )


fig55.update_layout(
    title={'text':'Porcentaje camas UCI',
           'xanchor':'center',
           'yanchor':'top',
           'x':0.5})

st.plotly_chart(fig55)

###############################################################

#########################################################
###############################################################

#########################################################

####################################################
#                 PREGUNTA 6                       #
####################################################

st.subheader("Muertes por covid hubo, por Estado, durante el año 2021")
st.caption("Gráfico Nro 6:")

# Convert Date from Dtype 'Object' (or String) to Dtype 'Datetime'
USCov["date"] = pd.to_datetime(USCov["date"])
# Replace missing values '' with NAN and then 0
USCov = USCov.replace('', np.nan).fillna(0)

# Drop unnecessary columns

# Replace missing values '' with NAN and then 0
USCov1 = USCov.replace('', np.nan).fillna(0)

# Convert the date to datetime64
USCov1['date'] = pd.to_datetime(USCov1['date'], format='%Y-%m-%d')
USCov2 = USCov1.loc[(USCov1['date'] >= '2021-01-01')
                      & (USCov1['date'] < '2021-12-31')]

####################################################
