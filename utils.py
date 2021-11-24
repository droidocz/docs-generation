import os
import shutil
import markdownify as md

def convert_html_to_md(html_text: str):
  return md.markdownify(html_text)

def kebab_case_to_human(text: str):
  return ' '.join(word.capitalize() for word in text.split('-'))

def human_to_kebab_case(text: str):
  return '-'.join(word for word in text.split()).lower().replace('?', '').replace('/', '')

def create_folder(folder: str):
  return os.mkdir(folder)

def cleanup_folder(folder: str):
  try:
    shutil.rmtree(folder)
  except:
      pass

  create_folder(folder)
