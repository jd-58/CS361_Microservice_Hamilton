import unittest
from affirmation_microservice import app

class TestAffirmationMicroservice(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_happy_mood(self):
        response = self.app.post('/get_affirmation', json={"mood": "happy"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("affirmation", response.get_json())

    def test_unrecognized_mood(self):
        response = self.app.post('/get_affirmation', json={"mood": "unknown"})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

if __name__ == "__main__":
    unittest.main()