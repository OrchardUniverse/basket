import unittest
from model_client import ModelClient

class TestModelClient(unittest.TestCase):

    def setUp(self):
        self.client = ModelClient()

    def test_init(self):
        self.assertEqual(self.client.maas, "")
        self.assertEqual(self.client.model, "")

    def test_init_with_values(self):
        client = ModelClient("test_maas", "test_model")
        self.assertEqual(client.maas, "test_maas")
        self.assertEqual(client.model, "test_model")

    def test_set_get_maas(self):
        self.client.set_maas("new_maas")
        self.assertEqual(self.client.get_maas(), "new_maas")

    def test_set_get_model(self):
        self.client.set_model("new_model")
        self.assertEqual(self.client.get_model(), "new_model")

    def test_property_maas(self):
        self.client.maas = "property_maas"
        self.assertEqual(self.client.maas, "property_maas")

    def test_property_model(self):
        self.client.model = "property_model"
        self.assertEqual(self.client.model, "property_model")

    def test_invalid_maas_type(self):
        with self.assertRaises(TypeError):
            self.client.maas = 123

    def test_invalid_model_type(self):
        with self.assertRaises(TypeError):
            self.client.model = 456

    def test_empty_string_allowed(self):
        self.client.maas = ""
        self.client.model = ""
        self.assertEqual(self.client.maas, "")
        self.assertEqual(self.client.model, "")

if __name__ == '__main__':
    unittest.main()