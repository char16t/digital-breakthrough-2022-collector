import math
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
from solution.load_data import \
    df_issues_train, \
    df_comment_train, \
    df_emp, \
    df_issues_test, \
    df_comment_test, \
    merged


def build_d2v_comments_model():
  tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(df_comment_train["text"])]
  max_epochs = 100
  vec_size = 20
  alpha = 0.025

  model = Doc2Vec(vector_size=vec_size,
                  alpha=alpha, 
                  min_alpha=0.00025,
                  min_count=1,
                  dm =0)
    
  model.build_vocab(tagged_data)

  for epoch in range(max_epochs):
      print('[comments model] iteration {0}'.format(epoch))
      model.train(tagged_data,
                  total_examples=model.corpus_count,
                  epochs=model.epochs)
      # decrease the learning rate
      model.alpha -= 0.0002
      # fix the learning rate, no decay
      model.min_alpha = model.alpha

  model.save("target/comments.d2v.model")
