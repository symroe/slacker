#!/usr/bin/env python
"""Post slack message."""

# https://github.com/senpay/slacker
# fork of https://github.com/os/slacker
# https://api.slack.com/methods

import os
from slacker2 import Slacker


def post_slack():
    """Post slack message."""
    try:
        token = os.environ['SLACK_TOKEN']
        slack = Slacker(token)

        obj = slack.chat.post_message('#general', 'Hello fellow slackers!')
        print(obj.successful, obj.__dict__['body']['channel'], obj.__dict__[
            'body']['ts'])
    except KeyError as ex:
        print('Environment variable %s not set.' % str(ex))


if __name__ == '__main__':
    post_slack()
