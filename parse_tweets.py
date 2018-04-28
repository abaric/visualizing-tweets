import json

data = []
#with open('fetched_tweets.txt') as f:
with open('all_tweets.json') as f:
    for line in f:
    	l = json.loads(line)

    	try:
    		if l['place'] is not None: 
    			if l['place']['bounding_box'] is not None:
    				if l['place']['bounding_box']['coordinates'] is not None:
    					coordinates = l['place']['bounding_box']['coordinates'][0][0]
    					text = l['text'].replace('\n', ' ')
    					print("%s\t%s" %(text, coordinates))
    	except:
    		pass