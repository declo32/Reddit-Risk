"""
I don't know how to do this yet
"""

import praw

import RedditOAuth  # Local

reddit = praw.Reddit(client_id=RedditOAuth.CLIENT_ID,
                     client_secret=RedditOAuth.CLIENT_SECRET,
                     password=RedditOAuth.PASSWORD,
                     user_agent=RedditOAuth.USER_AGENT,
                     username=RedditOAuth.USERNAME)
