import re
import time

import praw

import RedditOAuth  # Local

reddit = praw.Reddit(client_id=RedditOAuth.CLIENT_ID,
                     client_secret=RedditOAuth.CLIENT_SECRET,
                     password=RedditOAuth.PASSWORD,
                     user_agent=RedditOAuth.USER_AGENT,
                     username=RedditOAuth.USERNAME)


def get_info(message, username, reply, max_time=60*60):
    reply = re.compile(reply)

    while True:
        print("Asking /u/{un}: \"{m}\".".format(un=username, m=message))
        try:
            reddit.redditor(username).message("Reddit-Risk!", message)
            break
        except Exception as e:
            print(e)
            time.sleep(2)
    
    start_time = time.time()
    while True:
        time_elapsed = time.time() - start_time
        if time_elapsed <= max_time:
            print("Checking for messages from /u/{un}.".format(un=username))
            try:
                time.sleep(2)
                for pm in reddit.inbox.unread():
                    reddit.inbox.mark_read([pm])
                    if pm.author == username:
                        print("{un} replied with \"{b}\".".format(un=username, b=pm.body))
                        return reply.match(pm.body)
            except Exception as e:
                print(e)

            time.sleep(2)
        else:
            print("Timed out.")
            return None
