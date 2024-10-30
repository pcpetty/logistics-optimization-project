import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(X, y):
    """Train a Random Forest model."""
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model using RMSE."""
    predictions = model.predict(X_test)
    rmse = mean_squared_error(y_test, predictions, squared=False)  # Set squared=False to get RMSE
    print(f"Root Mean Squared Error: {rmse}")

if __name__ == "__main__":
    # Example usage
    logistics_df = pd.read_csv('data/processed/engineered_data.csv')
    X = logistics_df[['Actual Distance (miles)', 'Cost per Mile']]
    y = logistics_df['Total Operational Cost (USD)']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    print("Modeling complete.")