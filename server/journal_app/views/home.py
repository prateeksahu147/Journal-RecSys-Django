from django.shortcuts import render
from ..models.Journal import Journal
from ..utils.journal_utills import *

def get_latest_jounal(request):
    if request.method == 'GET':
        context = {}
        data = read_csv('././data/CS-journal-resSys-dataset.csv').sample(10)
        cols = [i for i in data]
        context['journal_list'] = [dict(zip(cols, i)) for i in data.values]
        #context['journal_list'] = Journal.objects.all()[:10]
    return render(request, 'journal_app/home.html', context=context)

def get_journal(request, model, feature, journal_id):
    if request.method == 'GET':
        context ={}
        context['model']=model
        context['feature']=feature
        data = read_csv('././data/CS-journal-resSys-dataset.csv')
        idx = data[data['id']==journal_id].index.values
        cols = [i for i in data]
        context['journal_detail'] = [dict(zip(cols, data.loc[idx[0]]))]
        vec=get_vectorizer('./data/title_features_count_vectorizer.pickle')

        if model == 'BagOfWord':
            if feature == 'title':
                vec=get_vectorizer('./data/title_features_count_vectorizer.pickle')
                a = bagOfWords_tfidf_model(idx[0],4,data, vec)
            elif feature == 'abstract':
                vec=get_vectorizer('./data/abstract_features_count_vectorizer.pickle')
                a = bagOfWords_tfidf_model(idx[0], 4, data, vec)
            elif feature == 'title-abstract':
                title_vec=get_vectorizer('./data/title_features_count_vectorizer.pickle')
                abstract_vec=get_vectorizer('./data/abstract_features_count_vectorizer.pickle')
                a=bagOfWords_tfidf_model_title_abstract(idx[0], 5, data, 5, 5, title_vec, abstract_vec)

        
        elif model == 'tfidf':
            if feature == 'title':
                vec=get_vectorizer('./data/tfidf_title_features.pickle')
                a = bagOfWords_tfidf_model(idx[0],4,data, vec)
            elif feature == 'abstract':
                vec=get_vectorizer('./data/tfidf_features_abstract_1.pickle')
                a = bagOfWords_tfidf_model(idx[0],10,data, vec)
            elif feature == 'title-abstract':
                title_vec=get_vectorizer('./data/tfidf_title_features.pickle')
                abstract_vec=get_vectorizer('./data/tfidf_features_abstract_1.pickle')
                a=bagOfWords_tfidf_model_title_abstract(idx[0], 5, data, 5, 5, title_vec, abstract_vec)

        elif model == 'w2v':
            if feature == 'title':
                title_weighted_vector = get_vectorizer('./data/title_weighted_vector.pickle')
                vec=get_vectorizer('./data/tfidf_title_features.pickle')
                a=weighted_w2v_model(5, title_weighted_vector,data,idx[0])
                
            elif feature == 'abstract':
                abstract_weighted_vector = get_vectorizer('./data/abstract_weighted_vector.pickle')
                vec=get_vectorizer('./data/tfidf_title_features.pickle')
                a=weighted_w2v_model(5, abstract_weighted_vector,data,idx[0])

            elif feature == 'title-abstract':
                title_weighted_vector = get_vectorizer('./data/title_weighted_vector.pickle')
                abstract_weighted_vector = get_vectorizer('./data/abstract_weighted_vector.pickle')
                a=title_abstract_weighted_w2v_model(5, title_weighted_vector, 
                                                    abstract_weighted_vector, 5, 5,
                                                    data, idx[0])
        context['rec_data'] = [dict(zip(cols, i)) for i in a]
    return render(request, 'journal_app/journal_detail.html', context=context)


def get_recommendation(data, model, feature, jornal_id):
    if model == 'bag_of_word':
        context={}
        idx = data[data['id']==journal_id].index.values
        cols = [i for i in data]
        context['journal_detail'] = [dict(zip(cols, data.loc[idx[0]]))]
        vec=get_vectorizer('./data/title_features_count_vectorizer.pickle')
        a = bagOfWords_tfidf_model(doc_id=idx[0], num_results=4, data=data, features=vec)

def select_model(request,model,feature):
    if request.method=='GET':
        context={}
        context['model']=model
        context['feature']=feature
    return render(request, 'journal_app/select_model.html', context=context)

    




