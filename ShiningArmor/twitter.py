import json
import tweepy


def tokens(tokens_file):
    # Get Twitter twitter_tokens
    try:
        f = open(tokens_file, mode='r')
        twitter_tokens = json.load(f)
        f.close()
    except FileNotFoundError as err:
        raise err
    except IOError as err:
        raise err

    return twitter_tokens


def auth(t_tokens):
    # tokens can be found under "Apps > RainBowDashBOT"
    try:
        t_auth = tweepy.OAuthHandler(t_tokens['consumer_api_key'],
                                     t_tokens['consumer_api_key_secret'])

        t_auth.set_access_token(t_tokens['access_token'],
                                t_tokens['access_token_secret'])

        api = tweepy.API(t_auth)

    except Exception as err:
        raise err

    return api


def tweet(api, tweet):
    # post the tweet on twitter
    status = 0

    try:
        if isinstance(tweet, str):
            orig_tweet = api.update_status(status=tweet)
        else:
            # multi-line message - create twitter thread
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
