import requests
import six

import meetup.api
client = meetup.api.Client('6039502f4e5599726f23f5a6a3318')
client.api_key = "6039502f4e5599726f23f5a6a3318"
print client.GetGroup