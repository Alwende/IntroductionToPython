# Network Anomalies Detection

## Project Overview
The Network Anomalies Detection system uses machine learning techniques to detect anomalies in network traffic. The system analyzes network traffic patterns and identifies abnormal behaviors or activities that may indicate potential security threats or breaches. It utilizes both supervised and unsupervised machine learning algorithms to learn from historical network data and detect deviations from normal network behavior.

The system generates real-time alerts and notifications, enabling network administrators to proactively mitigate security risks. The project aims to enhance network security by leveraging machine learning to effectively detect and respond to network anomalies.

## Project Components
1. **Data Collection:** Collect network traffic data for training and testing the machine learning models.
2. **Data Preprocessing:** Clean and preprocess the data to make it suitable for machine learning.
3. **Feature Engineering:** Extract relevant features from the network traffic data.
4. **Model Training:** Train supervised and unsupervised machine learning models on the preprocessed data.
5. **Anomaly Detection:** Use the trained models to detect anomalies in real-time network traffic.
6. **Alert Generation:** Generate real-time alerts and notifications for detected anomalies.
7. **Visualization:** Visualize the network traffic and detected anomalies.
## Tools and Libraries
- **Python:** Programming language for implementing the project.
- **Pandas:** Data manipulation and analysis.
- **NumPy:** Numerical operations.
- **Scikit-learn:** Machine learning algorithms.
- **Matplotlib/Seaborn:** Data visualization.

## Installation
To run this project, you need to have Python installed on your system. You also need to install the required libraries. You can install the libraries using pip:

```sh
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Improvements to the Network Anomaly Detection Script

The code has been improved in several ways to make it more robust, maintainable, and professional. Here are the key modifications and enhancements:

### 1. **Logging:**
   - Added logging to track the execution of the script and any potential issues.
   - Configured logging to display timestamps, log levels, and messages.

### 2. **Error Handling:**
   - Implemented error handling using try-except blocks to manage potential issues gracefully.
   - Logged error messages and exited the script if an exception occurs.

### 3. **Modularization:**
   - Broke down the code into functions to improve readability and maintainability.
   - Created separate functions for loading data, preprocessing data, training the model, detecting anomalies, and visualizing anomalies.

### 4. **Configuration:**
   - Used a configuration section to define the dataset URL and column names.
   - Made it easier to modify the configuration without changing the core logic.

### 5. **Data Preprocessing:**
   - Encoded categorical features and normalized the data to make it suitable for machine learning.

### 6. **Model Training:**
   - Trained the Isolation Forest model for anomaly detection.
   - Configured the contamination rate and random state for reproducibility.

### 7. **Anomaly Detection:**
   - Used the trained model to detect anomalies in the network traffic data.
   - Added the anomaly labels to the data and filtered the anomalies.

### 8. **Visualization:**
   - Visualized the network traffic and detected anomalies using a scatter plot.
   - Configured the plot with titles, labels, and legends for better readability.

### Summary of the Improved Code

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(url, columns):
    try:
        data = pd.read_csv(url, names=columns)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        sys.exit(1)

def preprocess_data(data, categorical_features):
    try:
        encoder = LabelEncoder()
        for feature in categorical_features:
            data[feature] = encoder.fit_transform(data[feature])
        X = data.drop(columns=["label"])
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        logging.info("Data preprocessing completed.")
        return X_scaled, data
    except Exception as e:
        logging.error(f"Error preprocessing data: {e}")
        sys.exit(1)

def train_model(X_scaled, contamination=0.01):
    try:
        model = IsolationForest(contamination=contamination, random_state=42)
        model.fit(X_scaled)
        logging.info("Model trained successfully.")
        return model
    except Exception as e:
        logging.error(f"Error training model: {e}")
        sys.exit(1)

def detect_anomalies(model, X_scaled, data):
    try:
        anomalies = model.predict(X_scaled)
        data["anomaly"] = anomalies
        anomalies_data = data[data["anomaly"] == -1]
        logging.info("Anomalies detected.")
        return anomalies_data
    except Exception as e:
        logging.error(f"Error detecting anomalies: {e}")
        sys.exit(1)

def visualize_anomalies(data):
    try:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="src_bytes", y="dst_bytes", hue="anomaly", data=data, palette={1: "blue", -1: "red"})
        plt.title("Network Traffic Anomalies")
        plt.xlabel("Source Bytes")
        plt.ylabel("Destination Bytes")
        plt.legend(["Normal", "Anomaly"])
        plt.show()
        logging.info("Anomalies visualized.")
    except Exception as e:
        logging.error(f"Error visualizing anomalies: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Configuration
    url = "http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz"
    columns = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment", "urgent",
               "hot", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
               "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login",
               "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
               "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate",
               "dst_host_diff_srv_rate", "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
               "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"]
    categorical_features = ["protocol_type", "service", "flag"]

    # Load and preprocess data
    data = load_data(url, columns)
    X_scaled, data = preprocess_data(data, categorical_features)

    # Train model
    model = train_model(X_scaled)

    # Detect anomalies
    anomalies_data = detect_anomalies(model, X_scaled, data)
    print("Anomalies detected:")
    print(anomalies_data)

    # Visualize anomalies
    visualize_anomalies(data)
```
These improvements make the code more robust, maintainable, and professional, which is important when sharing it with potential employers for cybersecurity roles.