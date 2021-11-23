from .doc_page import DocPage
from utils import convert_html_to_md, kebab_case_to_human

class TagDocPage(DocPage):
  def __init__(self, tag_name, tag_description, tag_wiki_body):
    self.tag_name = tag_name
    self.tag_description = tag_description
    self.tag_wiki_body = tag_wiki_body

  @property
  def title(self):
    return kebab_case_to_human(self.tag_name)

  @property
  def description(self):
    return self.tag_description

  @property
  def content(self):
    return convert_html_to_md(self.tag_wiki_body)
