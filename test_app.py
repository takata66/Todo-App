import unittest
import json
import time
from http.server import HTTPServer
from threading import Thread
from app import RequestHandler
import requests

class TodoTestCase(unittest.TestCase):
    """
    Test case for the TODO application.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test server and start it in a separate thread.
        """
        cls.server = HTTPServer(('localhost', 8000), RequestHandler)
        cls.thread = Thread(target=cls.server.serve_forever)
        cls.thread.start()
        time.sleep(1)  # добавляем задержку

    @classmethod
    def tearDownClass(cls):
        """
        Shut down the test server and wait for the thread to finish.
        """
        cls.server.shutdown()
        cls.thread.join()

    def test_add_todo(self):
        """
        Test adding a new TODO item.
        """
        response = self._make_request('/todos', 'POST', {'title': 'Test Todo'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('title', response.json())
        self.assertEqual(response.json()['title'], 'Test Todo')

    def _make_request(self, path, method, data=None):
        """
        Make an HTTP request to the test server.

        :param path: The path of the request.
        :param method: The HTTP method (GET, POST, PUT, DELETE).
        :param data: The data to be sent with the request (default is None).
        :return: The response from the server.
        """
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
