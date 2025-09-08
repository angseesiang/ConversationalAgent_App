import pandas as pd

class DataPreprocessor:
    """Class for data loading and preprocessing."""

    def load_data(self, filepath: str) -> pd.DataFrame:
        """
        Returns:
            pd.DataFrame: Loaded data.
        """
        data = pd.read_csv(filepath)
        return data

    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess the data by cleaning and normalizing.

        Args:
            data (pd.DataFrame): Raw data.

        Returns:
            pd.DataFrame: Preprocessed data.
        """

        # Example preprocessing steps
        data = data.dropna()  # Remove missing values
        data['text'] = data['text'].str.lower()  # Convert text to lowercase
        return data

