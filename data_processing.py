import pandas as pd
# Read data.csv
data_df = pd.read_csv('data.csv')

# Read domains_location.csv
domains_df = pd.read_csv('domains_location.csv')

# Read traffic_data.csv
traffic_df = pd.read_csv('traffic.csv')
# Display the first few rows of each dataframe
print("Data.csv:")
print(data_df.head())

print("\nDomains_location.csv:")
print(domains_df.head())

print("\nTraffic.csv:")
print(traffic_df.head())

# Get summary statistics for numeric columns
print("\nSummary statistics for data.csv:")
print(data_df.describe())

# Check data types and missing values
print("\nData types and missing values for data.csv:")
print(data_df.info())
# Check dimensions of the dataframes
print("Data dimensions:", data_df.shape)
print("Domains dimensions:", domains_df.shape)
print("Traffic dimensions:", traffic_df.shape)

# View the first few rows of each dataframe
print("\nData head:\n", data_df.head())
print("\nDomains head:\n", domains_df.head())
print("\nTraffic head:\n", traffic_df.head())
# Summary statistics for data dataframe
print("\nData summary statistics:\n", data_df.describe())
# Information about data types and missing values
print("\nData info:\n", data_df.info())
