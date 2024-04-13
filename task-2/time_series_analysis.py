import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load time series data from CSV file."""
    return pd.read_csv(file_path, parse_dates=['date'], index_col='date')

def plot_time_series(data, column_name):
    """Plot a time series."""
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data[column_name])
    plt.title('Time Series Analysis')
    plt.xlabel('Date')
    plt.ylabel(column_name)
    plt.grid(True)
    plt.show()

def calculate_statistics(data):
    """Calculate basic statistics of the time series."""
    return data.describe()

def detect_trends(data):
    """Detect trends in the time series."""
    # Example: calculate rolling mean and plot
    rolling_mean = data.rolling(window=30).mean()
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data, label='Original')
    plt.plot(rolling_mean.index, rolling_mean, label='Rolling Mean', color='red')
    plt.title('Trend Detection')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

# Define file path
file_path = "time_series_data.csv"

# Load time series data
time_series_data = load_data(file_path)

# Plot the time series
plot_time_series(time_series_data, 'value')

# Calculate basic statistics
stats = calculate_statistics(time_series_data)
print("Basic Statistics:")
print(stats)

# Detect trends in the time series
detect_trends(time_series_data)
