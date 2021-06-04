import tensorflow as tf
import json
import numpy as np
import re
import pickle

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

MODEL = load_model('../models/nlp.h5')
TOKENIZER = pickle.load(open('../models/tokenizer.pickle','rb'))
with open('../models/response.json') as response_data:
  responses = json.load(response_data)

def predictionProc(text):
  max_length = 30
  trunc_type='post'
  padding_type='post'
  seq = TOKENIZER.texts_to_sequences([text])
  pad = pad_sequences(seq, maxlen=max_length, padding=padding_type, truncating=trunc_type)
  pred = int(np.argmax(MODEL.predict(pad, verbose=0)))
  response = ""
  for key in responses:
    if key == f'{pred}':
      response = responses[key]
  return response

