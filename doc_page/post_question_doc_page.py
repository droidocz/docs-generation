from .doc_page import DocPage
from utils import convert_html_to_md

class PostQuestionDocPage(DocPage):
  def __init__(self, question_title, question_body, question_tags, answer_body):
    self.question_title = question_title
    self.question_body = question_body
    self.question_tags = question_tags
    self.answer_body = answer_body

  @property
  def title(self):
    return self.question_title.replace('?', '')

  @property
  def content(self):
    return convert_html_to_md(self.answer_body)

  @property
  def header_attrs(self):
    base_header_attrs = super().header_attrs
    return {**base_header_attrs, 'tags': self.question_tags} if self.question_tags else base_header_attrs
