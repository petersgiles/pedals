from icecream import ic
from mylib.pedal_function import PedalFunction
from pathlib import Path
import json
import jsonpickle # pip install jsonpickle

from pathlib import Path

path = 'merged_file.json'
with open(path, 'r') as f:
    pedals = jsonpickle.loads(f.read())

    functions=(p.function for p in pedals)
    results_union = set().union(*functions)

    pfs = []
    for funct in results_union:
        pfs.append(PedalFunction(funct))

    serialized = jsonpickle.encode(pfs, max_depth=2) # max_depth is optional
    # ic( json.dumps(json.loads(serialized), indent=4))
    with open(f'functions.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(serialized), f, ensure_ascii=False, indent=4)
