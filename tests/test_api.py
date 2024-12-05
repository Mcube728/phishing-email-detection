import unittest
import json
from api import app

import warnings
warnings.filterwarnings('ignore')

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def tearDown(self):
        pass
    
    def test_predict_no_urls(self):
        response = self.app.post('/predict', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('No URLs provided!', response.get_json()['error'])
    
    def test_predict_valid_url(self):
        # Replace 'http://example.com' with a valid URL you want to test
        response = self.app.post('/predict', data=json.dumps({'urls': ['https://youtube.com']}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('urls', data)
        self.assertEqual(len(data['urls']), 1)
        self.assertIn('url', data['urls'][0])
        self.assertIn('prediction', data['urls'][0])
        self.assertIn('message', data['urls'][0])

    def test_predict_empty_url_list(self):
        response = self.app.post('/predict', 
                                 data=json.dumps({'urls': []}), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['urls'], [])

if __name__ == '__main__':
    unittest.main()