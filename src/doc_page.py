class DocPage:
  def __init__(self, title, description, content):
    self.title = title
    self.description = description
    self.content = content

  def _get_header(self):
    header_attrs = {
        'title': self.title,
        'metaTitle': self.title,
        'metaDescription': self.description
    }
    attrs_content = [f"{key}: \"{value}\"" for (key, value) in header_attrs.items()]
    header_content = ['---'] + attrs_content + ['---\n\n']
    return '\n'.join(header_content)

  def generate(self):
    header = self._get_header()
    return header + self.content

  def save(self, output_file):
    with open(output_file, 'w+') as f:
        f.write(self.generate())