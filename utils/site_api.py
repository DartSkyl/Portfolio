from typing import List, Dict
import requests
from handlers.custom_handlers.output_of_the_result import start_output


def get_exercise(url: str, headers: Dict[str, str], querystring: Dict[str, str]) -> List[Dict[str, str]]:
    """
    Function sends a request to the API of the site
    :param url: Site URL
    :param headers: API headers
    :param querystring: Parameters selected by the user
    :return response.json(): Site response
    """
    response = requests.get(url=url, headers=headers, params=querystring)
    return response.json()


def main_api_func(url: str, headers: Dict[str, str], querystring: Dict[str, str], bot, from_user_id: int) -> None:
    """
    Function processes the received response and stores it in the user`s state
    :param url: Site URL
    :param headers: API headers
    :param querystring: Parameters selected by the user
    :param bot: TeleBot
    :param from_user_id: User ID
    """
    ready_list: List[str] = list()  # Site`s response will be processed here
    # We will convert each element of the response into a string convenient for output to the user
    for elem in get_exercise(url, headers, querystring):
        ready_string: str = elem['name'] + '\n' + 'Equipment: ' + elem['equipment'] + '\n' + elem['instructions']
        ready_list.append(ready_string)  # Forming a list with ready-made strings
    with bot.retrieve_data(user_id=from_user_id) as data:
        data['exercise'] = ready_list  # We save it separately for each user
    bot.send_message(from_user_id, text='Your exercises:')
    start_output(from_user_id=from_user_id)  # Launching the exercise display
