# Unit tests for data_processing.py
import unittest
from data_processing import preprocess_text

class TestDataProcessing(unittest.TestCase):
    def test_preprocess_text(self):
        text = "This is a sample text for testing."
        preprocessed_text = preprocess_text(text)
        self.assertIsInstance(preprocessed_text, str)
        self.assertNotIn("sample", preprocessed_text)
        self.assertNotIn("testing", preprocessed_text)

if __name__ == '__main__':
    unittest.main()
