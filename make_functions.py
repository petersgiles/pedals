from icecream import ic
from mylib.pedal_function import PedalFunction
from pathlib import Path
import json
import jsonpickle  # pip install jsonpickle

from pathlib import Path

mnemonic = [
    'Tuner',
    'Wah', 'Fuzz', 'Phase Shifter', 'Phaser',
    'Compression','Compressor',
    'Overdrive','Distortion', 'Gain', 'Crunch',
    'Equalizer',
    'Pitch', 'Vibrato', 'Pitch Shifter',
    'Modulation', 'Ring Modulator', 'Chorus', 'Flanger', 'Filter'
    'Level', 'Volume', 'Tremolo', 'Noise Gate', 'Limiter', 
    'Echo', 'Delay', 'Sampling', 'Looper', 'Digital Glitch', 'Drum',
    'Reverb',
    'Utility', 'Expression', 'Controller', 'Switch', 'MIDI',  'Power', 'Unlisted'
]

# 'Bass',
# 'Digital',
# 'Dual/Stereo',
# 'Dynamics',
# 'Modeling/Simulation',
# 'Multieffect',
# 'PreAmp',
# 'Rotary',
# 'Synth Voice',
# 'Tube',


path = 'all_pedals.json'
with open(path, 'r') as f:
    pedals = jsonpickle.loads(f.read())

    functions = (p.function for p in pedals)
    results_union = set().union(*functions)

    pfs = []
    for funct in results_union:
        try:
            index = mnemonic.index(funct)
        except ValueError:
            index = 99
        pfs.append(PedalFunction(funct, index))

    serialized = jsonpickle.encode(pfs, max_depth=2)  # max_depth is optional
    # ic( json.dumps(json.loads(serialized), indent=4))
    with open(f'functions.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(serialized), f, ensure_ascii=False, indent=4)
