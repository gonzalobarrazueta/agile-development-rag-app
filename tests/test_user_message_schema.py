import unittest
from marshmallow import ValidationError
from app.api.schemas.user_message_schema import UserMessageSchema

class TestUserMessageSchema(unittest.TestCase):

    def setUp(self):
        """Set up schema instance for use in multiple tests."""
        self.schema = UserMessageSchema()

    def test_valid_input(self):
        # Create an instance of the schema
        schema = UserMessageSchema()

        # Valid input data
        input_data = {
            "user_message": "Hello, world!"
        }

        # Validate the input and check if it passes
        result = schema.load(input_data)
        self.assertEqual(result, input_data)  # Ensure the output matches the input

    def test_invalid_data_type(self):
        # Invalid data type for 'user_message'
        input_data = {"user_message": 12345}
        with self.assertRaises(ValidationError) as context:
            self.schema.load(input_data)
        self.assertIn("user_message", context.exception.messages)

if __name__ == "__main__":
    unittest.main()
