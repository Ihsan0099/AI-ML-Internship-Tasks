**🫀 Task 03 – Heart Disease Prediction**
**🎯 Objective**
Build a machine learning model to predict whether a person is at risk of heart disease based on health-related features.

**📦 Dataset**
Source: Heart Disease UCI Dataset
Format: CSV
Target Variable: target (1 = heart disease, 0 = no heart disease)
Features Include:
Age, Sex, Chest Pain Type, Resting BP, Cholesterol
Fasting Blood Sugar, Max Heart Rate, ST Depression
Exercise Induced Angina, etc.
**🧠 Models Used**
Logistic Regression
Decision Tree Classifier
**🛠️ Workflow Steps**
Data Cleaning
Checked for null values
Verified data types and range

**Exploratory Data Analysis (EDA**)
Pairplots, heatmaps, distribution plots
Class balance using countplot
Outlier & correlation inspection
**Preprocessing**

Feature-target split (X, y)
Train-test split (25% test)
StandardScaler for feature scaling

**Model Training**
Trained Logistic Regression (max_iter=1000)
Trained Decision Tree (default params)

**Evaluation**
Accuracy Score
Confusion Matrix
ROC Curve & AUC Score
Feature Importance

**📈 Key Results**
Metric	Logistic Regression	Decision Tree
Accuracy	~89%	~75%
ROC AUC	~0.93	~0.76
**📊 Visuals Included**
Correlation Heatmap
Scatterplots of Features vs Target
Countplot of Target Variable
Feature Importance Bar Charts
ROC Curve for both models
