import requests


def parseAttribute(key, rxcui_object_list):
    return [ obj[key] for obj in rxcui_object_list ]


def parseTTY(tty_list, concept_groups):
    selected_groups = []
    for group in concept_groups:
        if group['tty'] in tty_list and 'conceptProperties' in group:
            selected_groups += group['conceptProperties']
    return selected_groups


def getAllRelatedInfo(rxcui):
    url = f'https://rxnav.nlm.nih.gov/REST/rxcui/{rxcui}/allrelated.json'
    response = requests.get(url)
    return response.json()


def getAllConceptRxcui(tty_list, rxcui):
    allRelatedInfo = getAllRelatedInfo(rxcui)

    concept_groups = allRelatedInfo['allRelatedGroup']['conceptGroup']

    concept_objs = parseTTY(tty_list, concept_groups)

    return parseAttribute('rxcui', concept_objs)
