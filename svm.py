import pickle
import re
from nltk.tokenize import TweetTokenizer
import numpy as np
from sklearn import svm
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer


def get_num_of_hashtags(data_set):
    X = np.zeros((len(data_set), 1))
    
    for i, tweet in enumerate(data_set):
        X[i, 0] = np.asarray(tweet.count("#"))
        
    return X


def get_num_of_mult_punctuation(data_set):
    X = np.zeros((len(data_set), 1))

    for i, tweet in enumerate(data_set):
        X[i, 0] = len(re.findall(r"[?!]{2,}", tweet))
        
    return X


def get_ngram_vectors(train, test, n):
    vectorizer = CountVectorizer(ngram_range=(1, n), tokenizer=TweetTokenizer().tokenize)
    train_vector = vectorizer.fit_transform(train)
    test_vector = vectorizer.transform(test)

    return np.asarray(train_vector.toarray()), np.asarray(test_vector.toarray())


def extract_features(train, test):
    # TODO: remove magic number?
    train_vectors, test_vectors = get_ngram_vectors(train, test, 4)

    train_features = np.concatenate([get_num_of_hashtags(train),
                                     get_num_of_mult_punctuation(train),
                                     train_vectors], axis=1)

    test_features = np.concatenate([get_num_of_hashtags(test),
                                    get_num_of_mult_punctuation(test),
                                    test_vectors], axis=1)
    return train_features, test_features


def transform_to_pos_neg(np_array):
    np_array[np_array < 0] = -1
    np_array[np_array > 0] = 1
    
    return np_array


def eveluate_model(model, X, y):
    prediction = model.predict(X)

    acc = metrics.accuracy_score(y, prediction)
    print("Accuracy:", acc)

    acc_interval = acc + metrics.accuracy_score(y + 1, prediction)                    + metrics.accuracy_score(y - 1, prediction)
    print("Accuracy for small interval:", acc_interval)  # Accuracy if predicted value is +-1

    acc_dir = metrics.accuracy_score(transform_to_pos_neg(y), transform_to_pos_neg(prediction))
    print("Accuracy for right direction:", acc_dir)

train_set = np.asarray(pickle.load(open("train_set.p", "rb")))
test_set = np.asarray(pickle.load(open("test_set.p", "rb")))

y_train = train_set[:, 1].astype(np.int_)
train = train_set[:, 0]

y_test = test_set[:, 1].astype(np.int_)
test = test_set[:, 0]

X_train, X_test = extract_features(train, test)

# TODO: implement cross validation
# TODO: normalization? 
# TODO: find out about c and y (grid search maybe)

lin_svm = svm.LinearSVC()
lin_svm.fit(X_train, y_train)

eveluate_model(lin_svm, X_test, y_test)

