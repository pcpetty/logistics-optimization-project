# Logistics Optimization Project

## Introduction
This project focuses on optimizing logistics operations by identifying high-cost routes, analyzing the impact of traffic and weather conditions on fuel efficiency, and predicting delays. The goal is to derive actionable insights that reduce operational costs and improve delivery efficiency.

## Project Structure
- **data/**: Contains raw and processed data files.
- **notebooks/**: Jupyter notebooks for EDA, feature engineering, modeling, and result analysis.
- **scripts/**: Modular scripts for data processing, feature engineering, and model training.
- **results/**: Contains figures, saved models, and summary tables.
- **README.md**: Overview and instructions for the project.
- **requirements.txt**: List of required dependencies.

## Methodology
1. **Data Exploration**: Analyze key metrics like fuel costs and delivery times to understand baseline performance.
2. **Feature Engineering**: Create domain-specific features such as Weather Severity Score, Driver Consistency Score, and Idle Time Impact Score.
3. **Modeling**: Use regression and classification models to predict operational costs and on-time delivery performance.
4. **Results and Insights**: Summarize findings with actionable recommendations for reducing costs and improving efficiency.

## Results
- **Top Cost-Drivers**: Truck condition and distance traveled were identified as primary factors influencing operational costs.
- **Impact of Traffic and Weather**: Severe traffic and adverse weather significantly increase delays and idle time, resulting in higher fuel costs.
- **Predictive Model Performance**: Achieved an RMSE of 354.9 on the operational cost prediction model, indicating reasonable accuracy for cost prediction.

## Getting Started
To reproduce this project:
1. Clone the repository:
   ```bash
   git clone https://github.com/pcpetty/logistics-optimization-project.git
   cd logistics-optimization-project

## Contact
For questions, contact [Cole Petty](colepetty57@gmail.com).