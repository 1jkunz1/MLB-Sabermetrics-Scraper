import os

import praw


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

    for k, v in threads.items():
        if sport not in k:
            del threads[k]

    return threads


class RedditScraper(object):

    def __init__(self):

        self.comments = []
        self.submission = None
        self.mlb_threads = None
        self.nfl_threads = None

        self.reddit = reddit

        self.subreddit = self.reddit.subreddit('sportsbook')
        self.new_subreddit = self.subreddit.new(limit=25)

    def get_daily_threads(self):

        # returns a dict with the top 25 most recent threads
        # we will run this once per day

        for submission in self.new_subreddit:
            self.submissions.append((submission.title, submission.id))

        self.threads = dict(self.submissions)

        for k, v in self.threads.items():
            if 'Daily' not in k:
                del self.threads[k]

        return self.threads

    @staticmethod
    def get_daily_comments(args):
        if 'NFL' in args:
            return get_daily_threads('NFL')
        elif 'MLB' in args:
            return get_daily_threads('MLB')
        elif 'NCAAF' in args:
            return get_daily_threads('NCAAF')
        elif 'NBA' in args:
            return get_daily_threads('NBA')

    def make_comment_list(self, **kwargs):

        # Returns a list of comments from the thread passed into the function

        self.submission = self.reddit.submission(kwargs['thread_id'])

        for comment in self.submission.comments.list():
            self.comments.append(comment.body)

        return self.comments
