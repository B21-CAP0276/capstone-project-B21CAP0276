import tensorflow as tf
import json
import numpy as np
import re

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model

MODEL = load_model('../models/nlp.h5')

with open('../dataset/dataset.json') as json_data:
  intents = json.load(json_data)

def string_preprocessing(text):
  text = re.sub(r'[^\w\s]', '', text)
  return text.lower()

def tokenizers():
  inputs, targets = [], []
  labels = []
  response_for_every_label = {}

  for intent in intents['intents']:
    if intent['intent'] not in labels:
      labels.append(intent['intent'])
    if intent['intent'] not in response_for_every_label:
      response_for_every_label[intent['intent']] = []
        
    for text in intent['utterances']:
      inputs.append(string_preprocessing(text))
      targets.append(intent['intent'])
        
    for response in intent['answers']:
      response_for_every_label[intent['intent']].append(response)
  
  vocab_size = 100
  oov_tok = "<OOV>"

  tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
  tokenizer.fit_on_texts(inputs)

  return tokenizer

def predictionProc(text):
  max_length = 30
  trunc_type='post'
  padding_type='post'
  seq =  tokenizers().texts_to_sequences([text])
  pad = pad_sequences(seq, maxlen=max_length, padding=padding_type, truncating=trunc_type)
  return int(np.argmax(MODEL.predict(pad, verbose=0)))

