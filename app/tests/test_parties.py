import unittest
import os
import json
from app import create_app


class TestPartiesEndpoints(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.party = {                
                        "name" : "UCL Party" ,
                        "hqAddress" : "Pennsylnvania" ,
                        "logoUrl" : "Zen.png"
                        }
        self.party_err = {                
                        "name" : "" ,
                        "hqAddress" : "Pennsylnvania" ,
                        "logoUrl" : "Zen.png"
                        }

        self.party_name = {"name":"Liberal Party"}
        self.party_edit_err = {"name":""}


    def test_api_can_get_all_parties(self):
        """Test endpoint that fetches all parties"""

        res = self.client().get(path='/api/v1/parties/', content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Democratic Party', str(res.data))

    def test_api_can_get_party_by_id(self):
        """Test endpoint that fetches a particular party"""

        res = self.client().get('/api/v1/parties/1')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Democratic Party', str(res.data))

    def test_api_can_create_party(self):
        """Test endpoint that posts a particular party"""
        
        res = self.client().post('/api/v1/parties/', json=self.party)
        self.assertEqual(res.status_code, 201)
        self.assertIn('UCL Party', str(res.data))


    def test_party_deletion(self):
        """Test endpoint that deletes a particular party"""

        res = self.client().delete('/api/v1/parties/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/api/v1/parties/1')
        self.assertEqual(result.status_code, 404)

    def test_api_can_edit_party(self):
        """Test endpoint that edits a particular party"""

        res = self.client().patch('/api/v1/parties/3/name', json=self.party_name)
        self.assertEqual(res.status_code, 200)
        self.assertIn('Liberal Party', str(res.data))

    
    def test_api_response_for_non_existing_resource(self):
        """Test endpoints response for non existing resource"""

        res = self.client().get('/api/v1/parties/8')
        self.assertEqual(res.status_code, 404)
        res = self.client().delete('/api/v1/parties/8')
        self.assertEqual(res.status_code, 404)
        res = self.client().patch('/api/v1/parties/8/name', json=self.party_name)
        self.assertEqual(res.status_code, 404)
    
    def test_api_raises_error_on_invalid_input(self):
        """Test endpoints raise error upon provision of invalid input"""
        
        res = self.client().patch('/api/v1/parties/3/name', json=self.party_edit_err)
        self.assertEqual(res.status_code, 400)
        res = self.client().post('/api/v1/parties/', json=self.party_err)
        self.assertEqual(res.status_code, 400)



if __name__ == "__main__":
    unittest.main()        