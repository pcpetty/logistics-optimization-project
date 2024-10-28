import pandas as pd

def load_data(filepath):
    """Load the dataset from the specified file path."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Perform basic data cleaning tasks like handling missing values."""
    df = df.dropna()  # Example - drop missing values
    # Add other cleaning steps here
    return df

if __name__ == "__main__":
    # Example usage
    df = load_data('../data/raw/logistics_data.csv')
    df = clean_data(df)
    df.to_csv('../data/processed/cleaned_data.csv', index=False)
    print("Data cleaning complete.")