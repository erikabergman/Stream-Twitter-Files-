import twitter
#import python-twitter
import os
import json

consumer_key = os.environ["TwitterAPIKey"]
consumer_secret = os.environ["TwitterAPISecretKey"]
access_token = os.environ["TwitterAccessToken"]
access_token_secret = os.environ["TwitterAccessTokenSecret"]


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)




def main(LANGUAGES, FILTER, filename, path='./'):
    count = 0
    limit = 100
    with open(path + filename + '.txt', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES):
            if count < limit:
                f.write(json.dumps(line))
                f.write('\n')
                count += 1
                # print(line)
                print('\n')
                # print(count)
            else:
                return

main(['en'], [':('], 'frowny')
main(['en'], [':)'], 'smiley')
# main(['en'], ['#datascience'], 'output')


