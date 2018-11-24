import os

import praw


class RedditScraper(object):

    def __init__(self):

        self.comments = []
        self.submissions = []
        self.threads = {}
        self.submission = None

        self.reddit = praw.Reddit(client_id='LsEMlrflEe17VA',
                                  client_secret='U5DIf2X4jFldQpsig2-w-S0nbNE',
                                  user_agent='sabermetric-scraper',
                                  username= os.getenv("USERNAME"),
                                  password=os.getenv("PASS"))

        self.subreddit = self.reddit.subreddit('sportsbook')
        self.new_subreddit = self.subreddit.new(limit=25)

    def get_threads(self):

        # returns a dict with the top 25 most recent threads
        # we will run this once per day

        for submission in self.new_subreddit:
            self.submissions.append((submission.title, submission.id))

        self.threads = dict(self.submissions)

        return self.threads

    def make_comment_list(self, *kwargs):

        # Returns a list of comments from the thread passed into the function

        self.submission = self.reddit.submission(id='9zlrrx')

        for comment in self.submission.comments.list():
            self.comments.append(comment.body)

        return self.comments
