import os
import re

def get_emoji_file(file_name):
    data_path = os.getcwd() + '/'

    with open(data_path + file_name, 'r') as f:
        raw_text = f.read()
        raw_text = raw_text.split('\n')

    return raw_text



def create_dict(raw_emojis):

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



emoji_dict = create_dict(get_emoji_file('emoji_data.txt'))


t = '😍'
t2 = '❤'
x = 'U+{:X}'.format(ord(t2))
for k in emoji_dict:
    print(k, emoji_dict[k])
print(emoji_dict[x])




#print(emoji_dict[x])





#x = int('0030', 16)
#y = int('0039', 16)
#for i in range(x, y+1):
#    print(hex(i))


#emoji_line = e[0]
#unicode = re.search(r'^.*?(?=\s)', emoji_line).group()
#words = re.search(r'(?<=\)\s).*$', emoji_line).group().split()
#print('U+'+unicode, words)
