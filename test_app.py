import unittest
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        
    def tearDown(self):
        pass
        
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'I am almost a Devops Engineer!')

if __name__ == '__main__':
    unittest.main()
