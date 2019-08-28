from flask import Flask,request
from flask_restful import Api,Resource

import json
import numpy as np

app = Flask(__name__)
api = Api(app)

class Demo(Resource):
    
    def __init__(self):
        pass;
    
    def get(self):
        return "this is a get_method!";
    
    
    def post(self):
        data_json = request.json;
        data_dict = json.loads(data_json);
        
        signal = data_dict["signal"];
        
        ret = {};
        ret["return_signal"] = signal;
        
        return ret;

api.add_resource(Demo,"/");

if __name__=="__main__":
    app.run();