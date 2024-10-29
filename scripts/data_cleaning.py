import pandas as pd

def load_data(filepath='data/raw/logistics_df.csv'):
    """Load the dataset from the specified file path."""
    return pd.read_csv(filepath)

def clean_data(logistics_df):
    """Perform basic data cleaning tasks."""
    # Drop rows with any missing values
    logistics_df = logistics_df.dropna()
    
    # Remove duplicates, if any
    logistics_df = logistics_df.drop_duplicates()
    
    # Ensure correct data types (example: converting dates or numeric columns)
    # logistics_df['Date Column'] = pd.to_datetime(logistics_df['Date Column'], errors='coerce')
    # logistics_df['Numeric Column'] = pd.to_numeric(logistics_df['Numeric Column'], errors='coerce')
    
    # Reset the index after dropping rows
    logistics_df.reset_index(drop=True, inplace=True)
    
    return logistics_df

if __name__ == "__main__":
    # Load the raw data
    logistics_df = load_data('data/raw/logistics_df.csv')
    
    # Clean the data
    logistics_df = clean_data(logistics_df)
    
    # Save the cleaned data
    logistics_df.to_csv('data/processed/cleaned_logistics_data.csv', index=False)
    print("Data cleaning complete.")
