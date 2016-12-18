from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '2, Mégrine Riadh, Ben arous, Tunisia'
    print(Geocoder.geocode(address)[0].coordinates)
