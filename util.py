#!/bin/env python

import os

from globusonline.transfer.api_client.goauth import get_access_token

__all__ = ['get_token',
            'process_args']


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
        options.filter = args[3]
    else:
        options.filter = '*.*'
        
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

