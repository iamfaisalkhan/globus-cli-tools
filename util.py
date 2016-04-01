#!/bin/env python

import os

from globusonline.transfer.api_client.goauth import get_access_token

__all__ = ['get_token',
            'process_args',
            'sizeof_fmt']


def process_args(args=None):
    import sys

    if (args == None):
        args = sys.argv

    if len (args) < 3:
        print ' Usage %pprog username endpoint [reg-exp-filter]'
        sys.exit(1)

    options = type('lamdbaobject', (object,), {})()
    options.username = args[1]
    options.endpoint = args[2]

    if len(args) > 3:
        options.path = args[3]
    else:
        options.path = "/"

    if len(args) > 4:
        options.filter = args[4]
    else:
        options.filter = None
        
    return options

def get_token(username, token_file='globus-token.txt'):
    
    token = None
    
    if os.path.exists(token_file):
        with open(token_file, 'r') as f:
            token = f.read()

    if token == None:
        token = get_access_token(username)
        with open(token_file, 'w') as f:
            f.write(token.token)

    return token


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)