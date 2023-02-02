import requests
from urllib.parse import urlencode
import sys


def makeTiny(url):
    requestUrl = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    result = requests.get(requestUrl)
    return result.text
