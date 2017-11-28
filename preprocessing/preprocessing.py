import re
from os.path import dirname, abspath
import nltk


class Tweet:
    def __init__(self, raw, id, valence, users, emoticons, smileys, hashtags):
        self.raw = raw
        self.id = id
        self.valence = valence
        self.users = users
        self.emoticons = emoticons
        self.smileys = smileys
        self.hashtags = hashtags


data_path = dirname(dirname(abspath(__file__))) + '/data'
with open(data_path + '/en/2018-Valence-oc-En-train.txt', 'r') as f:
    raw_text = f.read()
    raw_tweets = raw_text.split('\n')


#TODO part of speech tagging


def extract(raw_tweet):
    try:
        stopwords = nltk.corpus.stopwords.words('english')
        raw_tweet = ' '.join([w.lower() for w in raw_tweet.split() if w not in stopwords])
        raw = re.search(r'(?<=\d{5}).*?(?=\svalence)', raw_tweet).group()
        raw = re.sub(r'(.)\1{3,}', r'\1\1', raw)
        id = raw_tweet.split('-')[4]
        valence = re.search(r'(?<=valence\s).*', raw_tweet).group()
        users = re.findall(r'(?<=@).*?(?=\s)', raw_tweet)
        emoticons = re.findall(u'[\U00010000-\U0010ffff]', raw_tweet)
        smileys = re.findall(r'[(),\.\'$|8´]*[:;]+[(),\.\'$|8´]+', raw_tweet)
        hashtags = re.findall(r'(?<=#).*?(?=\s)', raw_tweet)
    except Exception as e:
        return
    return raw, id, valence, users, emoticons, smileys, hashtags


processed_tweets = []
for i in range(len(raw_tweets)):
    try:
        raw, id, valence, users, emoticons, smileys, hashtags = extract(raw_tweets[i])
        nt = Tweet(raw, id, valence, users, emoticons, smileys, hashtags)
        processed_tweets.append(nt)
    except:
        print(i)
        continue
