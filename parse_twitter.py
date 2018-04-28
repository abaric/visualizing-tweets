import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

data = []
client = language.LanguageServiceClient()
#with open('fetched_tweets.txt') as f:
with open('mined_tweets.json') as f:
    for line in f:
        l = json.loads(line)

        try:
            if l['place'] is not None: 
                if l['place']['bounding_box'] is not None:
                    if l['place']['bounding_box']['coordinates'] is not None:
                        coordinates = l['place']['bounding_box']['coordinates'][0][0]
                        text = l['text'].replace('\n', ' ')
                        document = types.Document(
                                    content=text,
                                    type=enums.Document.Type.PLAIN_TEXT)
                        sentiment = client.analyze_sentiment(document=document).document_sentiment
                        #print(sentiment.score)
                        print("%s\t%s\t%6.1f" %(text, coordinates, sentiment.score))
        except:
            pass