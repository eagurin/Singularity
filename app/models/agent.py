## app/models/agent.py

from transformers import pipeline

class Agent:
    def __init__(self, name: str, model_name_or_path: str):
        """
        Initialize an Agent instance with a name and a model.

        Args:
            name (str): The name of the agent.
            model_name_or_path (str): The name or path of the model to be used for processing text.
        """
        self.name = name
        # Initialize the NLP model pipeline for text processing
        self.nlp_pipeline = pipeline("text-classification", model=model_name_or_path)

    def process_text(self, text: str) -> dict:
        """
        Process the given text using the agent's NLP model.

        Args:
            text (str): The text to be processed.

        Returns:
            dict: The result of the text processing, including the model's predictions.
        """
        # Use the NLP pipeline to process the text and obtain predictions
        predictions = self.nlp_pipeline(text)
        # Return the processed text along with the model's predictions
        return {"processed_text": text, "predictions": predictions, "model": self.name}
