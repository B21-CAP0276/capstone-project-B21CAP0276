import tensorflow as tf
import json
import numpy as np
import re
import pickle

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

MODEL = load_model('../models/nlp.h5')
TOKENIZER = pickle.load(open('../models/tokenizer.pickle','rb'))
with open('../models/response.json') as response_data:
  responses = json.load(response_data)

def string_preprocessing(text):
  # Delete punctuation mark and lowing the text
  text = re.sub(r'[^\w\s]', '', text)
  text.lower()

  # create stemmer
  factory = StemmerFactory()
  stemmer = factory.create_stemmer()
  # stemming process
  text   = stemmer.stem(text)

  #Removing stopwords
  factory = StopWordRemoverFactory()
  stopword = factory.create_stop_word_remover()
  
  # Kalimat
  output = stopword.remove(text)

  return output

def predictionProc(text):
  max_length = 30
  trunc_type='post'
  padding_type='post'
  texts = string_preprocessing(text)
  seq = TOKENIZER.texts_to_sequences([texts])
  pad = pad_sequences(seq, maxlen=max_length, padding=padding_type, truncating=trunc_type)
  pred = int(np.argmax(MODEL.predict(pad, verbose=0)))
  response = ""
  for key in responses:
    if key == f'{pred}':
      response = responses[key]
  return response

