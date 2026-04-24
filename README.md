## NYC Taxi Fare Prediction

## Project Overview
Predicts NYC taxi fares using trip data (location, passengers, time). End-to-end ML pipeline from data cleaning to model prediction.

## Dataset
- **Source**: Kaggle NYC Taxi Fare Competition  
- **Size**: ~1M training + 500K test samples  
- **Download**: kaggle competitions download -c new-york-city-taxi-fare-prediction  

## Tools
- Python, Pandas, NumPy  
- Scikit-learn, XGBoost  
- Matplotlib, Seaborn  

## Workflow

### 1. Data Cleaning
- Removed invalid fares (negative or zero values)  
- Filtered unrealistic passenger counts (1–6)  
- Removed coordinate outliers (e.g., (0,0) and outside NYC bounds)  

### 2. Feature Engineering
- `distance_km` using Haversine formula  
- `is_airport` flag (JFK, LGA, EWR)  
- Temporal features (hour, day_of_week, year)  

### 3. Modeling
- Compared Linear Regression, Ridge, and XGBoost  
- **XGBoost** performed best after tuning with RandomizedSearchCV  

## Results

- **Linear Regression** → RMSE: 4.23 | R²: 0.79  
- **Ridge Regression** → RMSE: 4.21 | R²: 0.80  
- **XGBoost (Tuned)** → RMSE: 3.42 | R²: 0.87  

## Key Insights
- Distance is the strongest predictor of fare  
- Airport trips introduce premium pricing effects  
- Temporal features have minimal direct impact  

## Status
Completed (End-to-End ML Pipeline)

## Future Work
- Explore neural network models for capturing more complex patterns.

