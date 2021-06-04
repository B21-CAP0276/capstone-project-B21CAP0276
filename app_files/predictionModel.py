import tensorflow as tf
import json
import numpy as np
import re
import pickle

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model

MODEL = load_model('../models/nlp.h5')
TOKENIZER = pickle.load(open('../models/tokenizer.pickle','rb'))
with open('../dataset/dataset.json') as json_data:
  intents = json.load(json_data)

def string_preprocessing(text):
  text = re.sub(r'[^\w\s]', '', text)
  return text.lower()

def predictionProc(text):
  max_length = 30
  trunc_type='post'
  padding_type='post'
  seq = TOKENIZER.texts_to_sequences([text])
  pad = pad_sequences(seq, maxlen=max_length, padding=padding_type, truncating=trunc_type)
  return int(np.argmax(MODEL.predict(pad, verbose=0)))

