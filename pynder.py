#Tinder API
import pynder

#technical Tinder stuff
import itertools 

#have fun changing our location
from geopy.geocoders import Nominatim
import requests
from random import *
import random

#so we can see pictures
from PIL import Image
import requests
from io import BytesIO



FACEBOOK_ID = ""
FACEBOOK_TOKEN = ""

while True:

    data = requests.get('https://raw.githubusercontent.com/David-Haim/CountriesToCitiesJSON/master/countriesToCities.json').json()
    quit = input("Quit? (type in 'quit')\n")
    #number = int(input("Number of inputs??\n")) for now were choosing a default for inputs
    if quit == "quit":
        break
    random.seed()
    country = random.choice(list(data.keys()))
    length = float(len(data[country]))
    rand_number = randint(0, length)
    city = data[country][rand_number]

    address = (("%s , %s") % (country, city))
    print(address)

    geolocator = Nominatim()
    location = geolocator.geocode(address)

    session = pynder.Session(facebook_id=FACEBOOK_ID, facebook_token=FACEBOOK_TOKEN)
    session.update_location(location.latitude, location.longitude)

    users = session.nearby_users()

    likes = 0
    dislikes = 0

    for nombres in range(1,10):
        usuarios = next(itertools.islice(users, nombres))
        #usuarios = itertools.islice(users, nombres)[1]
        photos = usuarios.photos
        first = photos[0]
        response = requests.get(first)
        image = Image.open(BytesIO(response.content))
        image.show()
        answers = input("yes or no?\n")
        if answers == "yes":
            likes += 1
        elif answers == "no":
            dislikes += 1


    print("People from %s are liked in %s percent" % (country, '{:.1%}'.format(likes/(likes+dislikes))))


 

