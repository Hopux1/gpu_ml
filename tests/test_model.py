import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Mock data for testing
@pytest.fixture
def mock_data():
    data = {
        'price': [100, 200, 300, 400, 500],
        'TDP': [50, 100, 150, 200, 250],
        'G2Dmark': [500, 600, 700, 800, 900],
        'price_per_watt': [2.0, 2.0, 2.0, 2.0, 2.0],
        'G3Dmark': [1000, 2000, 3000, 4000, 5000]
    }
    return pd.DataFrame(data)

def test_data_structure(mock_data):
    """Test that the data has the expected columns"""
    expected_cols = ['price', 'TDP', 'G2Dmark', 'price_per_watt', 'G3Dmark']
    assert all(col in mock_data.columns for col in expected_cols)

def test_model_training(mock_data):
    """Test that the model can be trained without errors"""
    X = mock_data[['price', 'TDP', 'G2Dmark', 'price_per_watt']]
    y = mock_data['G3Dmark']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    
    assert model is not None
    assert hasattr(model, 'predict')

def test_prediction_shape(mock_data):
    """Test that prediction returns the correct shape"""
    X = mock_data[['price', 'TDP', 'G2Dmark', 'price_per_watt']]
    y = mock_data['G3Dmark']
    
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    model.fit(X, y)
    
    predictions = model.predict(X)
    assert len(predictions) == len(X)
    assert isinstance(predictions, np.ndarray)
