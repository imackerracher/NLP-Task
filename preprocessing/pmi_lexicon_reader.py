from os.path import dirname, abspath
import re


class PMILexiconReader:

    def __init__(self, path, type='uni'):
        #path to emoji lexicon
        self.path = path
        self.type = type

    def get_lexicon_file(self):
        data_path = dirname(dirname(abspath(__file__))) + '/data/lexicons/'

        with open(data_path + self.path, 'r') as f:
            raw_text = f.read()
            raw_text = raw_text.split('\n')

        return raw_text

    def split_line(self, line):
        """
        Split the line from the .txt file into the interesting parts.
        :param type: Specifies wether the lexicon is uni(gram), bi(gram) or pair
        :return:
        """
        line_split = line.split('\t')
        if self.type == 'bi':
            words_str = line_split[0].split()
            words = (words_str[0], words_str[1])
            emotion = line_split[1]
        elif self.type == 'pair':
            #Right now the structure of the pairs is not taken into account
            #i.e. 'one more---am' will end up as (one, more, am)
            #I don't think this matters
            #words = re.findall('^.*?[0-9]', line)
            words_str = re.split(r' |---', line_split[0])
            words = tuple(word for word in words_str)
            emotion = line_split[-3]
            #print(words)
        else:
            words = (line_split[0])
            emotion = line_split[1]
        return words, emotion


    def create_dict(self):
        word_emotion_dictionary = {}
        for line in self.get_lexicon_file()[:10]:
            try:
                word, emotion = self.split_line(line)
                word_emotion_dictionary[word] = emotion
                #print(line)
            except Exception as e:
                print(e)


        return word_emotion_dictionary



#Usage:
#lexicon = PMILexiconReader('unigrams-pmilexicon.txt').create_dict()
#lexicon = PMILexiconReader('bigrams-pmilexicon.txt', type='bi').create_dict()
lexicon = PMILexiconReader('pairs-pmilexicon.txt', type='pair').create_dict()
for k in lexicon:
    print(k, lexicon[k])