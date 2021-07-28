'''
Modules imported
'''

import requests 

from bs4 import BeautifulSoup

from src.utils import common_words

import nltk

import re 


'''
This class takes the text and converts it to list and removes the common words from the scraped text
'''

class WebsiteText:

    def __init__(self, url):
        self.url = url
    
    def get_website(self):
        
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'html.parser')
        raw_words = soup.get_text()
        return raw_words

    def text_list(self) :
        tokenizer = nltk.tokenize.RegexpTokenizer("[a-zA-z]+")
        tokens = tokenizer.tokenize(self.get_website())
        return tokens
    
    def words_to_lowercase(self):
        new_words = []
        for char in self.text_list():
            new_words.append(char.lower())
        return new_words
    
    def remove_common_words(self):
        word_list = []
        for element in self.words_to_lowercase():
            if element not in common_words and len(element) >= 3:
                word_list.append(element)       
        return word_list
    

