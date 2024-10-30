import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Utility to load data
def load_data(filepath, data_type="data"):
    """Loads data from a specified file path."""
    try:
        df = pd.read_csv(filepath)
        print(f"{data_type.capitalize()} loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        print(f"File not found at {filepath}")
        return None

# Utility to save data
def save_data(df, filepath):
    """Saves a DataFrame to a CSV file, ensuring directory existence."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        print(f"Data saved successfully to {filepath}")
    except Exception as e:
        print(f"Error saving data to {filepath}: {e}")

# Utility to save and load models
def save_model(model, filepath):
    """Saves a model using joblib."""
    try:
        joblib.dump(model, filepath)
        print(f"Model saved successfully to {filepath}")
    except Exception as e:
        print(f"Error saving model: {e}")

def load_model(filepath):
    """Loads a model using joblib."""
    try:
        model = joblib.load(filepath)
        print(f"Model loaded successfully from {filepath}")
        return model
    except FileNotFoundError:
        print(f"Model file not found at {filepath}")
        return None

# Utility to plot distribution of a column
def plot_distribution(df, column, title="Distribution Plot"):
    """Plots the distribution of a column in a DataFrame."""
    if column in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], kde=True, bins=30, edgecolor='black')
        plt.title(f"{title} for {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()
    else:
        print(f"Column '{column}' not found in DataFrame.")

# Utility to plot correlation heatmap
def plot_correlation_heatmap(df, title="Correlation Heatmap"):
    """Plots a correlation heatmap for numeric features in a DataFrame."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    plt.show()

# Utility to check missing values
def check_missing_values(df):
    """Prints missing values summary for DataFrame columns."""
    missing_values = df.isnull().sum()
    print("Missing Values by Column:")
    print(missing_values[missing_values > 0])

# Utility to save plots and tables
def save_plot(fig, filename, folder="../results/figures"):
    """Saves a matplotlib figure to a specified folder."""
    os.makedirs(folder, exist_ok=True)
    fig.savefig(f"{folder}/{filename}", dpi=300, bbox_inches="tight")
    plt.close(fig)

def save_table_output(df, filename, folder="../results/model_output"):
    """Saves a DataFrame as a CSV to a specified folder."""
    os.makedirs(folder, exist_ok=True)
    df.to_csv(f"{folder}/{filename}", index=False)
    print(f"Table saved to {folder}/{filename}")

# Example usage
# if __name__ == "__main__":
#     # Load raw, cleaned, and engineered data
#     raw_df = load_data('../data/raw/logistics_df.csv', "raw data")
#     cleaned_df = load_data('../data/processed/cleaned_logistics_data.csv', "cleaned data")
#     engineered_df = load_data('../data/processed/engineered_data.csv', "engineered data")

#     # Check for missing values in raw data
#     if raw_df is not None:
#         check_missing_values(raw_df)

#     # Plot distribution for a specific column in engineered data
#     if engineered_df is not None:
#         plot_distribution(engineered_df, 'Distance Traveled (miles)', title="Distance Traveled Distribution")

#     # Save an example of processed data
#     if raw_df is not None:
#         save_data(raw_df, '../data/processed/logistics_processed_data.csv')
#     # Example usage
# fig = plt.figure(figsize=(10, 6))
# sns.histplot(df['Fuel Costs (USD)'], bins=30, kde=True)
# save_plot(fig, "fuel_cost_histogram.png")

# # Save model performance table
# save_table(model_performance, "model_performance.csv")

# if __name__ == "__main__":
#     # Load raw data
#     raw_df = load_raw_data()
    
#     # Load cleaned data
#     cleaned_df = load_cleaned_data()
    
#     # Load engineered data
#     engineered_df = load_engineered_data()
    
#     Check for missing values in raw data if loaded successfully
#     if raw_df is not None:
#         check_missing_values(raw_df)
    
#     Plot a distribution for a known column in engineered data
#     if engineered_df is not None and 'Distance Traveled (miles)' in engineered_df.columns:
#         plot_distribution(engineered_df, 'Distance Traveled (miles)', title="Distance Traveled Distribution")
    
#     # Save an example processed data file (adjust DataFrame as needed)
#     if raw_df is not None:
#         save_data(raw_df, 'data/processed/logistics_processed_data.csv')
#     print("Data Processing Complete")