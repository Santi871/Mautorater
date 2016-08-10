import praw
import OAuth2Util
from praw.handlers import MultiprocessHandler
import reddit_interface.utils as utils
from reddit_interface.bot_threading import own_thread
import requests


class RedditBot:
    """Class that implements a Reddit bot to perform moderator actions in a specific subreddit"""

    def __init__(self):
        handler = MultiprocessHandler
        self.r = praw.Reddit(user_agent="windows:Mautorater 0.1 by /u/santi871", handler=handler)
        self._authenticate()

    def _authenticate(self):
        o = OAuth2Util.OAuth2Util(self.r)
        o.refresh(force=True)
        self.r.config.api_request_delay = 1

    @own_thread
    def post_message_and_lock(self, kwargs):

        submission_url = kwargs['submission_url']
        lock_message = kwargs['lock_message']
        response_url = kwargs['response_url']

        submission = self.r.get_submission(url=submission_url)
        comment = submission.add_comment(lock_message)
        submission.lock()
        comment.distinguish(sticky=True)

        response = utils.SlackResponse()
        response.add_attachment(text="Submission locked successfully.", color='good', title=submission.title,
                                title_link=submission.permalink)

        requests.post(response_url, data=response.get_json(), headers={'Content-type': 'application/json'})

