import os

import praw
import html


reddit = praw.Reddit(client_id='LsEMlrflEe17VA',
                     client_secret='U5DIf2X4jFldQpsig2-w-S0nbNE',
                     user_agent='sabermetric-scraper',
                     username=os.getenv("USERNAME"),
                     password=os.getenv("PASS"))


def get_daily_threads(sport):

    submissions = []

    subreddit = reddit.subreddit('sportsbook')
    new_subreddit = subreddit.new(limit=25)

    for submission in new_subreddit:
        submissions.append((submission.title, submission.id))

    threads = dict(submissions)

    for k in list(threads):
        if sport not in k:
            del threads[k]

    return threads


class RedditScraper(object):

    def __init__(self):

        self.comments = []
        self.submissions = []
        self.comment_queue = None
        self.submission = None
        self.mlb_threads = None
        self.nfl_threads = None

        self.reddit = reddit

        self.subreddit = self.reddit.subreddit('sportsbook')
        self.new_subreddit = self.subreddit.new(limit=25)

    def get_daily_comments(self, args):
        if 'NFL' in args:
            nfl = list(get_daily_threads('NFL').values())
            return nfl
        elif 'MLB' in args:
            mlb = list(get_daily_threads('MLB').values())
            return mlb
        elif 'NCAAF' in args:
            ncaaf = list(get_daily_threads('NCAAF').values())
            return ncaaf
        elif 'NBA' in args:
            nba = list(get_daily_threads('NBA').values())
            return nba

    def make_comment_list(self, **kwargs):

        # Returns a list of comments from the thread passed into the function

        self.submission = self.reddit.submission(kwargs['thread_id'])
        self.submission.comments.replace_more(limit=None)

        for comment in self.submission.comments.list():
            comment = comment.body
            comment.replace('#39;', '')
            self.comments.append(comment)

        return self.comments
