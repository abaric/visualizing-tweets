from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

APP_KEY = "yYOq3kBrVcQxIiu5TkJcStKhq"
APP_SECRET = "AysQXnWeZWcd1GiYcl15SqgdaPxID3c2K6FofgZdCEV3OsfRxI"
OAUTH_TOKEN = "2945138685-LxVCeHygdHqeSkH13kZlbnnU22fBNEldjfCLjei"
OAUTH_TOKEN_SECRET = "bAvDPo09GRHnflMRhTgiofnQBdaCks56QfYsYge9KKwio"

runtime = 5

class listener(StreamListener):
    def on_data(self, data):
        #print data to file
        with open('tweeeeets.txt','a') as tf:
        	if (data['place']['bounding_box']['coordinates'] is not None):
        		tf.write(data)
        return True

    def on_error(self, status):
        print status

# set up connection to twitter
auth = OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitterStream = Stream(auth, listener())
#secretly get all tweets (this covers all locations)
twitterStream.filter(locations=[-180,-90,180,90])