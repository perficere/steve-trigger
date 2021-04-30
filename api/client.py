from .utils import api_request

trigger = lambda: api_request(method="POST", path="/trigger")
