# Use this module to interact with twitter api
import tweepy
# Use this module to pull down date
import time
# Use this module to make sleep time random each time
from random import randint
# Use this module to save results to files
import pickle
# Interdependencies
from api_connections import api

# List of twitter screen names to track
accounts = ["ACCOUNT_1","ACCOUNT_2","ACCOUNT_3","ACCOUNT_N"]

# Function to pull down new profiles
def get_new_profiles(account_list):
    # Set variables to track twitter api rate status
    rate_limit = 0
    # Set up string to hold email text output
    email_text = ""
    # For each account pull down new following and add to email
    for account in account_list:
        # Get account name
        account_name = api.get_user(account).name
        # Open or create previous following list
        file = ""
        file = account + ".p"
        try:
            friends = pickle.load(open(file,"rb"))
        except:
            friends = []
        # Check if any new following for each tracked account
        for friend in tweepy.Cursor(api.friends_ids, screen_name=account).items(50):
            # If new following, get details and add to email output
            if friend not in friends:
                friends.append(friend)
                new_friend = api.get_user(friend)
                new_friend_name = new_friend.screen_name
                new_friend_desc = new_friend.description
                email_text += """<p style="margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-family: Helvetica;font-size: 16px;line-height: 150%;text-align: left;">"""
                email_text += "-- <a href=\""
                email_text += "https://twitter.com/" + new_friend_name
                email_text += """" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #2BAADF;font-weight: normal;text-decoration: underline;">"""
                email_text += "@" + new_friend_name + "</a> was followed by " + account_name + ". "
                email_text += new_friend_desc + "</p>"
        # Save down new following list
        #pickle.dump(friends,open(file,"wb"))
        # Increment rate tracking
        rate_limit += 1
        # Put script to sleep if hit twitter api limit
        if rate_limit > 15:
            time.sleep(randint(950,1200)) # If hit rate limit go to sleep for about 15 minutes
    return email_text