# Basket

## Introduction

Basket is the essential toolkit for seamless MaaS integration.

It provides a unified interface for interacting with different MaaS services, allowing developers to easily switch between different services without changing their code. It is the first free toolkit that allows developers to use LLM services without registering or paying for them. Know more about [FreeModel](https://github.com/OrchardUniverse/FreeModel).

- Fast and free to access Model as a Service
- Unified interface for interacting with different MaaS services
- Easy to use and integrate with existing projects
- Manage API KEY for MaaS and easy to switch
- Extensible and customizable for local and remote services
- One step to chat with LLM service without coding and configurating

Refer to more [documentation](https://orchardai.github.io/basket/).


## Install

```
pip install orchard-basket
```

## Usage

1. List all available MaaS

```
basket maas list
```

2. Choose the MaaS to use.

```
basket maas use FreeModel
```

3. List all available models

```
basket model list
```

4. Choose the model to use.

```
basket model use qwen/qwen-7b-chat
```

5. Chat with Models

```
basket chat "What is the meaning of life?"
```

6. Switch to other MaaS or models

```
basket maas use deepseek

basket model use deepseek-chat
```

## Contribution

Please help us to integrate with more MaaS.

- [x] FreeModel
- [x] OpenAI
- [x] SiliconFlow
- [x] DashScope
- [x] OpenRouter
- [x] DeepSeek
- [x] MoonShot
- [x] ZhiPu
