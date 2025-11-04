import os
import requests
import json
import pandas as pd


if os.path.exists(os.curdir + 'data.json') :
    print('yes')
else:
    
        r = requests.get('https://raw.githubusercontent.com/lmfmaier/cities-json/refs/heads/master/cities500.json')
        cities = json.loads(r.content)

    
    
    