from flask import Flask, request, jsonify

import tensorflow as tf
import json
import numpy as np
import logging
import os
from predictionModel import predictionProc

app = Flask(__name__)

@app.route('/', methods=['GET'])
def server_check():
  return "i'm alive"

@app.route('/predict', methods=['POST'])
def predictor():
  try:
    content = request.json
    requested_data = content['data']
    with open('../dataset/dataset.json') as json_data:
      intents = json.load(json_data)
      pred = predictionProc(requested_data)
  except:
    logging.exception("The JSON request or file is broken.")
    return jsonify(status='error', predict=-1, data=content['data'])

  return jsonify(status='ok', predict=pred, data=content['data'])

if __name__=='__main__':
  app.run( debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)) )