from api import client
from api.utils import as_handler


def main(event, context):
    return as_handler(func=client.trigger)()
