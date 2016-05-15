import json
import spotipy
import random
import spotipy.util as util

# open spotify credentials json
with open('credentials.json') as data_file:    
    credentials = json.load(data_file)

# refresh token
sp_token = spotipy.util.prompt_for_user_token(
                            username='vndrewlee', 
                            client_id=credentials['sp_client_id'], 
                            client_secret=credentials['sp_client_secret'],
			    redirect_uri='https://www.google.com')

# instantiate authorized spotify class
sp = spotipy.Spotify(auth=sp_token)

# get list of artists from rap caviar playlist
rap_caviar = sp.user_playlist(user = 'spotify', playlist_id='5yolys8XG4q7YfjYGl5Lff')
rap_caviar_list = rap_caviar['tracks']['items']
artist_list = [track['track']['artists'][0]['name'] for track in rap_caviar_list]

# make a dictionary of randomzied values to fill headline patterns
nums = [5,7,9,11]
fill_values = {
    'rapper1': random.choice(artist_list), 
    'rapper2': random.choice(artist_list), 
    'oddnumber': random.choice(nums)}

# headline patterns
thenext = 'Is %(rapper1)s the next %(rapper2)s?' % fill_values
oddways = '%(oddnumber)d reasons %(rapper1)s wouldn\'t be here without %(rapper2)s.' %fill_values
mixtape = '%(rapper1)s should make a mixtape with %(rapper2)s.' % fill_values
everything = '%(rapper1)s is everything rn.' % fill_values
still = 'What about %(rapper2)s tho?' % fill_values
demographics = 'Who are these people always listening to %(rapper1)s?' % fill_values

# list of hydrated patterns
possible_tweets = [thenext, oddways, mixtape, everything, still, demographics]

tweet = random.choice(possible_tweets)

import tweepy

auth = tweepy.OAuthHandler(consumer_key=credentials['tw_key'], consumer_secret=credentials['tw_secret'])

auth.set_access_token(
    key=credentials['tw_access_token'], 
    secret=credentials['tw_access_token_secret'])

tw = tweepy.API(auth)

print(tweet)

tw.update_status(status=tweet)
