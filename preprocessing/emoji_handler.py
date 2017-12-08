import os
import re


class EmojiHandler:

    def __init__(self, path):
        #path to emoji lexicon
        self.path = path

    def get_emoji_file(self):
        data_path = os.getcwd() + '/'

        with open(data_path + self.path, 'r') as f:
            raw_text = f.read()
            raw_text = raw_text.split('\n')

        return raw_text



    def create_dict(self):


        raw_emojis = self.get_emoji_file()

        def generate(start, end):
            start = int(start, 16)
            end = int(end, 16)
            unicodes = ['U+'+ re.sub('0x', '', str(hex(i))) for i in range(start, end+1)]
            return unicodes

        emoji_dict = {}
        for emoji_line in raw_emojis:
            try:
                unicode = re.search(r'^.*?(?=\s)', emoji_line).group()
                #in case of multiple unicodes
                unicodes = unicode.split('..')
                total_unicodes = generate(unicodes[0], unicodes[-1])
                words = ''.join(re.search(r'(?<=\)\s).*$', emoji_line).group())#.split()
                words = re.split(r' |\.\.', words)
                words = [word for word in words if len(word) > 0]
                for tmp in total_unicodes:
                    emoji_dict[tmp] = words
            except Exception as e:
                print(e)
        return emoji_dict


emoji_dict = EmojiHandler('emoji_data.txt').create_dict()
for k in emoji_dict:
    print(k, emoji_dict[k])