from json import loads
from requests import post

# -------------------------------------------
# Google Translate - translate parts of the conversation into another language
#!pip install -U deep_translator
from deep_translator import GoogleTranslator

# get Supported Languages as list
def getLang1():
  langs_list = GoogleTranslator.get_supported_languages()
  return langs_list

# get Supported Languages as dict
def getLang2():
  langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)
  return langs_dict

def getLangCode(lang):
  lang = lang.lower()
  lang = lang.strip()
  langs_dict = getLang2()
  return langs_dict[lang]

class GOOGLE_translate(object):
  def google_translate(lang, text):
    code = 'en' # defult lang is English
    try:
      code = getLangCode(lang)
    except:
      print('there is no such language, please check your spelling')
      code = 'en'
    #
    try:
      translated = GoogleTranslator(source='auto', target=code).translate(text)
      return translated
    except:
      return 'sorry,cannot translate'
    return 'cannot connect to server'

  # 'chinese': 'zh',
  # 'chinese (simplified)': 'zh-cn',
  # 'chinese (traditional)': 'zh-tw',
  # 'japanese': 'ja'
  # 'english': 'en',
  # 'french': 'fr',
text = "keep it up, you are awesome"
lang = 'Chinese'

trans = GOOGLE_translate.google_translate(lang, text)
print(trans)

# -------------------------------------------
# Wikipedia API - extract knowledge from definitions for your own conversation use
  # first-time, you need to install wikipedia package

#!pip3 install wikipedia-api
import wikipediaapi

class Wiki_API(object):
  def definition(content, how_long=200):
    # set the language for wiki
    wiki_wiki = wikipediaapi.Wikipedia('en')
    # preprocess, extract the phrase
    content = content.replace('define', '').strip()
    # search it on wiki
    page_py = wiki_wiki.page(content)
    # if existing
    if page_py.exists():
      if how_long==-1:
        con = page_py.summary
      else:
        con = page_py.summary[0:how_long] + '...'
      return con
    # when not existing
    else:
      return 'sorry, no such page for ' + content
    return page_py

# search the definition pattern: what is New York
content = 'define Java programming language'
how_long = -1
result = Wiki_API.definition(content, how_long)

print(result)
