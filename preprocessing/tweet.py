class Tweet:
    def __init__(self, raw, id, valence, users, pos_tags, emoticons, emoticons_valence, smileys, hashtags):
        self.raw = raw
        self.id = id
        self.valence = valence
        self.users = users
        self.pos_tags = pos_tags
        self.emoticons = emoticons
        self.emoticons_valence = emoticons_valence
        self.smileys = smileys
        self.hashtags = hashtags


    def __str__(self):
        tweet_str = "Id: %s \nRaw: \"%s\"\nValence: %s\nUsers: %s\nEmoticons: %s \nEmoticonsValence: %s \nSmileys: %s\nHashtags: %s" \
                    % (self.id, self.raw, self.valence, self.users, self.emoticons, self.emoticons_valence, self.smileys, self.hashtags)
        return tweet_str


