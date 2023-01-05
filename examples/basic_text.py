from scriptgui.decorator import sgui

@sgui('/basic_text', {'type': 'Text'})
def basic_text():
    return 'Hello, World!'