import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(data):
    """
    Trains a Random Forest model on the provided data.

    Args:
        data (pd.DataFrame): The dataset containing features and the target label.

    Returns:
        RandomForestClassifier: The trained model.
    """
    X = data.drop('threat_label', axis=1)
    y = data['threat_label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    return model

def save_model(model, filename):
    """
    Saves the trained model to a file.

    Args:
        model (RandomForestClassifier): The trained model.
        filename (str): The file path to save the model.
    """
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

def load_model(filename):
    """
    Loads a trained model from a file.

    Args:
        filename (str): The file path to load the model from.

    Returns:
        RandomForestClassifier: The loaded model.
    """
    model = joblib.load(filename)
    print(f"Model loaded from {filename}")
    return model

def predict(model, input_data):
    """
    Makes predictions using the trained model.

    Args:
        model (RandomForestClassifier): The trained model.
        input_data (pd.DataFrame): The input data for prediction.

    Returns:
        list: The predicted labels.
    """
    predictions = model.predict(input_data)
    return predictions

def main():
    # Load the dataset
    data = pd.read_csv('access_data.csv')  # Ensure this file exists and is properly formatted

    # Train the model
    model = train_model(data)

    # Save the trained model
    save_model(model, 'access_control_model.pkl')

    # Load the model for testing
    loaded_model = load_model('access_control_model.pkl')

    # Example prediction
    sample_data = data.drop('threat_label', axis=1).iloc[:5]  # Use the first 5 rows as sample input
    predictions = predict(loaded_model, sample_data)
    print("\nSample Predictions:", predictions)

if __name__ == '__main__':
    main()