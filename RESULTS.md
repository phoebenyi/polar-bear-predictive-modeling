# Results Analysis

This document provides an analysis of the predictive modeling and time series forecasting results obtained from the trained models. Key metrics include Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² (R-Squared).

---

## Evaluation Metrics

### Predictive Modeling (Random Forest)
1. **Mean Squared Error (MSE)**: `79,640,751.46`
   - **Interpretation**: MSE measures the average squared difference between predicted and actual values. A lower MSE is better. 
   - While the value appears large, it is in the context of sea ice extent measured in square kilometers. Given the scale of the data, this result may be reasonable.

2. **Mean Absolute Error (MAE)**: `3,568.27`
   - **Interpretation**: MAE represents the average magnitude of errors in the predictions. In this case, the predictions are off by approximately 3,568 km² on average, which is relatively small compared to the total sea ice extent.

3. **R² (R-Squared)**: `1.00`
   - **Interpretation**: An R² of 1.00 indicates that the model explains all variability in the data perfectly. While this seems ideal, it raises concerns about overfitting.

### ARIMA Forecasting
For the ARIMA model, we focused on forecasting yearly average sea ice extent for the Chukchi Sea.

1. **Mean Squared Error (MSE)**: `2,850,000`
   - **Interpretation**: MSE is significantly lower than Random Forest due to the aggregation of daily data into yearly averages, simplifying the time series.
   
2. **Mean Absolute Error (MAE)**: `1,700`
   - **Interpretation**: The ARIMA model achieves lower absolute errors on yearly average predictions, highlighting its suitability for univariate time series forecasting.

3. **Visualization**: 
   - **Chukchi Sea ARIMA Forecast**: The forecast visualization below shows the ARIMA predictions alongside training and test data.
   - ![ARIMA Forecast](visualizations/Chukchi_arima_forecast.png)

---

## Visualizations

### 1. Sea Ice Extent Trends
The visualizations below display daily sea ice extent along with smoothed 7-day rolling averages for each region.

#### **Chukchi Sea**
![Chukchi Sea Ice Extent](visualizations/Chukchi_sea_ice_extent_trend.png)

#### **Southern Beaufort Sea**
![Southern Beaufort Sea Ice Extent](visualizations/Southern_Beaufort_sea_ice_extent_trend.png)

---

### 2. Sea Ice Area Trends
These plots show daily sea ice area with corresponding rolling averages for trend analysis.

#### **Chukchi Sea**
![Chukchi Sea Ice Area](visualizations/Chukchi_sea_ice_area_trend.png)

#### **Southern Beaufort Sea**
![Southern Beaufort Sea Ice Area](visualizations/Southern_Beaufort_sea_ice_area_trend.png)

---

### 3. Daily Changes in Sea Ice Extent
The following visualizations highlight day-to-day changes in sea ice extent for both regions.

#### **Chukchi Sea**
![Chukchi Sea Ice Extent Daily Changes](visualizations/Chukchi_sea_ice_extent_diff.png)

#### **Southern Beaufort Sea**
![Southern Beaufort Sea Ice Extent Daily Changes](visualizations/Southern_Beaufort_sea_ice_extent_diff.png)

---

### 4. ARIMA Forecast
The ARIMA model was applied to yearly average sea ice extent for the Chukchi Sea. The visualization below shows the training data, test data, and the forecasted values.

#### **Chukchi Sea ARIMA Forecast**
![ARIMA Forecast](visualizations/Chukchi_arima_forecast.png)

---

## Evaluation and Recommendations

### 1. **Understanding the Metrics**:
   - **Random Forest**: The model achieved a perfect R² score, but the high MSE indicates potential overfitting. This suggests that the model may not generalize well to unseen data.
   - **ARIMA**: Lower MSE and MAE indicate strong performance for yearly averaged time series forecasting. The model captures temporal trends effectively.

### 2. **Comparison of Models**:
   - **Random Forest** excels with high-dimensional data and non-linear relationships.
   - **ARIMA** performs better for univariate time series with strong temporal dependencies.

### 3. **Real-World Forecasting**:
   - **Random Forest**: Incorporating additional features (e.g., temperature, atmospheric data) could improve generalization.
   - **ARIMA**: Extend the forecast horizon to predict future sea ice extent for several years.

---

## Summary

The project successfully combines predictive modeling and time series forecasting techniques. Key takeaways:
- The Random Forest model demonstrates high accuracy for multivariate predictions but may suffer from overfitting.
- The ARIMA model achieves strong results for univariate time series forecasting, providing reliable yearly predictions.

Incorporating additional features and addressing overfitting in Random Forest can further improve predictive capabilities.

---

## Visualization Directory

All visualizations are saved in the `visualizations/` directory of this project:
1. **Sea Ice Extent Trends**:
   - `visualizations/Chukchi_sea_ice_extent_trend.png`
   - `visualizations/Southern_Beaufort_sea_ice_extent_trend.png`
2. **Sea Ice Area Trends**:
   - `visualizations/Chukchi_sea_ice_area_trend.png`
   - `visualizations/Southern_Beaufort_sea_ice_area_trend.png`
3. **Daily Changes in Sea Ice Extent**:
   - `visualizations/Chukchi_sea_ice_extent_diff.png`
   - `visualizations/Southern_Beaufort_sea_ice_extent_diff.png`
4. **ARIMA Forecast**:
   - `visualizations/Chukchi_arima_forecast.png`

For detailed trend analysis, refer to these visualizations.
