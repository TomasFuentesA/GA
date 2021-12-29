import tweepy
import json
from datetime import datetime as dt
from datetime import timedelta as td
import pandas as pd
import csv

months = {
    'Jun': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}

#Credenciales
#Por efectos de privacidad, las credenciales de tweepy no se agregaron
API_KEY = ''
API_KEY_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

#Autenticación
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#verificar si el archivo existe
aux = []
try:
    csvfile = open('datasetMP.csv','r', newline='')

    lineas = csvfile.readlines()
    for line in lineas:
        line = line.split(',')
        aux.append(line[0])
    csvfile.close()
except:
    None

#Generación del objeto API
api = tweepy.API(auth, wait_on_rate_limit = True)
places = api.search_geo(query="CHILE", granularity="country")
place_id = places[0].id
tweets = api.search_tweets(q="place:%s" % place_id)
output = []
csvfile = open('datasetMP.csv','a+', newline='')
field_names= ['user_id', 'user_name', 'screen_name', 'followers_count', 'description', 'verified', 'profile_image_default', 'protected', 'favourites_count','user_registration']
writer = csv.DictWriter(csvfile, fieldnames=field_names)
writer.writeheader()

for tweet in tweepy.Cursor(api.search_tweets, q="place:%s" % place_id, tweet_mode="extended").items():

    if(str(tweet.user.id) not in aux):
        try: 

            user_id = tweet.user.id
            aux.append(str(user_id))
            user = api.get_user(user_id = user_id)
            name = user._json['name'].encode("utf-8")
            screen_name = user._json['screen_name']
            follower_count = user._json['followers_count']
            favourite_count = user._json['favourites_count']
            created_at = user._json['created_at']
            created_at = created_at[8:10]+'-'+months[created_at[4:7]]+'-'+created_at[26:31]
            if(user._json['description'] != ''):
                description = 1
            else:
                description = 0
                
            if(user._json['verified'] == 'true'):
                verified = 1
            else:
                verified = 0
                
            if(user._json['default_profile_image'] == 'true'):
                profile_image = 1
            else:
                profile_image = 0
            
            if(user._json['protected'] == 'true'):
                protected = 1
            else:
                protected = 0

            line = {'user_id': user_id, 
                    'user_name': name,
                    'screen_name': screen_name, 
                    'followers_count':follower_count, 
                    'description':description, 
                    'verified': verified, 
                    'profile_image_default': profile_image, 
                    'protected': protected, 
                    'favourites_count': favourite_count,
                    'user_registration': created_at
            }
            print(line, 'Largo = ',len(aux))
            writer.writerow(line)

        except:
            None

csvfile.close()
