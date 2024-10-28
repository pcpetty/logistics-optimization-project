import pandas as pd
import numpy as np

def create_features(df):
    """Generate new features for analysis."""
    # Example feature: Cost per mile
    df['Cost per Mile'] = df['Fuel Costs (USD)'] / df['Distance Traveled (miles)']
    # Add additional feature engineering steps here
    return df

if __name__ == "__main__":
    # Load the cleaned data
    df = pd.read_csv('../data/processed/cleaned_data.csv')
    df = create_features(df)
    df.to_csv('../data/processed/engineered_data.csv', index=False)
    print("Feature engineering complete.")