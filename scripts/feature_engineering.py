import pandas as pd
import numpy as np

def create_features(filepath='data/processed/engineered_data.csv'):
    """Generate new features for analysis."""
    # Load the cleaned data
    logistics_df = pd.read_csv(filepath)

    # Feature: Cost per Mile
    logistics_df['Cost per Mile'] = logistics_df['Fuel Costs (USD)'] / logistics_df['Distance Traveled (miles)']
    
    # Add additional feature engineering steps here
    # Example: Delivery Efficiency (Distance per Time)
    logistics_df['Delivery Efficiency'] = logistics_df['Distance Traveled (miles)'] / logistics_df['Delivery Time (hours)']
    
    # Save the engineered data
    logistics_df.to_csv(filepath, index=False)
    print("Feature engineering complete.")
    
    return logistics_df

if __name__ == "__main__":
    # Run feature engineering on the specified file
    engineered_data = create_features('data/processed/engineered_data.csv')