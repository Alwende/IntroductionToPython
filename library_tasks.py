import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: Create a NumPy array of numbers from 1 to 10 and calculate the mean
numbers = np.arange(1, 11)
mean_value = np.mean(numbers)
print(f"NumPy array: {numbers}")
print(f"Mean of the array: {mean_value}")

# Task 2: Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())

# Task 3: Fetch data from a public API using requests and print a key piece of information
response = requests.get('https://api.github.com')
if response.status_code == 200:
    data = response.json()
    print("\nPublic API Data:")
    print(f"Current GitHub API rate limit: {data['rate_limit_url']}")
else:
    print("Failed to fetch data from the API")

# Task 4: Plot a simple line graph using matplotlib (e.g., a list of numbers)
plt.plot(numbers, label='Numbers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Simple Line Graph')
plt.legend()
plt.show()