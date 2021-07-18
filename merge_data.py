from icecream import ic
from mylib.pedal import Pedal
from pathlib import Path
import json
import jsonpickle # pip install jsonpickle

from pathlib import Path

pathlist = Path('data').glob('**/*.json')

result = []
for path in pathlist:
    with open(path, 'r') as f:
        pedal = jsonpickle.loads(f.read())

        result.append(pedal)

serialized = jsonpickle.encode(result) # max_depth is optional

with open(f'merged_file.json', 'w', encoding='utf-8') as fout:
    json.dump(json.loads(serialized), fout, ensure_ascii=False, indent=4)