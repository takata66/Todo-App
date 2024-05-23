import unittest
import json
import time
from http.server import HTTPServer
from threading import Thread
from app import RequestHandler
import requests

class TodoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(('localhost', 8000), RequestHandler)
        cls.thread = Thread(target=cls.server.serve_forever)
        cls.thread.start()
        time.sleep(1)  # добавляем задержку

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join()

    def test_add_todo(self):
        response = self._make_request('/todos', 'POST', {'title': 'Test Todo'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('title', response.json())
        self.assertEqual(response.json()['title'], 'Test Todo')

    def _make_request(self, path, method, data=None):
        url = f'http://localhost:8000{path}'
        headers = {'Content-Type': 'application/json'}
        if method == 'POST':
            return requests.post(url, headers=headers, data=json.dumps(data))
        elif method == 'PUT':
            return requests.put(url, headers=headers, data=json.dumps(data))
        elif method == 'GET':
            return requests.get(url, headers=headers)
        elif method == 'DELETE':
            return requests.delete(url, headers=headers)

if __name__ == '__main__':
    unittest.main()
