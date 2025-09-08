import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class Evaluator:
    """Class for evaluating the model performance."""

    def evaluate(self, model, test_data: pd.DataFrame) -> dict:
        """
        Evaluate the model using test data.

        Args:
            model: Trained model.
            test_data (pd.DataFrame): Test data.

        Returns:
            dict: Evaluation metrics.
        """
        y_true = test_data['true_labels']
        y_pred = test_data['predicted_labels']

        metrics = {
            "accuracy": accuracy_score(y_true, y_pred),
            "precision": precision_score(y_true, y_pred, average='weighted'),
            "recall": recall_score(y_true, y_pred, average='weighted'),
            "f1_score": f1_score(y_true, y_pred, average='weighted')
        }
        return metrics

