import pandas as pd
import joblib  # For saving and loading models
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Utility to load raw data
def load_raw_data(filepath='../data/raw/logistics_df.csv'):
    """Loads raw data from the specified file path."""
    try:
        df = pd.read_csv(filepath)
        print(f"Raw data loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        print(f"File not found at {filepath}")
        return None

# Utility to load cleaned data

def load_cleaned_data(filepath='../data/processed/cleaned_logistics_data.csv'):
    """Loads cleaned data from the specified file path."""
    try:
        df = pd.read_csv(filepath)
        print(f"Cleaned data loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        print(f"File not found at {filepath}")
        return None

# Utility to load engineered data
def load_engineered_data(filepath='../data/processed/engineered_data.csv'):
    """Loads engineered data from the specified file path."""
    try:
        df = pd.read_csv(filepath)
        print(f"Engineered data loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        print(f"File not found at {filepath}")
        return None

# Utility to save processed data
def save_data(df, filepath):
    """Saves a pandas DataFrame to a CSV file."""
    try:
        # Ensure directory exists
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory created at {directory}")

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
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    plt.show()

def plot_numeric_correlation_heatmap(df, title="Correlation Heatmap"):
    """Plots a correlation heatmap for numeric features in a DataFrame."""
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    # Calculate the correlation matrix
    corr_matrix = numeric_df.corr()
    # Plot the heatmap
    plt.figure(figsize=(12, 8))
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

def save_plot(fig, filename, folder="results/figures"):
    """Save a matplotlib figure to the specified folder."""
    ensure_dir(folder)
    fig.savefig(f"{folder}/{filename}", dpi=300, bbox_inches="tight")
    plt.close(fig)  # Close figure after saving

def save_table(df, filename, folder="results/model_output"):
    """Save a pandas DataFrame to a specified folder as CSV."""
    ensure_dir(folder)
    df.to_csv(f"{folder}/{filename}", index=False)

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