from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from konlpy.tag import Okt
import pickle
import re


def sentiment_predict(new_sentence):
  stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
  max_len = 30 # 리뷰 길이
  okt = Okt()
  with open('./reviews/sentiment/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
  loaded_model = load_model('./reviews/sentiment/best_model.h5')

  new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
  new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
  new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거

  encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
  pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
  score = float(loaded_model.predict(pad_new)) # 예측
  return round(score * 100)
  
  