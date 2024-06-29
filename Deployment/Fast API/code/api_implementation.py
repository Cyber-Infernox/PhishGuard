# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:21:09 2024

@author: sayon
"""

import json
import requests

urly = "http://127.0.0.1:8000/url_prediction"; # Private URL
#urly = "https://39e7-34-106-17-90.ngrok-free.app/url_prediction"; # Public URL

input_data_for_model = {
    #'url' : "https://review-related.com/update"
    #'url' : "https://www.chess.com/"
    #'url' : "http://www.mnnit.ac.in/"
    #'url' : "https://www.instagram.com/"
    'url' : "https://www.linkedin.com/feed/"
    #'url' : "https://www.tcs.com/"
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(urly, data=input_json)

print(response.text)