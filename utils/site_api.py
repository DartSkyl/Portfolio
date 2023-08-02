import requests
from handlers.custom_handlers.output_of_the_result import start_output


def get_exercise(url, headers, querystring):
    response = requests.get(url=url, headers=headers, params={'muscle': 'neck'})
    return response.json()


def main_api_func(url, headers, querystring, bot, from_user_id):
    ready_string = ''
    ready_list = []
    for elem in get_exercise(url, headers, querystring):
        ready_string = elem['name'] + '\n' + 'Equipment: ' + elem['equipment'] + '\n' + elem['instructions']
        ready_list.append(ready_string)
    with bot.retrieve_data(user_id=from_user_id) as data:
        data['exercise'] = ready_list
    bot.send_message(from_user_id, text='Your exercises:')
    start_output(from_user_id=from_user_id)
