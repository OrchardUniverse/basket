class ModelClient:
    def __init__(self, maas: str = "", model: str = ""):
        self._maas: str = maas
        self._model: str = model

    @property
    def maas(self) -> str:
        return self._maas

    @maas.setter
    def maas(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("maas must be a string")
        self._maas = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("model must be a string")
        self._model = value

    def set_maas(self, maas: str) -> None:
        self.maas = maas

    def get_maas(self) -> str:
        return self.maas

    def set_model(self, model: str) -> None:
        self.model = model

    def get_model(self) -> str:
        return self.model

# 使用示例
if __name__ == "__main__":
    client = ModelClient()
    
    client.set_maas("example_maas")
    print(f"MaaS: {client.get_maas()}")
    
    client.set_model("example_model")
    print(f"Model: {client.get_model()}")
    
    # 使用属性访问
    client.maas = "new_maas"
    print(f"New MaaS: {client.maas}")
    
    client.model = "new_model"
    print(f"New Model: {client.model}")
    
    # 类型检查示例
    try:
        client.maas = 123  # 这会引发 TypeError
    except TypeError as e:
        print(f"Error: {e}")
    
    # 初始化时设置值
    client_with_init = ModelClient("init_maas", "init_model")
    print(f"Initialized MaaS: {client_with_init.maas}")
    print(f"Initialized Model: {client_with_init.model}")