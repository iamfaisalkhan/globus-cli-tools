import re

from globusonline.transfer.api_client import TransferAPIClient
from util import *

global api

def du(endpoint, pattern=None, path="/"):
    global api

    size = 0

    listing = api.endpoint_ls(endpoint, path)
    for item in listing[2]['DATA']:
        
        if item['type'] == 'file':
            if pattern:
                if pattern.match(item['name']):
                    size += long(item['size'])
            else:
                size += long(item['size'])
        elif item['type'] == 'dir':
            size += du(endpoint,  path="%s/%s"%(path, item['name']), pattern=pattern)

    return size

def main():
    global api

    options = process_args()
    token = get_token(options.username)
    api = TransferAPIClient(username=options.username, goauth=token)

    prog = None
    if options.filter != None:
        try:
            prog = re.compile(options.filter)
        except Exception, e:
            prog = None
        
    print sizeof_fmt(du(options.endpoint, path=options.path, pattern=prog))

if __name__ == "__main__":
    main()


