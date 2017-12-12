import re
from os.path import dirname, abspath
import nltk
# if running from a different file use this import
# from .split_hashtags import HashTagSplitter
from split_hashtags import HashTagSplitter
from nltk.corpus import brown
import pickle
import os
import multiprocessing
import time
#from .tweet import Tweet
from tweet import Tweet
#from .emoji_handler import EmojiHandler
from emoji_handler import EmojiHandler
#from .pmi_lexicon_reader import PMILexiconReader
from pmi_lexicon_reader import PMILexiconReader
import random


def token_valence_replace(tokens):
    uni_lexicon = PMILexiconReader('unigrams-pmilexicon.txt').create_dict()
    # bi_lexicon = PMILexiconReader('bigrams-pmilexicon.txt').create_dict()
    # pairs_lexicon = PMILexiconReader('pairs-pmilexicon.txt').create_dict()
    valences = [uni_lexicon[token] for token in tokens if token in uni_lexicon]
    return valences

def hashtag_valence_replace(hashtags):
    uni_lexicon = PMILexiconReader('unigrams-pmilexicon.txt').create_dict()
    #bi_lexicon = PMILexiconReader('bigrams-pmilexicon.txt').create_dict()
    #pairs_lexicon = PMILexiconReader('pairs-pmilexicon.txt').create_dict()

    valences = []
    for hashtag in hashtags:
        valences = [uni_lexicon[word] for word in hashtag if word in uni_lexicon]
    return valences

def emoji_valence_replace(emojis):

    emoji_dict = EmojiHandler('emoji_data.txt').create_dict()
    uni_lexicon = PMILexiconReader('unigrams-pmilexicon.txt').create_dict()
    #bi_lexicon = PMILexiconReader('bigrams-pmilexicon.txt').create_dict()
    #pairs_lexicon = PMILexiconReader('pairs-pmilexicon.txt').create_dict()

    valences = []
    if len(emojis) > 0:
        for emoticon in emojis:
            emoticon_code = 'U+{:X}'.format(ord(emoticon))
            #print(emoticon_code)
            if emoticon_code in emoji_dict:
                valences = [uni_lexicon[word] for word in emoji_dict[emoticon_code] if word in uni_lexicon]

    return valences



def split(hashtag):
    possible_words = list(set(brown.words()))
    if hashtag.lower() in possible_words:
        valid_tag = [hashtag]
    else:
        tags = HashTagSplitter().split_hashtag_to_words_all_possibilities(hashtag)
        #valid = True
        for tag in tags:
            valid = True
            for word in tag:
                if word.lower() not in possible_words:
                    valid = False
            if valid: return tag
        valid_tag = [hashtag]
    return valid_tag


def handle_hashtag(raw_tweet):
    """
    Cases:
    1) no hashtag
    2) single word hashtag
    3) multiple known word hashtag
    4) multiple word hashtag
        5) one word unknown
        6) all words unknown
    :param raw_tweet:
    :return:
    """
    hashtags = re.findall(r'(?<=#).*?(?=\s)', raw_tweet)
    split_hashtags = [split(hashtag) for hashtag in hashtags]
    return split_hashtags


def extract(raw_tweet, dev=False):
    try:
        stopwords = nltk.corpus.stopwords.words('english')
        raw_tweet = ' '.join([w.lower() for w in raw_tweet.split() if w not in stopwords])
        raw = re.search(r'(?<=\d{5}\s).*?(?=\svalence)', raw_tweet).group()
        # elongated words
        raw = re.sub(r'(.)\1{3,}', r'\1\1', raw)
        id = re.search(r'(?<=-)\d{5}(?=\s)', raw_tweet).group()
        valence_text = re.search(r'(?<=valence\s).*', raw_tweet).group()
        if valence_text[0] in '0123':
            valence = valence_text[0]
        else:
            valence = valence_text[:2]
        users = re.findall(r'(?<=@).*?(?=\s)', raw_tweet)
        tokens = nltk.pos_tag([token.lower() for token in re.findall(r'[A-Za-z]+', raw)])
        pos_tags = [tup[1] for tup in tokens]
        emoticons = re.findall(u'[\U00010000-\U0010ffff]', raw_tweet)
        emoticon_valences = emoji_valence_replace(emoticons)
        smileys = re.findall(r'[(),\.\'$|8´]*[:;]+[(),\.\'$|8´]+', raw_tweet)
        hashtags = handle_hashtag(raw_tweet)
        hashtag_valence = hashtag_valence_replace(hashtags)
        tokens_valence = token_valence_replace(nltk.word_tokenize(raw))
    except Exception as e:
        print('EXTRACT')
        print(e)
        print(raw_tweet)
        print()
        return
    return raw, id, valence, users, pos_tags, emoticons, emoticon_valences, smileys, hashtags, hashtag_valence, tokens_valence


def get_raw_tweets(file_name):
    data_path = dirname(dirname(abspath(__file__))) + '/data'
    with open(data_path + file_name, 'r') as f:
        raw_text = f.read()
        raw_tweets = raw_text.split('\n')

    return raw_tweets


def create_dataset(filename, dev=False):
    raw_tweets = get_raw_tweets(filename)

    processed_tweets = []

    for i in range(len(raw_tweets)):
        try:
            raw, id, valence, users, pos_tags, emoticons, emoticon_valences, smileys, hashtags, hashtags_valence, tokens_valence = extract(raw_tweets[i], dev)
            nt = Tweet(raw, id, valence, users, pos_tags, emoticons, emoticon_valences, smileys, hashtags, hashtags_valence, tokens_valence)
            processed_tweets.append(nt)
        except:
            continue

    return processed_tweets



"""def worker(tweets, i, processed_tweets):
    print('In worker ', i)
    for tweet in tweets:
        raw, id, valence, users, pos_tags, emoticons, smileys, hashtags = extract(tweet)
        nt = Tweet(raw, id, valence, users, pos_tags, emoticons, smileys, hashtags)
        processed_tweets[tweet] = nt
    print('Worker ', i, ' finished')

if __name__ == "__main__":
    start = time.time()
    train_set = get_raw_tweets('/en/2018-Valence-oc-En-train.txt')
    manager = multiprocessing.Manager()
    processed_tweets = manager.dict()
    jobs = []
    i = 0
    j = 0
    while i < len(train_set):
        if len(train_set) - i >= 50:
            worker_set = train_set[i:i+50]
        else:
            worker_set = train_set[i:]
        i += 50
        p = multiprocessing.Process(target=worker, args=(worker_set, j, processed_tweets))
        j += 1
        jobs.append(p)
        p.start()


    for job in jobs:
        job.join()
    end = time.time()

    print(processed_tweets.values())
    print(len(processed_tweets.values()))
    print('\n\n\nTIME TAKEN: ', end - start)"""

if __name__ == "__main__":
    #train_set = create_dataset('/en/2018-Valence-oc-En-train.txt')
    #print(len(train_set))
    #print("Done")
    #test_set = create_dataset('/en/2018-Valence-oc-En-dev.txt', dev=True)

    #pickle.dump(train_set, open("train_set", "wb"))
    #pickle.dump(test_set, open("test_set", "wb"))

    with open('train_set', 'rb') as f:
        file = f.read()

    train_set = pickle.loads(file)

    for i in train_set:
        print(i)






