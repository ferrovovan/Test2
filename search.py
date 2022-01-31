import sys
from io import BytesIO

import requests
from PIL import Image
from super_function import true_params

toponym_to_find = ' '.join(sys.argv[1:])

map_api_server = "http://static-maps.yandex.ru/1.x/"
params = true_params(toponym_to_find)
params['pt'] = params['ll'] + ',pmwtm1'
response = requests.get(map_api_server, params=params)

Image.open(BytesIO(
    response.content)).show()
