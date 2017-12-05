import re
from os.path import dirname, abspath
import nltk
from split_hashtags import HashTagSplitter
from nltk.corpus import brown
import pickle
import os


class Tweet:
    def __init__(self, raw, id, valence, users, pos_tags, emoticons, smileys, hashtags):
        self.raw = raw
        self.id = id
        self.valence = valence
        self.users = users
        self.pos_tags = pos_tags
        self.emoticons = emoticons
        self.smileys = smileys
        self.hashtags = hashtags

    def __str__(self):
        tweet_str = "Id: %s \nRaw: \"%s\"\nValence: %s\nUsers: %s\nEmoticons: %s\nSmileys: %s\nHashtags: %s" \
                    % (self.id, self.raw, self.valence, self.users, self.emoticons, self.smileys, self.hashtags)
        return tweet_str


def split(hashtag):
    possible_words = list(set(brown.words()))

    if hashtag.lower() not in possible_words:
        tags = HashTagSplitter().split_hashtag_to_words_all_possibilities(hashtag)
        valid_tag = []
        for tag in tags:
            valid = True
            for word in tag:
                if word not in possible_words:
                    valid = False
            if valid: valid_tag.append(tag)
    else:
        valid_tag = [hashtag]
    try:
        valid_tag = valid_tag[0]
    except Exception as e:
        print(e)
    return valid_tag


def extract(raw_tweet):
    try:
        stopwords = nltk.corpus.stopwords.words('english')
        raw_tweet = ' '.join([w.lower() for w in raw_tweet.split() if w not in stopwords])
        raw = re.search(r'(?<=\d{5}).*?(?=\svalence)', raw_tweet).group()
        # elongated words
        raw = re.sub(r'(.)\1{3,}', r'\1\1', raw)
        id = raw_tweet.split('-')[4]
        valence = re.search(r'(?<=valence\s).*', raw_tweet).group()[0]
        users = re.findall(r'(?<=@).*?(?=\s)', raw_tweet)
        tokens = nltk.pos_tag([token.lower() for token in re.findall(r'[A-Za-z]+', raw)])
        pos_tags = [tup[1] for tup in tokens]
        emoticons = re.findall(u'[\U00010000-\U0010ffff]', raw_tweet)
        smileys = re.findall(r'[(),\.\'$|8´]*[:;]+[(),\.\'$|8´]+', raw_tweet)
        hashtags = re.findall(r'(?<=#).*?(?=\s)', raw_tweet)
        split_hashtags = [split(hashtag) for hashtag in hashtags]
        split_hashtags = [s for s in split_hashtags if len(s) > 0]
    except Exception as e:
        print(e)
        return
    return raw, id, valence, users, pos_tags, emoticons, smileys, split_hashtags


def get_raw_tweets(file_name):
    data_path = dirname(dirname(abspath(__file__))) + '/data'
    with open(data_path + file_name, 'r') as f:
        raw_text = f.read()
        raw_tweets = raw_text.split('\n')

    return raw_tweets


def create_dataset(filename):
    raw_tweets = get_raw_tweets(filename)

    processed_tweets = []

    for i in range(len(raw_tweets[0])):
        try:
            raw, id, valence, users, pos_tags, emoticons, smileys, hashtags = extract(raw_tweets[i])
            nt = Tweet(raw, id, valence, users, pos_tags, emoticons, smileys, hashtags)
            processed_tweets.append(nt)
        except:
            continue

    return processed_tweets


if __name__ == "__main__":
    train_set = create_dataset('/en/2018-Valence-oc-En-train.txt')
    print("Done")
    test_set = create_dataset('/en/2018-Valence-oc-En-dev.txt')

    pickle.dump(train_set, open("train_set", "wb"))
    pickle.dump(test_set, open("test_set", "wb"))
