import yaml
from typing import List, Dict, Optional

class MaaSProvider:
    def __init__(self, name: str, url: str, models: Optional[List[str]] = None):
        self.name: str = name
        self.url: str = url
        self.models: List[str] = models or []

class MaaSConfig:
    def __init__(self, yaml_file: str):
        self.providers: List[MaaSProvider] = []
        self._load_config(yaml_file)

    def _load_config(self, yaml_file: str) -> None:
        with open(yaml_file, 'r') as file:
            config = yaml.safe_load(file)
        
        maas_list = config.get('maas', [])
        current_provider = None

        for item in maas_list:
            if isinstance(item, dict) and 'name' in item:
                if current_provider:
                    self.providers.append(current_provider)
                current_provider = MaaSProvider(item['name'], item['url'])
            elif isinstance(item, str) and current_provider:
                current_provider.models.append(item)

        if current_provider:
            self.providers.append(current_provider)

    def get_provider(self, name: str) -> Optional[MaaSProvider]:
        for provider in self.providers:
            if provider.name == name:
                return provider
        return None

    def list_providers(self) -> List[str]:
        return [provider.name for provider in self.providers]

    def get_provider_url(self, name: str) -> Optional[str]:
        provider = self.get_provider(name)
        return provider.url if provider else None

    def get_provider_models(self, name: str) -> Optional[List[str]]:
        provider = self.get_provider(name)
        return provider.models if provider else None


if __name__ == "__main__":
    config = MaaSConfig("maas_config.yaml")
    
    print("Available providers:", config.list_providers())
    
    openai_provider = config.get_provider("OpenAI")
    if openai_provider:
        print(f"OpenAI URL: {openai_provider.url}")
        print(f"OpenAI Models: {openai_provider.models}")
    
    deepseek_models = config.get_provider_models("DeepSeek")
    if deepseek_models:
        print(f"DeepSeek Models: {deepseek_models}")