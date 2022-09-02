# notebook dependencies
import os 
import pandas as pd
import numpy as np

# visualization imports
import matplotlib.pyplot as plt
import seaborn as sns

# importing request module
from requests import get    

# Beautiful Soup import
from bs4 import BeautifulSoup

# regular expression import
import re

# json modulea
import json

# uni-code library
import unicodedata

# natural language toolkit library/modules
import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer

from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords


'''TEXT CLEANING FUNCTIONS'''
# creating a function titled, 'basic_clean'
# lowercase everything
# normalize unicode characters
# replace non-alphanumeric characters with whitespace
def basic_clean(string):

    # lowercase the text
    string = string.lower()

    # Handle curly quotes
    # charmap = {0x201c: u'"',
    #             0x201d: u'"',
    #             0x2018: u"'",
    #             0x2019: u"'"}

    # string = string.translate(charmap)

    # normalizing the text
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')

    # return only alphanumeric values in text: everything else, convert to whitespace
    string = re.sub("[^a-z0-9\s']", ' ', string)

    # cleans multi-line strings in the data
    string = re.sub(r"[\r|\n|\r\n]+", ' ', string)

    # removing any word/ele <= 2 letters
    string = re.sub(r'\b[a-z]{,2}\b', '', string)
    
    # removing multiple spaces
    string = re.sub(r'\s+', ' ', string)

    # removing beginning and end whitespaces
    string = string.strip()

    # return the string text
    return string

# creating a function to tokenize the string text
def tokenize(string):
    
    # creating the tokenize object
    tokenizer = ToktokTokenizer()
    
    # using the tokenize object on the input string
    return tokenizer.tokenize(string, return_str = True)


# creating the function to accept some text and apply stemming process
# using 'PorterStemmer' method
def porter_stem(string):

    # creating the object
    ps = PorterStemmer()
    
    # using list comprehension to return the stem of ea. word in the string as a list
    stems = [ps.stem(word) for word in string.split()]

    # then re-joining ea. word as a single string text w/ a space in between ea. word
    stemmed_string = ' '.join(stems)

    return stemmed_string

# create the function to lemmatize text
def lemmatize(string):
    
    # creating the lemmatizer object
    wnl = WordNetLemmatizer()
    
    # using list comprehension to apply the lemmatizer on ea. word and return words as a list
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # re-joining the individual words as a single string text
    lemmatized_string = ' '.join(lemmas)
    
    # return the tranformed string text
    return lemmatized_string

# creating the function to remove stopwords from a string of text

def remove_stopwords(string, exclude_words = None, include_words = None):
    
    # including potential redundant words in scrape
    include_words = [
                    "metaverse", 
                    "Metaverse", 
                    "meta-verse", 
                    "Meta-verse", 
                    "meta verse", 
                    "Meta Verse", 
                    "Meta verse"]

    # creating the list of english stop words
    stopword_list = stopwords.words('english')
    
    # if there are words to exlude not in stopword_list, then add them to stop word list
    if include_words:
        
        stopword_list = stopword_list + include_words

    # if there are words we dont want to remove, then take them out of the stop words list
    if exclude_words:
        
        for word in exclude_words:
            
            stopword_list.remove(word)

    # split string text into individual words        
    words = string.split()
    
    # filter the string words, and only include words not in stop words list
    filtered_words = [word for word in words if word not in stopword_list]
    
    # re-join the words into individual string text
    filtered_string = ' '.join(filtered_words)
    
    # return the string text back: excluding stop words
    return filtered_string

'''Function to clean the original data objects/df'''
def clean_data_objects(df):
    df = df[[
        "repo", \
        "language", \
        "readme_contents"]].astype(str)

    print(f'df shape: {df.shape}')

    return df

'''Function to mass dataclean the original README repo files'''
def mass_text_clean(text, include_words=None, exclude_words=None):

    text = basic_clean(text)

    text = lemmatize(text)

    text = remove_stopwords(text, include_words = include_words, exclude_words = exclude_words)

    return text