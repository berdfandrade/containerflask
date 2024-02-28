import unittest
from app import app
import os
import sys

# diretório atual
diretorio_atual = os.path.dirname(__file__)

# Adiciona o diretório pai ao PATH do Python
diretorio_pai = os.path.abspath(os.path.join(diretorio_atual, os.pardir))
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, world!"})


if __name__ == "__main__":
    unittest.main()
