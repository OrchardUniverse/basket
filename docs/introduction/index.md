---
outline: deep
---

# Introduction

Basket is a common toolkit for all MaaS with OpenAI API.

## Install

```
pip install orchard-basket
```

## Usage

### Use MaaS

List all available MaaS

```
basket maas list
```

Choose the MaaS to use.

```
basket use FreeModel
```

Reset the API Key for MaaS.

```
basket maas reset OpenAI
```

### Use Models

List all available models

```
basket model list
```

Choose the model to use.

```
basket use gpt-3.5-turbo
```

Reset the model.

```
basket model reset
```

### Use Models

List all available models.

```
basket model list
```

Choose the model to use.

```
basket use gpt-3.5-turbo
```

### Chat with Models

Use the MaaS and model to chat.

```
basket chat "What is the meaning of life?"
```

Use interactive mode to chat with historical dialogue.

```
basket chat

User> "What is the meaning of life?"
```

### Manage configuration

List the current chosen MaaS and model.

```
basket config list
```
