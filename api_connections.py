# Use this module to send email output
import smtplib
# Use this module to connect to twitter api
import tweepy

# Auth twitter
consumer_key = "TWITTER_CONSUMER_KEY"
consumer_secret = "TWITTER_CONSUMER_SECRET"
access_token = "TWITTER_ACCESS_TOKEN"
access_token_secret = "TWITTER_ACCESS_TOKEN_SECRET"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Connect to remote email server - using gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("USERNAME", "PASSWORD")