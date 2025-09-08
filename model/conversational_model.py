import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class ConversationalModel:
    """Class for handling the conversational model."""

    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model.eval()

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the model.

        Args:
            prompt (str): User input prompt.

        Returns:
            str: Generated response from the model.
        """
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=50, num_return_sequences=1)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
