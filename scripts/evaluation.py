import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

# Load data and model
data = pd.read_csv('processed_data/processed_population_dynamics_data_with_trends.csv')
model = joblib.load('models/population_dynamics_model.pkl')

X = data[['YEAR', 'DAY', 'DAY_SIN', 'DAY_COS', 'SEA_ICE_EXTENT_7D_AVG', 'SEA_ICE_EXTENT_DIFF']]
y_true = data['SEA_ICE_EXTENT']

# Predictions
y_pred = model.predict(X)

# Metrics
print(f"MSE: {mean_squared_error(y_true, y_pred):.2f}")
print(f"MAE: {mean_absolute_error(y_true, y_pred):.2f}")
print(f"R²: {r2_score(y_true, y_pred):.2f}")
