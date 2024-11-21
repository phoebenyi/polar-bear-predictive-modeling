import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load processed data
data = pd.read_csv('processed_data/processed_population_dynamics_data_with_trends.csv')
X = data[['YEAR', 'DAY', 'DAY_SIN', 'DAY_COS', 'SEA_ICE_EXTENT_7D_AVG', 'SEA_ICE_EXTENT_DIFF']]
y = data['SEA_ICE_EXTENT']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, 'models/population_dynamics_model.pkl')

# Evaluate model
y_pred = model.predict(X_test)
print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}, R²: {r2_score(y_test, y_pred):.2f}")
