import tweepy
import time
import jsonpickle




# connect to twitter API
auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
 
api = tweepy.API(auth)

runtime = 10
class MyStreamListener(tweepy.StreamListener):
    #overload
    def on_status(self, status):
        try:
            with open('testFile.json', 'a') as f:
                if (status.coordinates is not None):
                    print(jsonpickle.encode(status._json, unpicklable=False))
                    #print(status)
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
# secretly gets all locations 
# twitter_stream.filter(locations=[-180,-90,180,90], languages=["en"], async=True)
twitter_stream.filter(locations=[-180,-90,180,90], async=True)
# collect data for this many seconds
time.sleep(runtime)
twitter_stream.disconnect() 



