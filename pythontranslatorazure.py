import requests, uuid, json

key = "AlEMjzpt6Ak7QECFfRTlGiEViGuUKV1Ay0HWpgPfTEX6bqiVeHoRJQQJ99AKACZoyfiXJ3w3AAAbACOGEdZ1"
endpoint = "https://api.cognitive.microsofttranslator.com"

location = "brazilsouth"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['fr', 'zu', 'pt-BR', 'es', 'ja', "it"]
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

body = [{
    'text': 'We are lights that spark in the chaos'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))