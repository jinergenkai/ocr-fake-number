import json

json_str = ""
config = {}
hideMenuBar, onTop, height, width, delay, image_name = [None] * 6

try:
    with open('config.json', 'r') as f:
        json_str = f.read()
    config = json.loads(json_str)

    hideMenuBar = config['hideMenuBar']
    onTop = config['onTop']
    height = config['height']
    width = config['width']
    delay = config['delay']
    image_name = config['image_name']

except FileNotFoundError:

    hideMenuBar = config['hideMenuBar'] = False
    onTop = config['onTop'] = False
    height = config['height'] = 500
    width = config['width'] = 500
    delay = config['delay'] = 250
    image_name = config['image_name'] = "Notepad"

    json_str = json.dumps(config)

    with open('config.json', 'w') as f:
        f.write(json_str)

print(config)