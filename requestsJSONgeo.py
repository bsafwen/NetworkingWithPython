import requests

def geocode(address):
    parameters = { 'address': address, 'sensor' : 'false '}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    for key in sorted(answer['results'][0]['geometry']['location']):
        print(key, ' = ' , answer['results'][0]['geometry']['location'][key])

if __name__ == '__main__':
    geocode('2, Rue omar ben abdelaziz, Ben arous, Tunisia')
