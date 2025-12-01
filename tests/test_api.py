from fastapi.testclient import TestClient
from API.app import app

# Creamos un cliente de prueba (como si fuera un navegador simulado)
client = TestClient(app)

def test_read_root():
    """Prueba 1: Verificar que la API responde al saludo inicial"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de GPUs funcionando correctamente v1.0"}

def test_predict_valid_gpu():
    """Prueba 2: Verificar que predice correctamente una GPU real"""
    # Simulamos una RTX 3060 teórica
    payload = {
        "price": 329.99,
        "TDP": 170.0,
        "G2Dmark": 850.0
    }
    response = client.post("/predict", json=payload)
    
    # Verificaciones (Assertions)
    assert response.status_code == 200
    data = response.json()
    assert "prediction_G3Dmark" in data
    assert "performance_level" in data
    assert data["status"] == "success"
    # La predicción debe ser un número positivo
    assert data["prediction_G3Dmark"] > 0

def test_predict_invalid_data():
    """Prueba 3: Verificar validación de tipos de datos"""
    # Enviamos texto en vez de números para provocar error
    payload = {
        "price": "muy cara",
        "TDP": 170.0,
        "G2Dmark": 850.0
    }
    response = client.post("/predict", json=payload)
    
    # FastAPI debe rechazar esto automáticamente (Error 422: Unprocessable Entity)
    assert response.status_code == 422