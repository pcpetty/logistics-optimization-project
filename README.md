# Logistics Optimization Project

![Screenshot 2025-01-05 at 15-56-05 riskrangerlogo webp (WEBP Image 1024 × 1024 pixels) — Scaled (75%)](https://github.com/user-attachments/assets/438ad3a7-6c11-41a3-8f83-177ec0cfc66f)

---

## Project Overview

This project is a comprehensive data science analysis designed to optimize logistics operations through predictive modeling and clustering techniques. Using a simulated dataset, we explore factors that impact operational costs, delivery efficiency, and customer satisfaction. The goal is to build predictive models and generate actionable insights to improve logistics and supply chain management.

The project is structured in four main phases:

1. **Exploratory Data Analysis (EDA)**
2. **Feature Engineering**
3. **Modeling**
4. **Results Analysis**

Each phase builds upon the previous one, resulting in a thorough understanding of logistics operations and actionable recommendations.

---

## Repository Structure

- **data/**
  - `raw/` - Contains raw data files (e.g., `logistics_df.csv`).
  - `processed/` - Contains processed and engineered data files (e.g., `cleaned_logistics_data.csv`, `engineered_data.csv`).
- **notebooks/**
  - `00_data_simulation.ipynb` - Notebook for simulating data (if applicable).
  - `01_data_exploration.ipynb` - Notebook for exploratory data analysis.
  - `02_feature_engineering.ipynb` - Notebook for feature engineering and dataset preparation.
  - `03_modeling.ipynb` - Notebook for training and evaluating predictive models.
  - `04_results_analysis.ipynb` - Notebook for analyzing model results and generating insights.
- **scripts/**
  - `data_cleaning.py` - Script for cleaning and preprocessing data.
  - `feature_engineering.py` - Script for engineering new features.
  - `modeling.py` - Script for training and evaluating models.
  - `utils.py` - Utility functions for data loading, saving, plotting, and directory management.
- **results/** - Stores generated plots, figures, and analysis tables.
  - `figures/` - Visualizations and plots.
  - `model_output/` - Model outputs and metrics.
  - `tables/` - Data tables and summaries.
- **README.md** - Overview and setup instructions (this file).
- **requirements.txt** - List of required Python packages for the project.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Recommended: Set up a virtual environment for the project

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/pcpetty/logistics-optimization-project.git
    cd logistics-optimization-project
    ```

2. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Project Phases and Notebooks

### 1. Exploratory Data Analysis (EDA)
The EDA notebook (`01_data_exploration.ipynb`) dives into the dataset, exploring the distribution of features such as **Distance Traveled**, **Fuel Costs**, **Customer Satisfaction**, and more. Clustering techniques like **K-Means** and **DBSCAN** are applied to identify natural groupings within the data, providing insights into potential optimizations.

### 2. Feature Engineering
In the feature engineering phase (`02_feature_engineering.ipynb`), we create new features that improve model performance. Examples include **Cost per Mile** and **Delivery Efficiency**, which quantify operational efficiency. This notebook standardizes and encodes categorical data to ensure compatibility with machine learning algorithms.

### 3. Modeling
The modeling notebook (`03_modeling.ipynb`) trains machine learning models to predict **Total Operational Cost (USD)**. We experiment with **Decision Trees** and **Random Forests** to find the most accurate model. Dimensionality reduction techniques such as **t-SNE** are used to visualize high-dimensional data and enhance interpretability.

### 4. Results Analysis
The results analysis notebook (`04_results_analysis.ipynb`) evaluates the models using metrics like **RMSE**, **MAE**, and **R²** scores. Feature importances are visualized to understand key drivers of operational costs, and clustering visualizations are revisited to provide actionable insights.

---

## Key Features and Analysis

1. **EDA and Clustering**: Visualizes distributions and relationships in the data, with insights into natural clusters for targeted optimization.
2. **Feature Engineering**: Creates new features like **Cost per Mile** and **Delivery Efficiency** to enhance model predictions.
3. **Predictive Modeling**: Employs Decision Trees and Random Forests to predict operational costs accurately.
4. **Results Analysis**: Evaluates model performance and identifies important features for cost reduction.

---

### Feature Engineering Example

```python
# Feature: Cost per Mile
df['Cost per Mile'] = df['Fuel Costs (USD)'] / df['Distance Traveled (miles)']

# Feature: Delivery Efficiency
df['Delivery Efficiency'] = df['Distance Traveled (miles)'] / df['Delivery Time (hours)']
```

---

### Model Training Example

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X = df[['Distance Traveled (miles)', 'Truck Condition', 'Driver Ratings', 'Load Weight (tons)', 'Cost per Mile']]
y = df['Total Operational Cost (USD)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
```

---

### Conclusion

This project demonstrates the application of data science techniques to optimize logistics operations. By analyzing key factors that influence operational costs and delivery efficiency, we provide a framework for actionable insights. The combination of clustering, feature engineering, predictive modeling, and detailed results analysis offers a comprehensive solution to reduce logistics costs and improve service quality.

Through data-driven insights and model predictions, this project paves the way for logistics and supply chain optimization, ultimately benefiting businesses with more efficient and cost-effective operations.

---

### License

This project is licensed under the MIT License - see the LICENSE file for details.

---

### Acknowledgments

This project uses simulated data to represent logistics operations and has been structured for educational and demonstrative purposes in the field of data science and machine learning.

---

### Contact

For questions, contact [Cole Petty](colepetty57@gmail.com).
