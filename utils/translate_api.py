import requests
from config_data.config import RAPID_API_KEY_TRANSLATE

url = "https://translate-plus.p.rapidapi.com/translate"

payload = {"text": "Seat yourself on an incline bench with a dumbbell in each hand. "
                   "You should pressed firmly against he back with your feet together. "
                   "Allow the dumbbells to hang straight down at your side, holding them with a neutral grip. "
                   "This will be your starting position. Initiate the movement by flexing at the elbow, "
                   "attempting to keep the upper arm stationary. Continue to the top of the movement and pause, "
                   "then slowly return to the start position.", "source": "en", "target": "ru"}

headers = {"content-type": "application/json",
           "X-RapidAPI-Key": RAPID_API_KEY_TRANSLATE,
           "X-RapidAPI-Host": "translate-plus.p.rapidapi.com"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
