from icecream import ic
from mylib.pedal import Pedal
from mylib.pedal_function import  PedalFunction
from pathlib import Path
import json
import jsonpickle # pip install jsonpickle
from pathlib import Path


my_pedal_ids = [
    'tc-electronic-polytune-3', # Polytune 3
    'electro-harmonix-super-pulsar', # Super Pulsar
    'electro-harmonix-tone-corset', # Tone Corset
    'ibanez-tube-screamer-mini', # Tube Screamer Mini
    'keeley-loomer', # Loomer
    'boss-oc-5', # Boss OC-5
    'mooer-ninety-phaser', # Mooer Ninety Phaser
    'eventide-eventide-h9-max-dark', # Eventide H9 Max Dark
    'chase-bliss-audio-brothers', # Brothers
    'chase-bliss-audio-condor', # Condor 
    'chase-bliss-audio-mood', # Mood
    'chase-bliss-audio-blooper', # Blooper
    'old-blood-noise-excess', # Old Blood Noise - Excess
    'boss-rc-500', # Boss RC-500 Looper
    'boss-dd-200-digital-delay', # Boss DD-200 Delay
    'morningstar-mc6-mkii', # Morning Star MC 6
    'empress-effects-zoia', # Zoia 
    'disaster-area-midi-box-4', # MIDI Box 4
    'digitech-whammy-5', # Whammy 5
    'digitech-trio+-band-creator', # Trio+
]

functions = []

with open('functions.json', 'r', encoding='utf-8') as f:
    functions = jsonpickle.loads(f.read(), classes=PedalFunction)
    functions = sorted(functions, key=lambda f: f.weight)

with open('all_pedals.json', 'r', encoding='utf-8') as p:
    all_pedals = jsonpickle.loads(p.read(), classes=Pedal)
    my_pedals = [i for i in all_pedals if i.hrid in my_pedal_ids]
    for p in my_pedals:
        p.function = sorted([i for i in functions if i.function in p.function], key=lambda f: f.weight)

    my_pedals = sorted(my_pedals, key=lambda p: p.function[0].weight)   

    for p in my_pedals:  
        ic(f'{p.manufacturer} {p.name} - {p.function[0].weight}')

