import pickle


with open('train_set', 'rb') as f:
    file = f.read()
train_set = pickle.loads(file)

with open('test_set', 'rb') as f:
    file = f.read()
test_set = pickle.loads(file)

num_hashtags = 0
num_emoticons = 0
num_usernames = 0
num_smileys = 0

for t in train_set:
#for i in test_set:
    if len(t.hashtags) > 0:
        num_hashtags += 1
    if len(t.emoticons) > 0:
        num_emoticons += 1
    if len(t.users) > 0:
        num_usernames += 1
    if len(t.smileys) > 0:
        num_smileys += 1


print('Number of tweets with hashtags: %d' % num_hashtags)
print('Number of tweets with emoticons: %d' % num_emoticons)
print('Number of tweets with usernames: %d' % num_usernames)
print('Number of tweets with smileys: %d' % num_smileys)
print(len(train_set))
#print(len(test_set))

