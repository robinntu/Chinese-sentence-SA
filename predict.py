# -*- coding: utf-8 -*-

from sent2charembedding import sent2charembed
from sent2wordembedding import sent2wordembed
from keras.models import Model
from keras.layers import Dropout, Activation, Bidirectional, Embedding,LSTM,Input, Dense,Wrapper, Recurrent, merge,GRU
from keras.callbacks import ModelCheckpoint
import numpy as np
from keras.objectives import categorical_crossentropy
from keras.metrics import categorical_accuracy as accuracy
from keras.regularizers import l2
import random
import codecs
import cPickle as pickle
from keras.models import load_model


def main(input_sent):
    model = load_model('my_model.h5')
    
    char_emb=sent2charembed(input_sent,'embedding_char.py','char_dic.py')
    word_emb=sent2wordembed(input_sent,'embedding_word.py','word_dic.py')

    predict=model.predict([word_emb,char_emb])

    if predict[0][0]>predict[0][1]:
        print 'Negative'
    elif predict[0][0]<predict[0][1]:
        print 'Positive'
    else:
        print 'Neutral'
    
main('这款手机的质量不错')