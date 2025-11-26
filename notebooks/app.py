import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear título
st.header("Análisis exploratorio de vehículos")

# Botón para histograma
hist_button = st.button('Construir histograma')

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')


# HISTOGRAMA
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')

    st.plotly_chart(fig, use_container_width=True)


# SCATTER PLOT
if scatter_button:
    st.write('Creación de un gráfico de dispersión: Precio vs Odómetro')

    fig = go.Figure(data=go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    ))

    fig.update_layout(
        title='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig, use_container_width=True)
