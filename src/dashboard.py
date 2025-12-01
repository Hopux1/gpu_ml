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
        st.caption("📝 Nota: Ahora puedes escribir texto para probar la validación.")
        price_input = st.text_input("Precio de Mercado (USD)", value="499.0", help="Ejemplo: 499.99")
        tdp_input = st.text_input("Consumo (TDP Watts)", value="200.0", help="Ejemplo: 150")
        g2d_input = st.text_input("Puntaje 2D (G2Dmark)", value="800.0", help="Ejemplo: 850")
        
        submitted = st.form_submit_button("Calcular Rendimiento")

with col2:
    st.header("📊 Resultados del Análisis")
    
    if submitted:
        # VALIDACIÓN MANUAL (Requisito: Demostrar validación de datos)
        if not price_input or not tdp_input or not g2d_input:
            st.error("❌ Error de Validación: Todos los campos son obligatorios. No puedes dejarlos vacíos.")
            st.stop()

        try:
            price = float(price_input)
            tdp = float(tdp_input)
            g2d = float(g2d_input)
        except ValueError:
            st.error("❌ Error de Validación: Por favor ingresa solo valores numéricos válidos.")
            st.stop()

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