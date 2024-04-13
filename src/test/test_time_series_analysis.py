import unittest
import pandas as pd
from src.time_series_analysis import load_data, plot_time_series, calculate_statistics, detect_trends

class TestTimeSeriesAnalysis(unittest.TestCase):
    def setUp(self):
        # Create sample time series data
        dates = pd.date_range('2022-01-01', periods=100)
        values = [i for i in range(100)]
        self.time_series_data = pd.DataFrame({'date': dates, 'value': values})
        self.time_series_data.set_index('date', inplace=True)

    def test_load_data(self):
        # Test if data is loaded successfully
        expected_columns = ['value']
        loaded_data = load_data("time_series_data.csv")
        self.assertTrue(all(col in loaded_data.columns for col in expected_columns))

    def test_plot_time_series(self):
        # Test if plot is generated successfully
        plot_time_series(self.time_series_data, 'value')  # Just check if no error is raised

    def test_calculate_statistics(self):
        # Test if statistics are calculated successfully
        stats = calculate_statistics(self.time_series_data)
        self.assertIsNotNone(stats)

    def test_detect_trends(self):
        # Test if trend detection works
        detect_trends(self.time_series_data)  # Just check if no error is raised

if __name__ == '__main__':
    unittest.main()
