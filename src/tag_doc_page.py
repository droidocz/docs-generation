from .doc_page import DocPage
from .utils import convert_html_to_md, humanize_tag_name

class TagDocPage(DocPage):
  def __init__(self, tag_name, tag_description, tag_wiki_body):
    title = humanize_tag_name(tag_name)
    description = tag_description
    content = convert_html_to_md(tag_wiki_body)
    super().__init__(title, description, content)