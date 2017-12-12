class Tweet:
    def __init__(self, raw, id, valence, users, pos_tags, emoticons, emoticons_valence, smileys, hashtags, hashtags_valence, tokens_valence):
        self.raw = raw
        self.id = id
        self.valence = valence
        self.users = users
        self.pos_tags = pos_tags
        self.emoticons = emoticons
        self.emoticons_valence = emoticons_valence
        self.smileys = smileys
        self.hashtags = hashtags
        self.hashtags_valence = hashtags_valence
        self.tokens_valence = tokens_valence


    def __str__(self):
        tweet_str = "Id: %s \nRaw: \"%s\"\nValence: %s\nUsers: %s\nEmoticons: %s \nEmoticonsValence: %s \nSmileys: %s\nHashtags: %s \nHashtagsValence: %s \nTokensValence: %s" \
                    % (self.id, self.raw, self.valence, self.users, self.emoticons, self.emoticons_valence, self.smileys, self.hashtags, self.hashtags_valence, self.tokens_valence)
        return tweet_str


