import requests

endpoint = 'http://127.0.0.1:8000/album/1'
endpoint_add= 'http://127.0.0.1:8000/cancion/create'
endpoint_update= 'http://127.0.0.1:8000/album/update/4'
endpoint_destroy= 'http://127.0.0.1:8000/album/destroy/4'

endpoint_new= 'http://127.0.0.1:8000/cancion'

response = requests.get (endpoint_new)

print(response.json())
