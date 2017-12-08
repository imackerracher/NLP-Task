
# coding: utf-8

# In[15]:

import pickle
import re
import numpy as np
from nltk.tokenize import TweetTokenizer
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import VarianceThreshold
from nltk.data import load


# In[19]:

train = np.asarray(pickle.load(open("preprocessing/train_set", "rb")))
test = np.asarray(pickle.load(open("preprocessing/test_set", "rb")))

print(train.shape, test.shape)


# In[6]:

# Extracting valence from the dataset

y_train = np.asarray([int(tweet.valence) for tweet in train])
y_test = np.asarray([int(tweet.valence) for tweet in test])


# ## Feature Generation
# 

# In[7]:

def get_num_of_hashtags(data_set):
    # This oddly shape array is needed, because the features need to be in a column-like shape
    X = np.zeros((len(data_set), 1))

    for i, tweet in enumerate(data_set):
        X[i, 0] = np.asarray(len(tweet.hashtags))

    return X


# In[8]:

def get_num_of_mult_punctuation(data_set):
    # multiple punctuation means sth. like ../!!!
    X = np.zeros((len(data_set), 1))

    for i, tweet in enumerate(data_set):
        X[i, 0] = len(re.findall(r"[?!]{2,}", tweet.raw))
        
    return X


# In[9]:

def get_num_pos_tags(train, test):
    # First find out which POS tags are possible
    vocabulary = list(load('help/tagsets/upenn_tagset.pickle'))
    pos_tags_train = [tweet.pos_tags for tweet in train]
    pos_tags_test = [tweet.pos_tags for tweet in test]

    # CountVectorizer is used to create a vector for each tweet. Each number in this vector 
    # represents the number of occurrences for a specific POS tag.
    # All those vectors have the same length, which is needed to use them for the SVM.
    vectorizer = CountVectorizer(vocabulary=vocabulary, tokenizer=lambda doc: doc, lowercase=False)

    train_vector = vectorizer.transform(pos_tags_train)
    test_vector = vectorizer.transform(pos_tags_test)
   
    return np.asarray(train_vector.toarray()), np.asarray(test_vector.toarray())



# In[10]:

def get_ngram_vectors(train, test, method="word", upper=3, lower=1):
    # This method either extracts word (method="word)" or char ngrams (method="char").
    # Again, they need to be transformed into one hot encoded vectors
    vectorizer = CountVectorizer(ngram_range=(lower, upper), tokenizer=TweetTokenizer().tokenize, 
                                 analyzer=method)
    
    raw_train = [tweet.raw for tweet in train]
    raw_test = [tweet.raw for tweet in test]
    
    train_vector = vectorizer.fit_transform(raw_train)
    test_vector = vectorizer.transform(raw_test)

    return np.asarray(train_vector.toarray()), np.asarray(test_vector.toarray())


# In[11]:

def extract_features(train, test):
    word_ngram_upper_bound = 4
    char_ngram_upper_bound = 5
    char_ngram_lower_bound = 3

    pos_vec_train, pos_vec_test = get_num_pos_tags(train, test)
    train_word_vectors, test_word_vectors = get_ngram_vectors(
        train, test, "word", word_ngram_upper_bound)
    train_char_vectors, test_char_vectors = get_ngram_vectors(
        train, test, "char", char_ngram_upper_bound, char_ngram_lower_bound)

    train_features = np.concatenate([get_num_of_hashtags(train),
                                     get_num_of_mult_punctuation(train),
                                     pos_vec_train,
                                     train_word_vectors,
                                     train_char_vectors], axis=1)

    test_features = np.concatenate([get_num_of_hashtags(test),
                                    get_num_of_mult_punctuation(test),
                                    test_word_vectors,
                                    test_char_vectors,
                                    pos_vec_test], axis=1)

    return train_features, test_features


# In[12]:

X_train, X_test = extract_features(train, test)


# ## Baseline

# In[13]:

def transform_to_pos_neg(np_array):
    np_array[np_array < 0] = -1
    np_array[np_array > 0] = 1
    
    return np_array


# In[14]:

def evaluate_model(model, X, y):
    y_copy = np.copy(y)
    prediction = model.predict(X)

    acc = metrics.accuracy_score(y, prediction)
    print("Accuracy:", acc)

    acc_interval = acc + metrics.accuracy_score(y_copy + 1, prediction)                    + metrics.accuracy_score(y_copy - 1, prediction)
    print("Accuracy for small interval:", acc_interval)  # Accuracy if predicted value is +-1

    acc_dir = metrics.accuracy_score(transform_to_pos_neg(y_copy), transform_to_pos_neg(prediction))
    print("Accuracy for right direction:", acc_dir, "\n")


# In[20]:

def fit_and_eval_svm(X_train, y_train, X_test, y_test):
    lin_svm = svm.LinearSVC()
    lin_svm.fit(X_train, y_train)
    evaluate_model(lin_svm, X_test, y_test)


# In[19]:

fit_and_eval_svm(X_train, y_train, X_test, y_test)


# ## Training with Grid Search

# In[18]:

cs = [0.001, 0.01, 0.1, 1, 10]
grid = {'C': cs}

grid_search = GridSearchCV(svm.LinearSVC(), grid, cv=5, verbose=10)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)
evaluate_model(grid_search, X_test, y_test)


# ## Feature Selection
# 

# ### Variance Threshold

# In[19]:

thresholds = [0, 0.01, 0.05, 0.1, 0.5]

for threshold in thresholds:
    variance_selector = VarianceThreshold(threshold)
    X_train_selected = variance_selector.fit_transform(X_train)
    X_test_selected = variance_selector.transform(X_test)

    print("Threshhold:", threshold)
    fit_and_eval_svm(X_train_selected, y_train, X_test_selected, y_test)


# ### Selection of kBest

# In[20]:

ks = [10, 50, 100, 200, 500, 1000, 5000]

for k in ks:
    kbest_selector = SelectKBest(chi2, k=k)
    X_train_selected = kbest_selector.fit_transform(X_train, y_train)
    X_test_selected = kbest_selector.transform(X_test)
    
    print("k:", k)
    fit_and_eval_svm(X_train_selected, y_train, X_test_selected, y_test)


# ### Recursive Feature Elimination with Cross Validation
# 

# In[22]:

from sklearn.feature_selection import RFECV

selector = RFECV(svm.LinearSVC(), step=500, cv=5, verbose=10)
selector.fit(X_train, y_train)
evaluate_model(selector, X_test, y_test)


# In[ ]:



