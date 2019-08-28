import requests
import numpy as np
import json

signal = list(range(10));
input_dict = dict(signal=signal);
input_json = json.dumps(input_dict);

request_response = requests.post(url="http://127.0.0.1:5000/",json=input_json);

json_ret = request_response.json();
final_key = json_ret["return_signal"];

print("final_key:{}".format(final_key));