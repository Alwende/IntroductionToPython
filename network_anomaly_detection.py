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