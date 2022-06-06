import json


def load_candidates():
    """ Loads the full list of candidates """
    with open("candidates.json") as file:
        candidates_list = json.load(file)
    return candidates_list
