import os

import praw
import pandas as pd
import datetime as dt


class RedditScraper(object):

    def __init__(self):

        self.reddit = praw.Reddit(client_id=os.environ["client_id"],
                                  client_secret=os.environ["client_secret"],
                                  user_agent=os.environ["user_agent"],
                                  username=os.environ["username"],
                                  password=os.environ["password"])



    def create_dict(self):
        for submission in top_subreddit:
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(submission.created)
            topics_dict["body"].append(submission.selftext)
            return topics_dict

    @staticmethod
    def get_date(created):
        return dt.datetime.fromtimestamp(created)


    _timestamp = topics_data["created"].apply(get_date)


    topics_data = topics_data.assign(timestamp=_timestamp)