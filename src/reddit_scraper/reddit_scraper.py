import os

import praw
import pandas as pd
import datetime as dt


'''
Each subreddit has five different ways of organizing the topics created by redditors: 
.hot, .new, .controversial, .top, and .gilded. 
You can also use .search("SEARCH_KEYWORDS") to get only results matching an engine search.
'''


reddit = praw.Reddit(client_id=os.environ["client_id"],
                     client_secret=os.environ["client_secret"],
                     user_agent=os.environ["user_agent"],
                     username=os.environ["username"],
                     password=os.environ["password"])


subreddit = reddit.subreddit('sportsbook')


top_subreddit = subreddit.top(limit=5)

for submission in subreddit.top(limit=5):
    print(submission.title, submission.id)

topics_dict = {"title":[],"score":[],"id":[],"url":[],"comms_num":[],"created": [],"body": []}


for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)


print topics_dict

topics_data = pd.DataFrame(topics_dict)

print topics_data


def get_date(created):
    return dt.datetime.fromtimestamp(created)


_timestamp = topics_data["created"].apply(get_date)


topics_data = topics_data.assign(timestamp=_timestamp)