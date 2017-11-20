# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:34:30 2016

@author: Haiyun Peng
"""

def sent2wordembed(input_sentence,dir_embedding,dir_dictionary):

    import cPickle as pickle
    import numpy as np
    import sys
    import jieba
    index=pickle.load(open(dir_dictionary,'r'))
    embedding=pickle.load(open(dir_embedding,'r'))
    
    
  
    
    po=input_sentence
    if isinstance(po,unicode):
        #print 'Unicode'
        pass
    elif isinstance(po,str):
        #print 'string'
        po=po.decode('utf8')
    else:
        sys.exit('Illegal input format')


    po=po.replace(' ','')
    
    seg=jieba.cut(po,cut_all=False)
    
    po=[]
    for e in seg:
        po.append(e)
        
    pcorpus=[po]

    dat_emb=[]
    for   ele in pcorpus: 
        dat_emb.append([])
        j =0
        if len(ele)<15:
            while j <15:
                if j>1:
                    dat_emb[-1].append([0]*128)
                    j+=1
                else:
                    for e in ele:

                        if e in index:
                            dat_emb[-1].append(embedding[index[e],:])
                            j+=1
                        else:
                            dat_emb[-1].append([0]*128)
                            j+=1   
                        
        else:
            for e in ele:

                if e in index:
                    dat_emb[-1].append(embedding[index[e],:])
                    j+=1
                else:
                    dat_emb[-1].append([0]*128)
                    j+=1   
                    
                if j>=15:
                    break
        
        



    
    
    data_arr= np.asarray(dat_emb)

          
    return data_arr
    
















print sent2wordembed('这是一句话哈哈','embedding_word.py','word_dic.py').shape



















