import tweepy
import time
import jsonpickle

# twitter authentication keys 
APP_KEY = ""
APP_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

# connect to twitter API
auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

# how many seconds you want to collect tweets for (this is 5 min)
runtime = 300
class MyStreamListener(tweepy.StreamListener):
    #overload
    def on_status(self, status):
        try:
            if (status.coordinates is not None):
                # convert to json object for parsing
                print(jsonpickle.encode(status._json, unpicklable=False))
            return True
     
        except BaseException as e:
            print("Error on_status: %s" % str(e))
            
        return True
 
    def on_error(self, status):
        print(status)
        return True

    def on_timeout(self):
        return True 

twitter_stream = tweepy.Stream(auth, MyStreamListener())
# change languages below if interested
# twitter_stream.filter(locations=[-180,-90,180,90], languages=["en"], async=True)
twitter_stream.filter(locations=[-180,-90,180,90], async=True)
# collect data for this many seconds
time.sleep(runtime)
# disconnect after runtime seconds
twitter_stream.disconnect() 



