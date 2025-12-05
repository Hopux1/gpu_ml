import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import os

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Predicción de GPU",
    page_icon="🎮",
    layout="wide"
)

# TÍTULO Y DESCRIPCIÓN
st.title("🎮 Sistema de Predicción de Rendimiento de GPUs")
st.markdown("""
Este sistema utiliza **Machine Learning (Random Forest)** para estimar el puntaje de benchmark (G3Dmark) 
de una tarjeta gráfica basándose en sus especificaciones técnicas.
""")

# COLUMNAS PARA EL LAYOUT
col1, col2 = st.columns([1, 2])

with col1:
    st.header("⚙️ Configura tu GPU")
    st.write("Ingresa los valores técnicos:")
    
    # FORMULARIO DE ENTRADA
    with st.form("prediction_form"):
        st.caption("📝 Nota: Los campos ahora solo aceptan números.")
        price_input = st.number_input("Precio de Mercado (USD)", value=499.0, min_value=0.0, step=10.0, format="%.2f", help="Ejemplo: 499.99")
        tdp_input = st.number_input("Consumo (TDP Watts)", value=200.0, min_value=0.0, step=5.0, format="%.1f", help="Ejemplo: 150")
        g2d_input = st.number_input("Puntaje 2D (G2Dmark)", value=800.0, min_value=0.0, step=10.0, format="%.1f", help="Ejemplo: 850")
        
        st.warning("⚠️ Solo se pueden colocar números.")
        
        submitted = st.form_submit_button("Calcular Rendimiento")

with col2:
    st.header("📊 Resultados del Análisis")
    
    if submitted:
        # VALIDACIÓN MANUAL (Requisito: Demostrar validación de datos)
        # st.number_input ya garantiza números, pero validamos que no sean cero si es crítico
        if price_input <= 0 or tdp_input <= 0:
             st.warning("⚠️ Advertencia: El precio y el consumo suelen ser mayores a 0.")

        # Asignación directa (ya son floats)
        price = price_input
        tdp = tdp_input
        g2d = g2d_input

        # CONEXIÓN CON LA API
        api_url = "http://127.0.0.1:8000/predict"
        payload = {
            "price": price,
            "TDP": tdp,
            "G2Dmark": g2d
        }
        
        try:
            with st.spinner("Consultando al oráculo digital..."):
                response = requests.post(api_url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                # CLAVES (Coinciden con API/app.py)
                prediction = result['prediction_G3Dmark']
                level = result['performance_level']
                
                # MOSTRAR MÉTRICAS GRANDES
                st.metric(label="Puntaje G3Dmark Predicho", value=f"{prediction} pts")
                
                # Mostrar clasificación dinámica (basada en lo que devuelve la API)
                if "Gama alta" in level or "Gama ultra" in level or "High End" in level:
                    st.success(f"Clasificación: **{level}**")
                else:
                    st.info(f"Clasificación: **{level}**")
                
                st.json(result) # Muestra el JSON crudo para evidencia técnica
                
            else:
                st.error("Error en la predicción. Revisa que la API esté corriendo.")
                
        except Exception as e:
            st.error(f"No se pudo conectar con la API. ¿Está encendida? Error: {e}")

    else:
        st.info("👈 Ajusta los parámetros y presiona 'Calcular' para ver la magia.")

# SECCIÓN DE GRÁFICOS (Requisito Rúbrica: Visualización EDA)
st.divider()
st.header("📈 Contexto del Mercado (Datos Reales)")

# Cargar datos para el gráfico
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'gpu_cleaned.csv')

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    fig = px.scatter(
        df, 
        x='price', 
        y='G3Dmark',
        color='TDP',
        title="Mapa de Rendimiento: Precio vs Potencia (Color = Consumo)",
        hover_data=['G3Dmark']
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No se encontró el archivo de datos procesados para generar gráficos.")