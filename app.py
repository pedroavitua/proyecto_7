import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la aplicación
st.header('Análisis de anuncios de venta de vehículos')

# Cargar el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

st.write('Explora los datos de vehículos usados anunciados en Estados Unidos.')

# Mostrar una vista previa
st.subheader('Vista previa de los datos')
st.dataframe(car_data.head())

# Casillas de selección
build_histogram = st.checkbox('Mostrar histograma de kilometraje')
build_scatter = st.checkbox('Mostrar relación entre kilometraje y precio')

# Construir histograma
if build_histogram:
    st.write('Distribución del kilometraje de los vehículos')

    fig = px.histogram(
        car_data,
        x='odometer',
        nbins=50,
        title='Distribución del kilometraje',
        labels={'odometer': 'Kilometraje (millas)'}
    )

    st.plotly_chart(fig, use_container_width=True)

# Construir diagrama de dispersión
if build_scatter:
    st.write('Relación entre kilometraje y precio')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Kilometraje vs. precio',
        labels={
            'odometer': 'Kilometraje (millas)',
            'price': 'Precio (USD)'
        },
        opacity=0.5
    )

    st.plotly_chart(fig, use_container_width=True)