import os
import json
import requests
from states.paremetrs_of_choice import request_dict
from config_data.config import RAPID_API_KEY


api_key = RAPID_API_KEY


def get_exercise():
    global api_key
    url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"
    querystring = request_dict['muscle']
    print(request_dict)
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


def edit_func():
    ready_string = ''
    ready_list = []
    for elem in get_exercise():
        ready_string = elem['name'] + '\n' + 'Equipment: ' + elem['equipment'] + '\n' + elem['instructions']
        ready_list.append(ready_string)
    with open('ready_answer.json', 'w') as file:
        json.dump(ready_list, file, indent=4)


if __name__ == '__main__':
    edit_func()
    with open('..\\states\\ready_answer.json', 'r') as file:
        text = json.load(file)
    print(type(text))
