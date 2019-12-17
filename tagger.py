import argparse
import re
import string

import nltk
from nltk import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag

parser = argparse.ArgumentParser(prog='Tagger')
parser.add_argument('--file', metavar='N', type=str, nargs='?', help='File')
parser.add_argument('--tags', metavar='N', type=str, nargs='?', help='Number of tags')
args = parser.parse_args()

file_ = args.file
tags_ = int(args.tags)

if not file_ or tags_ == 0:
    raise Exception("File and tags input are required")


class Tagger:
    def __init__(self, file, tags):
        self.file = file
        self.tags = tags
        self.text = ''

        f = open(self.file)
        text = f.read()
        f.close()

        # remove hyperlinks
        text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*,]|'
                      '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
        text = re.sub(r'\s+', ' ', text)
        self.text = text
        self.tokens = nltk.tokenize.regexp_tokenize(text, r'\w+')

    def get_tags(self):
        tokens = self.tokens
        lemmatizer = self.remove_noise(tokens)
        freq_dist_pos = FreqDist(lemmatizer)
        common = freq_dist_pos.most_common(self.tags)
        [print(tag[0]) for tag in common]

    @staticmethod
    def stop_words():
        return (
            'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
            'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into',
            'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
            'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were',
            'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to',
            'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have',
            'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can',
            'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself',
            'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by',
            'doing', 'it', 'how', 'further', 'was', 'here', 'than', '"', '"'
        )

    @staticmethod
    def remove_noise(tokens):
        stop_words = Tagger.stop_words()
        cleaned_tokens = []
        exclude_tags = ('DT', 'IN', 'TO', 'RB', 'WRB')
        for token, tag in pos_tag(tokens):
            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token) > 0 \
                    and token not in string.punctuation \
                    and token.lower() not in stop_words \
                    and tag not in exclude_tags:
                cleaned_tokens.append(token.lower())

        return cleaned_tokens

    @staticmethod
    def lemmatize_sentence(tokens):
        lemmatizer = WordNetLemmatizer()
        lemmatized_sentence = []
        for word, tag in pos_tag(tokens):
            if tag.startswith('NN'):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'
            lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
        return lemmatized_sentence


tagger = Tagger(file_, tags_)
tagger.get_tags()
