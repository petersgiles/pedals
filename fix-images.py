from icecream import ic
from mylib.pedal import Pedal
from pathlib import Path
import json
import jsonpickle # pip install jsonpickle

from pathlib import Path

pathlist = Path('data').glob('**/*.json')
for path in pathlist:
    i = open(path).read()

    pedal = jsonpickle.decode(i)
    
    image = Path(f'images/{pedal.image}')
    imagetarget = Path(f'images/{pedal.hrid}.jpg')
    if image.exists():
        image.rename(imagetarget)

        pedal.image = str(imagetarget)
        ic(f'{image} {imagetarget}')
        serialized = jsonpickle.encode(pedal) # max_depth is optional

        with open(f'out/{pedal.hrid}.json', 'w', encoding='utf-8') as f:
            json.dump(json.loads(serialized), f, ensure_ascii=False, indent=4)