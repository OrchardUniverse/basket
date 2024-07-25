import unittest
from io import StringIO
from unittest.mock import patch
from maas_config import MaaSConfig, MaaSProvider

class TestMaaSProvider(unittest.TestCase):
    def test_init(self):
        provider = MaaSProvider("TestProvider", "https://test.com", ["model1", "model2"])
        self.assertEqual(provider.name, "TestProvider")
        self.assertEqual(provider.url, "https://test.com")
        self.assertEqual(provider.models, ["model1", "model2"])

    def test_init_no_models(self):
        provider = MaaSProvider("TestProvider", "https://test.com")
        self.assertEqual(provider.name, "TestProvider")
        self.assertEqual(provider.url, "https://test.com")
        self.assertEqual(provider.models, [])

class TestMaaSConfig(unittest.TestCase):
    @patch('builtins.open')
    def test_load_config(self, mock_open):
        yaml_content = """
        maas:
          - name: OpenAI
            url: https://api.openai.com/v1
          - gpt-3.5-turbo-0125
          - text-embedding-3-small
          - name: DeepSeek
            url: https://api.deepseek.com/v1
          - deepseek-7b-v1
          - deepseek-chat
        """
        mock_open.return_value = StringIO(yaml_content)
        
        config = MaaSConfig("dummy_file.yaml")
        
        self.assertEqual(len(config.providers), 2)
        
        openai = config.get_provider("OpenAI")
        self.assertIsNotNone(openai)
        self.assertEqual(openai.url, "https://api.openai.com/v1")
        self.assertEqual(openai.models, ["gpt-3.5-turbo-0125", "text-embedding-3-small"])
        
        deepseek = config.get_provider("DeepSeek")
        self.assertIsNotNone(deepseek)
        self.assertEqual(deepseek.url, "https://api.deepseek.com/v1")
        self.assertEqual(deepseek.models, ["deepseek-7b-v1", "deepseek-chat"])

    @patch('builtins.open')
    def test_list_providers(self, mock_open):
        yaml_content = """
        maas:
          - name: Provider1
            url: https://provider1.com
          - name: Provider2
            url: https://provider2.com
        """
        mock_open.return_value = StringIO(yaml_content)
        
        config = MaaSConfig("dummy_file.yaml")
        providers = config.list_providers()
        
        self.assertEqual(providers, ["Provider1", "Provider2"])

    @patch('builtins.open')
    def test_get_provider_url(self, mock_open):
        yaml_content = """
        maas:
          - name: TestProvider
            url: https://test.com
        """
        mock_open.return_value = StringIO(yaml_content)
        
        config = MaaSConfig("dummy_file.yaml")
        url = config.get_provider_url("TestProvider")
        
        self.assertEqual(url, "https://test.com")

    @patch('builtins.open')
    def test_get_provider_models(self, mock_open):
        yaml_content = """
        maas:
          - name: TestProvider
            url: https://test.com
          - model1
          - model2
        """
        mock_open.return_value = StringIO(yaml_content)
        
        config = MaaSConfig("dummy_file.yaml")
        models = config.get_provider_models("TestProvider")
        
        self.assertEqual(models, ["model1", "model2"])

    @patch('builtins.open')
    def test_provider_not_found(self, mock_open):
        yaml_content = """
        maas:
          - name: TestProvider
            url: https://test.com
        """
        mock_open.return_value = StringIO(yaml_content)
        
        config = MaaSConfig("dummy_file.yaml")
        
        self.assertIsNone(config.get_provider("NonexistentProvider"))
        self.assertIsNone(config.get_provider_url("NonexistentProvider"))
        self.assertIsNone(config.get_provider_models("NonexistentProvider"))

if __name__ == '__main__':
    unittest.main()