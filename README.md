# visualizing-tweets

This is an app that maps sentiment of tweets across the world visually. It collects tweets in real-time based on the number of seconds you wish to collect it for. (The Twitter API does not allow you to get tweets over a certain period of time due to privacy issues most likely). It only collects tweets that have coordinates associated with it, which is about 1-2% of tweets since users typically don't like to reveal their location. Then it is able to associate each of the tweets with a sentiment that ranges from -1.0 to 1.0 (very negative to very positive) using the Google Cloud Natural Language API. A user can upload the tweets they want to visualize using the steps below.

There are about 500 tweets mapped in the sample data set uploaded here which was collected for 5 minutes on 4/28/2018. 

The way that the sentiment is mapped related to market color is red if on a scale between -1 and -0.5, a light orange between -0.5 and 0, a light yellow/white between 0 and 0.5, and then green between 0.5 and 1. 

# Perform the final steps in Terminal:

0) Include your Twitter credentials via https://apps.twitter.com/ by making a new project, and type in 	```export GOOGLE_APPLICATION_CREDENTIALS="language_key.json" ``` in your folder so that you can activate the Google NLP API. 
1) ```python mine_tweets.py > mined_tweets.json ```
   
   You can change the # of seconds you wish to collect tweets for by changing the variable "runtime" in mine_tweets.py.
2) ```python parse_twitter.py > final_tweets.json```
	
	Be sure to open final tweets and then delete the last empty line in the file (otherwise there will be an error).
3) Open the map.html file and then upload the final_tweets.json file at the top of the page
4) Enjoy the visualization! Ta-da :D
