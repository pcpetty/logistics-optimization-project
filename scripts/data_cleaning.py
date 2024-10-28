import pandas as pd

def load_data(filepath='data/logistics_df.csv'):
    """Load the dataset from the specified file path."""
    return pd.read_csv(filepath)

def clean_data(logistics_df):
    """Perform basic data cleaning tasks like handling missing values."""
    logistics_df = logistics_df.dropna()  # Example - drop missing values
    # Add other cleaning steps here
    return logistics_df

if __name__ == "__main__":
    # Example usage
    logistics_df = load_data('../data/raw/logistics_data.csv')
    logistics_df = clean_data(logistics_df)
    logistics_df.to_csv('../data/processed/cleaned_data.csv', index=False)
    print("Data cleaning complete.")