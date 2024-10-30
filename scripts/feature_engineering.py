import pandas as pd
import numpy as np

def create_features(filepath='data/processed/engineered_data.csv'):
    """Generate new features for analysis."""
    # Load the cleaned data
    logistics_df = pd.read_csv(filepath)
    # Replace instances of `Calculated Fuel Costs (USD)` with `Fuel Cost per Mile`
    # Example if calculating average or other metrics
    avg_fuel_cost_per_mile = df['Fuel Cost Per Mile'].mean()
    # Feature: Cost per Mile
    logistics_df['Cost per Mile'] = logistics_df['Calculated Fuel Cost (USD)'] / logistics_df['Actual Distance (miles)']
    # Replace instances of `Calculated Fuel Costs (USD)` with `Fuel Cost per Mile`
    # Add additional feature engineering steps here
    # Example: Delivery Efficiency (Distance per Time)
    logistics_df['Delivery Efficiency'] = logistics_df['Actual Distance (miles)'] / logistics_df['Delivery Duration (hours)']
    
    # Save the engineered data
    logistics_df.to_csv(filepath, index=False)
    print("Feature engineering complete.")
    
    return logistics_df

if __name__ == "__main__":
    # Run feature engineering on the specified file
    engineered_data = create_features('data/processed/engineered_data.csv')