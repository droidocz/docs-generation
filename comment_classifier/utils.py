import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, MWETokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from functools import reduce

nltk.download('stopwords')

ignore_words = ['<CODE>', '<URL>', '<CALL>', '?']
mwe_tokenizer = MWETokenizer([tuple(word_tokenize(word)) for word in ignore_words], separator='')
stemmer = PorterStemmer()
english_stopwords = set(stopwords.words('english'))

def tokenize_words(sentence: str):
  return mwe_tokenizer.tokenize(word_tokenize(sentence))

def stem_sentence(sentence: str):
  token_words = tokenize_words(sentence)
  selected_words = []

  for word in token_words:
    if word in ignore_words:
      selected_words.append(word)
      continue

    updated_word = word.lower()

    if updated_word.isalnum() and updated_word not in english_stopwords:
      selected_words.append(stemmer.stem(updated_word))

  return ' '.join(selected_words)

preprocess_fns = [
  lambda x : re.sub(r'```[\s\S]+?```', '<CODE>', x), # Replace multi line <CODE>
  lambda x : re.sub(r'`.+?`', '<CODE>', x), # Replace single line <CODE>
  lambda x : re.sub(r'@\S+', '<CALL>', x), # Replace <CALL>
  lambda x : re.sub(r'\[.*\]\(.*\)', '<URL>', x), # Replace <URL> for markdown
  lambda x : re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '<URL>', x), # Replace <URL>
  lambda x : re.sub('([a-z0-9])([A-Z])', r'\1 \2', x), # split camel case
  stem_sentence
]

def remove_user_calls(sentence: str):
  return re.sub(r'@\S+', '', sentence)

def preprocess_sentence(sentence: str):
  return reduce(lambda res, f: f(res), preprocess_fns, sentence)

def get_sentences_from_comment(comment: str):
  return sent_tokenize(comment)

def preprocess_comment(comment: str):
  sentences = get_sentences_from_comment(comment)
  return [preprocess_sentence(sentence) for sentence in sentences]
