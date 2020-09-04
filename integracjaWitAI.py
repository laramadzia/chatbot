from wit import Wit

access_token = "CB6Y5SR6R5R6VXUDZQN3G7SCWJ4HK2L5"

client = Wit(access_token=access_token)


def wit_response(message):
    resp = client.message(message)

    try:
        return list(resp['entities'])[0]
    except:
        return 'Nie rozumiem. Zadaj pytanie inaczej.'
        pass
