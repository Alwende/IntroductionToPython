import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data Collection
# Load the dataset
url = "http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz"
columns = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment", "urgent",
           "hot", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
           "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login",
           "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
           "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate",
           "dst_host_diff_srv_rate", "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
           "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"]

data = pd.read_csv(url, names=columns)
print("Data loaded successfully.")
print(data.head())

# Step 2: Data Preprocessing
# Encode categorical features
categorical_features = ["protocol_type", "service", "flag"]
encoder = LabelEncoder()

for feature in categorical_features:
    data[feature] = encoder.fit_transform(data[feature])

# Drop the label column for unsupervised learning
X = data.drop(columns=["label"])

# Step 3: Feature Engineering
# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Model Training
# Train the Isolation Forest model
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X_scaled)
print("Model trained successfully.")

# Step 5: Anomaly Detection
# Predict anomalies
anomalies = model.predict(X_scaled)
data["anomaly"] = anomalies

# Filter the anomalies
anomalies_data = data[data["anomaly"] == -1]
print("Anomalies detected:")
print(anomalies_data)

# Step 6: Visualization
# Visualize the anomalies
plt.figure(figsize=(10, 6))
sns.scatterplot(x="src_bytes", y="dst_bytes", hue="anomaly", data=data, palette={1: "blue", -1: "red"})
plt.title("Network Traffic Anomalies")
plt.xlabel("Source Bytes")
plt.ylabel("Destination Bytes")
plt.legend(["Normal", "Anomaly"])
plt.show()