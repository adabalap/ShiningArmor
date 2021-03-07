import json
import tweepy




def tokens(tokens_file):
    # Get Twitter tokens

    try:
        f =  open(tokens_file, mode='r')
        tokens = json.load(f)

    except FileNotFoundError as err:
        raise err

    except IOError as err:
        raise err

    finally:
        f.close()

    return tokens





def auth(tokens):
    # post the tweet on twitter
    # tokens can be found under "Apps > RainBowDashBOT"
    try:
        auth = tweepy.OAuthHandler(tokens['consumer_api_key'], \
                tokens['consumer_api_key_secret'])

        auth.set_access_token(tokens['access_token'], \
                tokens['access_token_secret'])

        api = tweepy.API(auth)

    except Error as err:
        raise err

    return api



def tweet(api, tweet):
    # post the tweet on twitter

    status = 0

    try:
        api.update_status(tweet)

    except tweepy.error.TweepError as err:
        raise err
        status = 1

    return status 
