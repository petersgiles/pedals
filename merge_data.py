from icecream import ic
from mylib import pedal_function
from mylib.pedal import Pedal
from mylib.pedal_function import  PedalFunction
from pathlib import Path
import json
import jsonpickle # pip install jsonpickle
from pathlib import Path


pathlist = Path('data').glob('**/*.json')

result = []
for path in pathlist:
    with open(path, 'r', encoding='utf-8') as f:
        pedal: Pedal = jsonpickle.loads(f.read(), classes=Pedal)
        result.append(pedal)

serialized = jsonpickle.encode(result) # max_depth is optional

with open(f'all_pedals.json', 'w', encoding='utf-8') as fout:
    json.dump(json.loads(serialized), fout, ensure_ascii=False, indent=4)