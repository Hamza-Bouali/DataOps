import sys
import os
from dotenv import load_dotenv
import json

load_dotenv()
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import App


OW_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
def serializer_function(v): # you can modify it later
    if v is None:
        return None
    try:
        return json.loads(v.decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"Warning: could not decode message value: {v!r}, error: {e}")
        return None



app = App(OW_API_KEY,'localhost:9092',serializer_function)