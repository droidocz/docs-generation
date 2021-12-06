from .doc_page import DocPage
from comment_classifier.utils import escape_html_tags, get_sentences_from_comment, preprocess_sentence, remove_user_calls
from utils import convert_html_to_md
import joblib
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

import nltk
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()
sentence_scorer = joblib.load('sentence_scorer.pkl')
comment_classifier = joblib.load('comment_classifier.pkl')

class PostQuestionDocPage(DocPage):
  def __init__(self, question_title, question_body, question_tags, answer_body, comments):
    self.question_title = question_title
    self.question_body = question_body
    self.question_tags = question_tags
    self.answer_body = answer_body
    self.comments = comments

  def _get_comments_content(self):
    content = ''

    for comment in self.comments:
      sentences = get_sentences_from_comment(comment)
      data = pd.DataFrame.from_dict({
        'SentenceText': [remove_user_calls(sentence) for sentence in sentences],
        'TextScore': sentence_scorer.get_scores([preprocess_sentence(sentence) for sentence in sentences]),
        'Sentiment': [sid.polarity_scores(sentence)['compound'] for sentence in sentences],
        'CommentTextLen': [len(sentence) for sentence in sentences]
      })

      features = ['TextScore', 'Sentiment', 'CommentTextLen']
      predicted_data = comment_classifier.predict(data[features])

      joined_useful_sentences = escape_html_tags(' '.join(data[predicted_data == 1]['SentenceText']))

      if joined_useful_sentences:
        content += f"- {joined_useful_sentences}\n"

    return f"\n\n---\n\n## Notes:\n\n{content}" if content else ''


  @property
  def title(self):
    return self.question_title.replace('?', '')

  @property
  def content(self):
    return '## Context\n\n' + convert_html_to_md(self.question_body) + '\n\n---\n\n' + convert_html_to_md(self.answer_body) + self._get_comments_content()

  @property
  def header_attrs(self):
    base_header_attrs = super().header_attrs
    return {**base_header_attrs, 'tags': self.question_tags} if self.question_tags else base_header_attrs
