import unittest
from marshmallow import ValidationError
from app.api.schemas.user_message_schema import UserMessageSchema

class TestUserMessageSchema(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
