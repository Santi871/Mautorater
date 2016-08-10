import os
from flask import Flask, request
import reddit_interface.utils as utils
from reddit_interface.bot import RedditBot

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'
SLACK_SLASHCMDS_SECRET = utils.get_token("SLACK_SLASHCMDS_SECRET")

app = Flask(__name__)
bot = RedditBot()


@app.route('/slack/tifu/commands', methods=['POST'])
def command():
    if request.form.get('token') == SLACK_SLASHCMDS_SECRET and request.form.get('command') == '/lock':

        text = request.form.get('text')
        args = text.split(" ", 1)
        url = args[0]
        reason = args[1]
        response_url = request.form.get('response_url')

        bot.post_message_and_lock(submission_url=url, lock_message=reason, response_url=response_url)

        return "Processing your request... please allow a few seconds."

    else:
        return "Invalid request token."
