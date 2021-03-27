import json
import tweepy


def tokens(tokens_file):
    # Get Twitter tokens
    try:
        f = open(tokens_file, mode='r')
        tokens = json.load(f)
        f.close()
    except FileNotFoundError as err:
        raise err
    except IOError as err:
        raise err

    return tokens


def auth(tokens):
    # tokens can be found under "Apps > RainBowDashBOT"
    try:
        auth = tweepy.OAuthHandler(tokens['consumer_api_key'],
                                   tokens['consumer_api_key_secret'])

        auth.set_access_token(tokens['access_token'],
                              tokens['access_token_secret'])

        api = tweepy.API(auth)

    except Exception as err:
        raise err

    return api


def tweet(api, tweet):
    # post the tweet on twitter
    status = 0

    try:
        if isinstance(tweet, str):
            tweet = tweet.split('\n')

        orig_tweet = api.update_status(status=tweet[0])

        for i in tweet[1:]:
            reply_tweet = api.update_status(status=i,
                                            in_reply_to_status_id=orig_tweet.id,
                                            auto_populate_reply_metadata=True)
            orig_tweet = reply_tweet

    except tweepy.error.TweepError as err:
        status = 1
        raise err

    return status
