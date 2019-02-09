import unittest
import os
import json
from app import create_app


class TestOfficesEndpoints(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.office = {"type":"State",
                        "name":"Secretary of State"}
        self.office_err = {"type":"",
                        "name":"Secretary of State"}

    
    def test_api_can_get_all_offices(self):
        """Test endpoint that fetches all offices"""

        res = self.client().get(path='/api/v1/offices/', content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('President', str(res.data))

    def test_api_can_get_office_by_id(self):
        """Test endpoint that fetches a particular office"""

        res = self.client().get('/api/v1/offices/2')
        self.assertEqual(res.status_code, 200)
        self.assertIn('legislative', str(res.data))
        

    def test_api_can_create_office(self):
        """Test endpoint that posts a particular office"""

        res = self.client().post(path='/api/v1/offices/', json=self.office, content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Secretary of State', str(res.data))
    
    def test_api_response_for_non_existing_resource(self):
        """Test endpoints response for non existing resource"""

        res = self.client().get('/api/v1/offices/8')
        self.assertEqual(res.status_code, 404)


    def test_api_raises_error_on_invalid_input(self):
        """Test endpoints raise error upon provision of invalid input"""
        res = self.client().post(path='/api/v1/offices/', json=self.office_err, content_type='application/json')
        self.assertEqual(res.status_code, 400)
        

if __name__ == "__main__":
    unittest.main()