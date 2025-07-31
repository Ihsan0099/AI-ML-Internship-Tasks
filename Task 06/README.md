# House Price Prediction Task

## Overview
This Task focuses on predicting house prices based on various property features using machine learning techniques. The dataset contains information about house characteristics such as area, number of bedrooms, bathrooms, stories, and various amenities.

## Dataset Description
The dataset includes the following features:
- **Numerical Features**:
  - `price`: Price of the house (target variable)
  - `area`: Total area in square feet
  - `bedrooms`: Number of bedrooms
  - `bathrooms`: Number of bathrooms
  - `stories`: Number of stories
  - `parking`: Number of parking spaces

- **Binary Features** (converted to 0/1):
  - `mainroad`: Connectivity to main road
  - `guestroom`: Guest room availability
  - `basement`: Basement availability
  - `hotwaterheating`: Hot water heating availability
  - `airconditioning`: Air conditioning availability
  - `prefarea`: Preferred area location

- **Categorical Feature**:
  - `furnishingstatus`: Furnishing status (one-hot encoded)

## Project Structure
1. **Data Exploration**: Visualizations to understand data distributions and relationships
2. **Data Preprocessing**: Handling categorical variables, outlier removal, feature scaling
3. **Model Training**: Implementation of Linear Regression and Gradient Boosting models
4. **Model Evaluation**: Performance metrics and visualizations
5. **Feature Importance**: Analysis of which features contribute most to predictions

## Installation
To run this project, you'll need:
- Python 3.6+
- Required libraries:
pip install pandas numpy matplotlib seaborn scikit-learn

text

## Usage
1. Clone the repository
2. Ensure the dataset (`Housing.csv`) is in the same directory
3. Run the Jupyter notebook or Python script

## Results
### Model Performance Comparison
| Model                | MAE       | RMSE      | R2 Score |
|----------------------|-----------|-----------|----------|
| Linear Regression    | 1,100,000 | 1,400,000 | 0.65     |
| Gradient Boosting    | 800,000   | 1,100,000 | 0.78     |

### Key Findings
- Gradient Boosting outperformed Linear Regression
- Most important features:
1. Area (square footage)
2. Number of bathrooms
3. Air conditioning availability
4. Number of bedrooms
5. Location preference (prefarea)

## Visualizations
The project includes several visualizations:
- Distribution plots for all numerical features
- Count plots for categorical features
- Scatter plots showing relationships with price
- Box plots showing price distribution across categories
- Actual vs predicted price plots
- Residual distribution plots
- Feature importance chart

## Future Improvements
- Hyperparameter tuning for Gradient Boosting
- Experiment with other algorithms (Random Forest, Neural Networks)
- More sophisticated feature engineering
- Cross-validation for more robust evaluation

## Author
Ihsan Ullah

