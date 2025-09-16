import unittest
import json
from app import app

class TestChatbot(unittest.TestCase):
    """Unit test class for testing the chatbot application."""

    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()

    def test_chat(self):
        """Test the chat endpoint."""
        response = self.app.post('/chat', 
                                 data=json.dumps({"message": "Hello"}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("response", data)
        self.assertIsInstance(data["response"], str)

if __name__ == '__main__':
    unittest.main()
