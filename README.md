# ScriptGui

A simple plugin architecture GUI tool for scripts.

```python
from scriptgui.decorator import sgui

@sgui('/basic_text', {'type': 'Text'})
def basic_text():
    return 'Hello, World!'
```

![alt text](https://github.com/tylerhjones/scriptgui/blob/main/readme/basic_text_demo.png?raw=true)

## Quick Start

```
pip install scriptgui
```
```
scriptgui demo
```