import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
import os
import logging
import time

# 1. CONFIGURACIÓN DE LOGS (Requisito: Log del entrenamiento)
# ---------------------------------------------------------
# Esto guardará un historial de lo que pasa en un archivo 'logs/training.log'
os.makedirs("logs", exist_ok=True) # Crear carpeta si no existe

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/training.log"), # Guarda en archivo dentro de logs/
        logging.StreamHandler()                   # Muestra en consola
    ]
)

logger = logging.getLogger(__name__)

def main():
    print("\n" + "="*50)
    print("🚀 INICIANDO PROCESO DE ENTRENAMIENTO DEL MODELO")
    print("="*50 + "\n")

    # Rutas dinámicas
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'gpu_cleaned.csv')
    MODEL_PATH = os.path.join(BASE_DIR, 'models', 'gpu_predictor_model.pkl')

    # 2. CARGA DE DATOS
    # ---------------------------------------------------------
    print("⏳ [1/4] Cargando y procesando datos...")
    time.sleep(1) # Simulación de proceso para que se vea el mensaje
    
    if not os.path.exists(DATA_PATH):
        logger.error(f"No se encontró el dataset en: {DATA_PATH}")
        return

    df = pd.read_csv(DATA_PATH)
    logger.info(f"Datos cargados exitosamente: {df.shape[0]} registros encontrados.")

    # 3. PREPARACIÓN
    # ---------------------------------------------------------
    print("⏳ [2/4] Separando conjuntos de entrenamiento y prueba...")
    X = df[['price', 'TDP', 'G2Dmark', 'price_per_watt']]
    y = df['G3Dmark']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logger.info(f"Set de Entrenamiento: {X_train.shape[0]} datos | Set de Prueba: {X_test.shape[0]} datos")

    # 4. ENTRENAMIENTO
    # ---------------------------------------------------------
    print("⚙️ [3/4] Entrenando algoritmo Random Forest (esto puede tardar unos segundos)...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    logger.info("Entrenamiento finalizado correctamente.")

    # 5. EVALUACIÓN
    # ---------------------------------------------------------
    print("📈 [4/4] Evaluando precisión del modelo...")
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    logger.info(f"Métricas obtenidas -> R2 Score: {r2:.4f} | MAE: {mae:.2f}")

    # 6. GUARDADO
    # ---------------------------------------------------------
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    
    print("\n" + "="*50)
    print(f"✅ ÉXITO: Modelo guardado en 'models/gpu_predictor_model.pkl'")
    print(f"📊 Precisión Final (R2): {r2:.4f}")
    print("="*50)

if __name__ == "__main__":
    main()