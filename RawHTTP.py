import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawReply = connection.getresponse().read()
    reply = json.loads(rawReply.decode('utf-8'))
    for key in sorted(reply['results'][0]['geometry']['location']):
        print(key, ' = ', reply['results'][0]['geometry']['location'][key])

if __name__ == '__main__':
    geocode('5th avenue, new york city')
