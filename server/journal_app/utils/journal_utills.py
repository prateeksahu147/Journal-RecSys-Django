import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances
import pickle
import json

def get_json():
    return json.load('file.json')

def read_csv(file):
    df = pd.read_csv(file, dtype={'id': str},)
    return df

def get_vectorizer(pickle_file):
    with open(pickle_file,'rb') as handle:
        e = pickle.load(handle)
    return e

def bagOfWords_tfidf_model(doc_id, num_results, data, features):
    pairwise_dist = pairwise_distances(features, features[doc_id])
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    pdists  = np.sort(pairwise_dist.flatten())[0:num_results]
    df_indices = list(data.index[indices])
    rec_data = []
    for i in range(0,len(indices)):
        rec_data.append(data.loc[df_indices[i]])
    return rec_data
        
def bagOfWords_tfidf_model_title_abstract(doc_id, num_results, data, w1, w2, title_features, features_abstract ):
    
    pairwise_dist_title = pairwise_distances(title_features, 
                                             title_features[doc_id].reshape(1,-1))
    pairwise_dist_abstract = pairwise_distances(features_abstract,
                                                features_abstract[doc_id].reshape(1,-1))
    pairwise_dist   = (w1 * pairwise_dist_title +  w2 * pairwise_dist_abstract)/float(w1 + w2)
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    pdists  = np.sort(pairwise_dist.flatten())[0:num_results]
    df_indices = list(data.index[indices])
    rec_data = []
    for i in range(0,len(indices)):
        rec_data.append(data.loc[df_indices[i]])
    return rec_data

def weighted_w2v_model(num_results, dataVector,data,doc_id):
    pairwise_dist = pairwise_distances(dataVector, dataVector[doc_id].reshape(1,-1))
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    pdists  = np.sort(pairwise_dist.flatten())[0:num_results]
    df_indices = list(data.index[indices])
    rec_data = []
    for i in range(0,len(indices)):
        rec_data.append(data.loc[df_indices[i]])
    return rec_data

def title_abstract_weighted_w2v_model(num_results, title_weighted_vector, 
                                      abstract_weighted_vector, w1, w2,
                                      data, doc_id):
    
    pairwise_dist_title = pairwise_distances(title_weighted_vector, 
                                             title_weighted_vector[doc_id].reshape(1,-1))
    pairwise_dist_abstract = pairwise_distances(abstract_weighted_vector,
                                                abstract_weighted_vector[doc_id].reshape(1,-1))
    pairwise_dist   = (w1 * pairwise_dist_title +  w2 * pairwise_dist_abstract)/float(w1 + w2)
    
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    pdists  = np.sort(pairwise_dist.flatten())[0:num_results]
    df_indices = list(data.index[indices])
    rec_data = []
    for i in range(0,len(indices)):
        rec_data.append(data.loc[df_indices[i]])
    return rec_data     

         