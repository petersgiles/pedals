from icecream import ic
from mylib.pedal import Pedal
from pathlib import Path
import json
import jsonpickle # pip install jsonpickle
from pathlib import Path

my_pedal_ids = [
    'tc-electronic-polytune-3', # Polytune 3
    'chase-bliss-audio-brothers', # Brothers
    'chase-bliss-audio-condor', # Condor 
    'chase-bliss-audio-mood', # Mood
    'chase-bliss-audio-blooper', # Blooper
    'old-blood-noise-excess', # Old Blood Noise - Excess
    'boss-rc-500', # Boss RC-500
    'morningstar-mc6-mkii', # Morning Star MC 6
    'empress-effects-zoia', # Zoia 
    'disaster-area-midi-box-4', # MIDI Box 4
    'digitech-whammy-5', # Whammy 5
]

with open('all_pedals.json', 'r') as p:
    all_pedals = jsonpickle.loads(p.read(), classes=Pedal)
    my_pedals = [i for i in all_pedals if i.hrid in my_pedal_ids]
    my_sorted_pedals = sorted(my_pedals, key=lambda f: f.weight)

    for p in my_sorted_pedals:
        ic(f'{p.manufacturer} {p.name}')

