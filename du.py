from globusonline.transfer.api_client import TransferAPIClient
from util import *

global api

def du(endpoint, path="/", file='*.*'):
    global api
    size = 0

    listing = api.endpoint_ls(endpoint, path)
    for item in listing[2]:
        print item.name


def main():
    global api

    options = process_args()
    token = get_token(options.username)
    api = TransferAPIClient(username=options.username, goauth=token)
    du(options.endpoint)

if __name__ == "__main__":
    main()


