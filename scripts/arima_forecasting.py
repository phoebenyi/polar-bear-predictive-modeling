import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

# Load processed data
data = pd.read_csv('processed_data/processed_population_dynamics_data_with_trends.csv')

# Filter data for a specific region (e.g., Chukchi Sea)
region = 'Chukchi'
region_data = data[data['REGION'] == region]

# Aggregate daily data into yearly averages for simplicity
region_yearly = region_data.groupby('YEAR')['SEA_ICE_EXTENT'].mean().reset_index()

# Prepare the data
time_series = region_yearly.set_index('YEAR')['SEA_ICE_EXTENT']

# Split into training and testing sets
train = time_series[:-5]  # Use all but the last 5 years for training
test = time_series[-5:]   # Use the last 5 years for testing

# Fit the ARIMA model (SARIMAX for flexibility)
model = SARIMAX(train, order=(1, 1, 1), seasonal_order=(0, 1, 1, 12))
results = model.fit(disp=False)

# Forecast future values
forecast = results.forecast(steps=len(test))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(train, label='Training Data', color='blue')
plt.plot(test, label='Test Data', color='orange')
plt.plot(forecast, label='Forecast', color='green', linestyle='--')
plt.title(f"ARIMA Forecast for Sea Ice Extent - {region}")
plt.xlabel('Year')
plt.ylabel('Sea Ice Extent (km²)')
plt.legend()
plt.grid()
plt.savefig(f"visualizations/{region}_arima_forecast.png")
plt.show()

# Print model summary and accuracy
print(results.summary())

# Calculate forecast accuracy
from sklearn.metrics import mean_squared_error, mean_absolute_error

mse = mean_squared_error(test, forecast)
mae = mean_absolute_error(test, forecast)
print(f"Forecast Accuracy:\nMSE: {mse:.2f}\nMAE: {mae:.2f}")
