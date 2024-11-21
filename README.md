# polar-bear-predictive-modeling
Polar Bear Population Predictive Modeling

This repository uses Time Series Forecasting and Predictive Modeling methods to analyze and forecast population dynamics using Sea Ice Data. The project includes data processing, trend analysis, ARIMA-based forecasting, model training, evaluation, and visualization.

---

## Concepts

### Predictive Modeling
Predictive modeling is a statistical or machine learning technique used to predict future outcomes based on historical data. It involves creating a model that maps input features to desired output targets. In this project, predictive modeling is used to estimate **sea ice extent** based on past data, including cyclical trends, yearly patterns, and changes over time.

Key steps in predictive modeling include:
1. **Data Preparation**: Clean and preprocess the data for modeling.
2. **Feature Engineering**: Add meaningful features, such as rolling averages or cyclical transformations, to capture trends and patterns.
3. **Model Training**: Use algorithms (e.g., Random Forest) to learn relationships between input features and target variables.
4. **Evaluation**: Test the model's accuracy on unseen data using metrics like Mean Squared Error (MSE) and R².

---

### Time Series Forecasting
Time series forecasting is a specialized form of predictive modeling that focuses on data collected at regular time intervals. The goal is to predict future values by understanding temporal dependencies and trends in the data.

Key components of time series data:
- **Trend**: Long-term increase or decrease in the data.
- **Seasonality**: Recurring patterns or cycles (e.g., annual sea ice changes).
- **Noise**: Random variation that cannot be explained by the model.

In this project:
- Time series forecasting helps predict daily and yearly sea ice extent and area.
- Features like **sine/cosine transformations** of the day and **rolling averages** capture seasonal and trend effects.
- Yearly and daily information are combined with these features to enhance forecast accuracy.

---

## Dataset
The dataset used in this project is publicly available on [Dryad Digital Repository](https://datadryad.org/stash/dataset/doi:10.5061/dryad.f68m0), specifically from Regehr et al. (2017). It contains:
- Daily measurements of **sea ice extent** and **sea ice area** for the Chukchi and Southern Beaufort Seas.
- Metadata describing the data structure.

### Original Fields:
- **YEAR**: Calendar year of observation.
- **DAY**: Day of the year (1-365).
- **SEA_ICE_EXTENT**: Daily sea ice extent in km².
- **SEA_ICE_AREA**: Daily sea ice area in km².

---

## Workflow

### 1. Data Processing
- Combines the Chukchi and Southern Beaufort sea ice datasets.
- Adds new features:
  - **Rolling Averages**: Smooths data to highlight trends.
  - **Daily Differences**: Captures day-to-day changes.
  - **Cyclical Features**: Uses sine and cosine transformations to model seasonal patterns.
- Saves processed data for analysis and modeling.

### 2. ARIMA Forecasting
- Fits an **ARIMA (AutoRegressive Integrated Moving Average)** model to forecast yearly sea ice extent for specific regions (e.g., Chukchi Sea).
- Outputs:
  - Forecast visualization of yearly trends.
  - Metrics such as **Mean Squared Error (MSE)** and **Mean Absolute Error (MAE)** for evaluation.

### 3. Model Training
- Trains a **Random Forest Regressor** to predict sea ice extent using features such as:
  - Year, day, rolling averages, and daily differences.
- The trained model is saved for future predictions.

### 4. Evaluation
- Tests the trained model's accuracy using unseen data.
- Key metrics include:
  - **Mean Squared Error (MSE)**: Measures average prediction error.
  - **R² (R-Squared)**: Indicates how well the model explains the variability in the data.

### 5. Trend Visualization
- Generates visualizations of sea ice trends, including:
  - Daily sea ice extent and area with rolling averages.
  - Day-to-day changes in sea ice extent.
- For more details, refer to the RESULTS.md file.
- All generated visualizations are stored in the visualizations/ directory, including:
  - Sea Ice Extent Trends
  - Sea Ice Area Trends
  - Daily Changes in Sea Ice Extent
  - ARIMA Forecast Visualization

---

## Installation Instructions 💻

To set up the environment, clone this repository and install the required packages:

```bash
git clone https://github.com/phoebenyi/polar-bear-predictive-modeling.git
cd polar-bear-predictive-modeling
python3 -m pip install -r requirements.txt
```


## Running Instructions ⌨️
Use the following commands:
```bash
python3 scripts/data_processing.py         # Processes Data & Prepares Dataset
python3 scripts/arima_forecasting.py       # Forecast Future Sea Ice Extents
python3 scripts/model_training.py          # Train Predictive Model
python3 scripts/evaluation.py              # Evaluate Model Performance
python3 scripts/trend_visualization.py     # Create Visualizations of Trends
```

