from sklearn.feature_selection import SelectKBest,score_method

def select_k_best(train_data,train_label,score_method,k):
    list_index=[]
    selector=SelectKBest(score_method,k='all').fit(train_data,train_label)
    scores=selector.scores_
    scores=scores.tolist()
    sorted_score=sorted(scores,reverse=True)
    duplicates=set([x for x in sorted_score if sorted_score.count(x) > 1])
    for i in duplicates:
        sorted_score.remove(i)
    for i in range(k):
        list_index.append(scores.index(sorted_score[i]))
    return list_index