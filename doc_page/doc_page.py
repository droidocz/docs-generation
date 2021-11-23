import yaml

class DocPage:
  @property
  def title(self):
    pass

  @property
  def description(self):
    pass

  @property
  def content(self):
    pass

  @property
  def header_attrs(self):
    doc_header_attrs = {
        'title': self.title,
        'metaTitle': self.title
    }

    if self.description:
      doc_header_attrs['metaDescription'] = self.description

    return doc_header_attrs

  def _get_header(self):
    attrs_content = yaml.dump(self.header_attrs, width=float("inf"))
    return f'---\n{attrs_content}---\n\n'

  def generate(self):
    header = self._get_header()
    return header + self.content

  def save(self, output_file):
    with open(output_file, 'w+') as f:
        f.write(self.generate())