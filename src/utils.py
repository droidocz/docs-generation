import os
import shutil
import markdownify as md

def convert_html_to_md(html_text):
  return md.markdownify(html_text)

def humanize_tag_name(tag_name):
  return ' '.join(word.capitalize() for word in tag_name.split('-'))

def cleanup_folder(folder):
  try:
    shutil.rmtree(folder)
  except:
      pass

  os.mkdir(folder)