# 📘 Manual de Usuario: Sistema de Predicción de Rendimiento de GPUs

Bienvenido al manual de usuario del **Sistema de Predicción de Rendimiento de GPUs**. Esta aplicación web utiliza Machine Learning para estimar el rendimiento (G3Dmark) de una tarjeta gráfica basándose en sus especificaciones técnicas.

---

## 🚀 1. Introducción

Esta herramienta está diseñada para ayudar a entusiastas y profesionales a estimar el potencial de una GPU antes de comprarla o probarla.

**Funcionalidades Principales:**
- **Predicción de Rendimiento:** Estima el puntaje G3Dmark.
- **Clasificación Automática:** Categoriza la GPU en gamas (Baja, Media, Alta, Ultra).
- **Visualización de Mercado:** Gráficos interactivos para comparar con datos reales.

---

## 🛠️ 2. Requisitos e Instalación

Antes de iniciar, asegúrate de tener instalado:
- Python 3.8 o superior
- Las dependencias del proyecto (listadas en `requirements.txt`)

### Pasos para iniciar la aplicación:

El sistema consta de dos partes: el **Backend (API)** y el **Frontend (Dashboard)**. Debes iniciar ambos para que funcione correctamente.

#### Paso 1: Iniciar la API (Backend)
Abre una terminal en la carpeta raíz del proyecto y ejecuta:
```bash
uvicorn API.app:app --reload
```
*Deberías ver un mensaje indicando que la API está corriendo en `http://127.0.0.1:8000`.*

#### Paso 2: Iniciar el Dashboard (Frontend)
Abre **otra** terminal en la carpeta raíz y ejecuta:
```bash
streamlit run src/dashboard.py
```
*Esto abrirá automáticamente una pestaña en tu navegador con la aplicación.*

---

## 🎮 3. Guía de Uso

Una vez en el Dashboard, verás una interfaz dividida en dos secciones principales.

### A. Configuración de tu GPU (Panel Izquierdo)
Aquí ingresarás los datos técnicos de la tarjeta gráfica que deseas analizar.

1.  **Precio de Mercado (USD):** Ingresa el precio estimado en dólares.
    *   *Ejemplo:* `499.99`
2.  **Consumo (TDP Watts):** Ingresa la potencia de diseño térmico en Watts.
    *   *Ejemplo:* `220`
3.  **Puntaje 2D (G2Dmark):** Ingresa el puntaje de rendimiento 2D (si lo conoces, o un estimado).
    *   *Ejemplo:* `850`

> **Nota:** Todos los campos son obligatorios y deben ser valores numéricos.

### B. Resultados del Análisis (Panel Derecho)
Presiona el botón **"Calcular Rendimiento"** para obtener los resultados.

- **Puntaje G3Dmark Predicho:** El valor estimado de rendimiento 3D.
- **Clasificación:** La categoría de la GPU (ej. "Gama alta - Gaming 1440p/4K").
- **Detalles Técnicos:** Un bloque JSON con la respuesta cruda del servidor para validación técnica.

### C. Contexto del Mercado (Parte Inferior)
Desplázate hacia abajo para ver el gráfico **"Mapa de Rendimiento"**.
- Este gráfico interactivo muestra cómo se compara tu GPU con datos históricos.
- **Eje X:** Precio
- **Eje Y:** Rendimiento (G3Dmark)
- **Color:** Consumo (TDP)

---

## ❓ 4. Solución de Problemas

**Problema:** "Error en la predicción. Revisa que la API esté corriendo."
- **Solución:** Asegúrate de haber ejecutado el **Paso 1** (Iniciar la API) y que la terminal no muestre errores.

**Problema:** "Error de Validación"
- **Solución:** Verifica que hayas ingresado solo números en los campos de texto (usa punto `.` para decimales).

**Problema:** El gráfico no aparece.
- **Solución:** Verifica que el archivo de datos `data/processed/gpu_cleaned.csv` exista en la ruta correcta.

---

## 📞 Soporte
Si encuentras errores adicionales, por favor contacta al equipo de desarrollo o revisa los logs en la carpeta `logs/`.
