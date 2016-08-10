# Mautorater


## Dependencies

### Python 3 packages

* PRAW
* PRAW-OAuth2Util
* Flask


## Setup

The integration needs to be added to Slack as Slash commands custom integration
 and ran on an Internet-facing server so that Slack can reach it.


Additional files not included in this repository are:

* A tokens.ini file, containing just a `[tokens]` section and key-value
`SLACK_SLASHCMDS_SECRET = sekrit`, which will be given to you by Slack.
* An oauth.ini file for OAuth2 authentication, see
[PRAW-OAuth2Util](https://github.com/SmBe19/praw-OAuth2Util/blob/master/OAuth2Util/README.md)

Both files should go in the `main.py` folder.

## Usage

### Locking threads

Usage: `/lock [submission_url] [lock_message]`

Have in mind the lock message will be posted as-is to reddit. You can use the usual Markdown synthax and
newlines (by pressing shift+Enter). **Be careful, if you press Enter the command will be sent.**