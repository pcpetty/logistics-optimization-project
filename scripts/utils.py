import pandas as pd
import joblib  # For saving and loading models
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Utility to load data
def load_data(filepath):
    """Loads a CSV file into a pandas DataFrame."""
    try:
        logistics_df = pd.read_csv('logistics_df.csv')
        print(f"Data loaded successfully from {filepath}")
        return logistics_df
    except FileNotFoundError:
        print(f"File not found at {filepath}")
        return None

# Utility to save processed data
def save_data(df, filepath):
    """Saves a pandas DataFrame to a CSV file."""
    try:
        df.to_csv(filepath, index=False)
        print(f"Data saved successfully to {filepath}")
    except Exception as e:
        print(f"Error saving data to {filepath}: {e}")

# Utility to save model
def save_model(model, filepath):
    """Saves a trained model to a file using joblib."""
    try:
        joblib.dump(model, filepath)
        print(f"Model saved successfully to {filepath}")
    except Exception as e:
        print(f"Error saving model: {e}")

# Utility to load model
def load_model(filepath):
    """Loads a trained model from a file using joblib."""
    try:
        model = joblib.load(filepath)
        print(f"Model loaded successfully from {filepath}")
        return model
    except FileNotFoundError:
        print(f"Model file not found at {filepath}")
        return None

# Utility to plot distribution of a column
def plot_distribution(df, column, title="Distribution Plot"):
    """Plots the distribution of a specific column in a DataFrame."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30, edgecolor='black')
    plt.title(f"{title} for {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# Utility to plot correlation heatmap
def plot_correlation_heatmap(df, title="Correlation Heatmap"):
    """Plots a correlation heatmap for numeric features in a DataFrame."""
    plt.figure(figsize=(12, 8))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    plt.show()

# Utility to check for missing values
def check_missing_values(df):
    """Checks for missing values in a DataFrame and prints the summary."""
    missing_values = df.isnull().sum()
    print("Missing Values by Column:")
    print(missing_values[missing_values > 0])

# Utility to create directory if it doesn’t exist
def ensure_dir(directory):
    """Creates a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory created at {directory}")
    else:
        print(f"Directory already exists at {directory}")

# Example usage
if __name__ == "__main__":
    # Load sample data
    df = load_data('../data/raw/sample_data.csv')
    
    # Check for missing values
    if df is not None:
        check_missing_values(df)
    
    # Plot a sample distribution
    if df is not None and 'SampleColumn' in df.columns:
        plot_distribution(df, 'SampleColumn', title="Sample Column Distribution")
    
    # Save processed data
    save_data(df, '../data/processed/processed_data.csv')
