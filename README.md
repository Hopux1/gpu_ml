# 🎮 Sistema de Predicción de Rendimiento de GPUs

## 1. Introducción y Objetivo
Este proyecto desarrolla una solución de Machine Learning para predecir el rendimiento de tarjetas gráficas (GPUs) basándose en sus especificaciones técnicas. El objetivo es proporcionar una herramienta útil para consumidores y analistas que deseen estimar la potencia (G3Dmark) de una GPU sin necesidad de tenerla físicamente para realizar benchmarks.

## 2. Explicación del Problema y Solución

### El Problema
En el mercado actual de hardware, existen cientos de modelos de GPUs con especificaciones variadas. Para un usuario, es difícil saber qué rendimiento esperar solo viendo números como la frecuencia o la memoria. Los benchmarks reales (como G3Dmark) son la referencia, pero no siempre están disponibles para modelos nuevos o variantes específicas.
**Impacto:** Ayudar a tomar decisiones de compra informadas y estimar la relación precio-rendimiento.

### La Solución Propuesta
Hemos desarrollado un sistema predictivo basado en **Random Forest Regressor**.
*   **Arquitectura:**
    *   **Backend:** FastAPI para servir el modelo como una API REST.
    *   **Frontend:** Streamlit para un dashboard interactivo.
    *   **Modelo:** Scikit-learn (Random Forest).
*   **Pipeline:**
    1.  Ingesta de datos crudos (CSV).
    2.  Limpieza y preprocesamiento (Manejo de nulos, conversión de tipos).
    3.  Feature Engineering (Creación de `price_per_watt`).
    4.  Entrenamiento y validación.

## 3. Estructura del Proyecto
```
proyecto_gpu_ml/
├── API/                # API FastAPI
├── data/               # Datasets (raw y processed)
├── docs/               # Documentación y evidencias
├── logs/               # registro de entrenamiento
├── models/             # Modelos serializados (.pkl)
├── notebooks/          # Jupyter Notebooks (EDA y Entrenamiento)
├── src/                # Código fuente
│   ├── dashboard.py    # Interfaz Streamlit
│   └── train.py        # Script de entrenamiento
├── tests/              # Tests unitarios
├── venv/               # Entorno virtual
└── README.md           # Este archivo
```

## 4. Instalación y Uso

### Prerrequisitos
*   Python 3.8+
*   Git

### Pasos
1.  **Clonar el repositorio:**
    ```bash
    git clone <url-repo>
    cd proyecto_gpu_ml
    ```

2.  **Crear y activar entorno virtual:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la API:**
    ```bash
    uvicorn API.app:app --reload
    ```

5.  **Ejecutar el Dashboard:**
    ```bash
    streamlit run src/dashboard.py
    ```

### Video Manual de Usuario
Aquí puedes ver un video demostrativo del funcionamiento básico de la aplicación:

[![Ver Video](https://img.youtube.com/vi/j0aZOetCKOw/0.jpg)](https://www.youtube.com/watch?v=j0aZOetCKOw)

## 5. Tecnologías Utilizadas
*   **Python**: Lenguaje principal.
*   **Pandas/Numpy**: Manipulación de datos.
*   **Scikit-learn**: Modelado de ML.
*   **FastAPI**: API REST.
*   **Streamlit**: Visualización de datos.
*   **Pytest**: Testing.

## 6. Autores
Proyecto desarrollado para el curso de Machine Learning.
