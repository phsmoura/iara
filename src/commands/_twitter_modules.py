import time
import tweepy
# from textblob import TextBlob
# import preprocessor
from requests_oauthlib import OAuth1Session

from src.commands._secrets import TWITTER_API_KEY, TWITTER_API_SECRET


consumer_key = TWITTER_API_KEY
consumer_secret = TWITTER_API_SECRET

def get_session():
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    print("Please go here and authorize: %s" % authorization_url)
    verifier = input("Paste the PIN here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]
    
    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    return oauth

def check_tweet_url(post,interactions) -> bool:
    print("Checking image in tweet url...")
    return True

def get_posts_url(username,number_tweets) -> list:
    print("Getting tweet posts urls...")
    return []

def get_accounts_interacted(interactions) -> list:
    print("Getting accounts interacted with the post...")
    return []

def write_database(username,tweet,accounts):
    print("Writing all info in database...")

def write_report(username,tweet,out):
    print("Writing report...")