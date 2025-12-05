# Evidencia de Pruebas Funcionales

## 1. Pruebas de API (Backend)

### Prueba 1: Predicción Exitosa
**Objetivo:** Verificar que el endpoint `/predict` devuelve una predicción válida para datos correctos.
**Entrada (JSON):**
```json
{
  "price": 350.0,
  "TDP": 170.0,
  "G2Dmark": 900.0
}
```
**Resultado Esperado:** Código 200 OK y JSON con `prediction_G3Dmark`.
**Resultado Obtenido:**
```json
{
  "status": "success",
  "gpu_specs": {
    "price": 350.0,
    "TDP": 170.0,
    "G2Dmark": 900.0
  },
  "prediction_G3Dmark": 14935.0,
  "performance_level": "Mid/Low Range"
}
```
**Estado:** ✅ PASÓ

### Prueba 2: Validación de Datos
**Objetivo:** Verificar que la API rechaza datos con tipos incorrectos.
**Entrada:** `price` como string "caro".
**Resultado Esperado:** Código 422 Unprocessable Entity.
**Resultado Obtenido:** Código 422 (Verificado vía TestClient en `test_api.py`).
**Estado:** ✅ PASÓ

---

## 2. Pruebas de Dashboard (Frontend)

### Prueba 3: Carga de Interfaz
**Objetivo:** Verificar que Streamlit carga sin errores.
**Comando:** `streamlit run src/dashboard.py`
**Resultado:** La aplicación carga en `http://localhost:8501`. Se visualizan los inputs numéricos y el botón de calcular.
**Estado:** ✅ PASÓ

### Prueba 4: Integración Frontend-Backend
**Objetivo:** Verificar que el botón "Calcular Rendimiento" en Streamlit se comunica con la API.
**Acción:** Ingresar valores por defecto y presionar "Calcular".
**Resultado:** Se muestra el puntaje predicho y la clasificación "High End" o "Mid/Low Range".
**Estado:** ✅ PASÓ
