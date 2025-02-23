import json5
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from utils import jsonDumps
from utils import updateConfig

def before(src, dst):
    key_list = ['version', 'desp']
    for key in src:
        if key in dst:
            if key in key_list:
                src[key] = dst[key]


with open(sys.argv[1], 'r', encoding='utf-8') as f:
    config = json5.load(f)
with open(sys.argv[2], 'r', encoding='utf-8') as f:
    oldconfig = json5.load(f)

before(oldconfig, config)

data = updateConfig(oldconfig, config)

with open(sys.argv[3], 'w', encoding='utf-8') as f:
    f.write(jsonDumps(data))
