# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:34:30 2016

@author: Haiyun Peng
"""

def sent2charembed(input_sentence,dir_embedding,dir_dictionary):

    import cPickle as pickle
    import numpy as np
    import sys
    
    index=pickle.load(open(dir_dictionary,'r'))
    embedding=pickle.load(open(dir_embedding,'r'))
    
    
#    p= codecs.open(input_sentence,'r','utf8')
#    po=p.readlines()  
    
    po=input_sentence
    if isinstance(po,unicode):
        #print 'Unicode'
        pass
    elif isinstance(po,str):
        #print 'string'
        po=po.decode('utf8')
    else:
        sys.exit('Illegal input format')
    

    po=po.replace('',' ')
    po=po.split()  

    pcorpus=[po]

    
    
        

    
    dat_emb=[]
    for   ele in pcorpus: 
        dat_emb.append([])
        j =0
        if len(ele)<20:
            while j <20:
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
                    
                if j>=20:
                    break
        
        



    
    
    data_arr= np.asarray(dat_emb)

          
    return data_arr
    


#print sent2charembed('这是个句子','/media/c9/9C4612F94612D43C/Users/peng0065/Dropbox/Business/senticnet/api/char_embedding/embedding_char.py','/media/c9/9C4612F94612D43C/Users/peng0065/Dropbox/Business/senticnet/api/char_embedding/char_dic.py').shape

