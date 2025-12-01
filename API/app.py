from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# 1. INICIALIZAR LA APP
# ---------------------------------------------------------
app = FastAPI(
    title="API de Predicción de GPUs",
    description="Endpoint para predecir el rendimiento G3Dmark usando Random Forest",
    version="1.0.0"
)

# 2. CARGAR EL MODELO ENTRENADO (Requisito 4.5 - Carga del modelo)
# ---------------------------------------------------------
# Buscamos la ruta relativa correcta desde 'src' hacia 'models'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'gpu_predictor_model.pkl')

print(f"Cargando modelo desde: {MODEL_PATH}")

try:
    model = joblib.load(MODEL_PATH)
    print("¡Modelo cargado correctamente en memoria!")
except Exception as e:
    print(f"ERROR CRÍTICO: No se pudo cargar el modelo. {e}")
    model = None

# 3. DEFINIR EL FORMATO DE ENTRADA (Requisito 4.5 - Validación de datos)
# ---------------------------------------------------------
class GPUInput(BaseModel):
    price: float       # Precio en USD
    TDP: float         # Consumo en Watts
    G2Dmark: float     # Puntaje 2D (Suele estar correlacionado)

    # Ejemplo para la documentación automática
    class Config:
        schema_extra = {
            "example": {
                "price": 499.99,
                "TDP": 220.0,
                "G2Dmark": 850.0
            }
        }

# 4. CREAR EL ENDPOINT DE PREDICCIÓN (Requisito 4.5 - Endpoint funcional)
# ---------------------------------------------------------
@app.post("/predict")
def predict_performance(data: GPUInput):
    """
    Recibe especificaciones de GPU y devuelve la predicción de G3Dmark.
    """
    if not model:
        raise HTTPException(status_code=500, detail="Modelo no cargado")

    try:
        # A. PREPROCESAMIENTO
        # El modelo fue entrenado con 4 variables: price, TDP, G2Dmark, price_per_watt
        # El usuario solo nos manda 3, así que calculamos la 4ta aquí mismo (Feature Engineering en vivo)
        price_per_watt = data.price / data.TDP if data.TDP > 0 else 0
        
        # Creamos un DataFrame con el formato exacto que espera el modelo
        input_df = pd.DataFrame([{
            'price': data.price,
            'TDP': data.TDP,
            'G2Dmark': data.G2Dmark,
            'price_per_watt': price_per_watt
        }])

        # B. PREDICCIÓN
        prediction = model.predict(input_df)[0]

        # CLASIFICACIÓN AVANZADA
        if prediction < 5000:
            level = "Gama baja - De oficina"
        elif 5000 <= prediction < 14000:
            level = "Gama media - Gaming 1080p"
        elif 14000 <= prediction < 22000:
            level = "Gama alta - Gaming 1440p/4K"
        else:
            level = "Gama ultra - ¡Nivel Dios!"

        # C. RESPUESTA
        return {
            "status": "success",
            "gpu_specs": data.dict(),
            "prediction_G3Dmark": round(prediction, 0),
            "performance_level": level
        }

    except Exception as e:
        # Manejo de errores (Requisito 4.5)
        raise HTTPException(status_code=500, detail=f"Error al procesar: {str(e)}")

# Endpoint de prueba para ver si la API vive
@app.get("/")
def read_root():
    return {"message": "API de GPUs funcionando correctamente v1.0"}