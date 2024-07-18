import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

# Variable setup (otherwise some functions won't work when copying from Jupyter notebook)
lemmatizer = WordNetLemmatizer()
stopword_list = stopwords.words('english')


def remove_punctuation(text):
    '''
    Takes in a text string and returns a string with all the punctuation removed.
    '''
    return re.sub(r'[^a-zA-Z0-9]', ' ', text)

def normalize_case(text):
    '''
    Takes in a text string and returns a string with all characters in lower case. 
    '''
    return text.lower()

def tokenize_text(text):
    '''
    Takes in a text string and returns a list where each item corresponds to a token.
    '''
    tokenized_text = word_tokenize(text)
    return tokenized_text

def remove_stopwords(tokenized_text):
    '''
    Takes in a list of text, and returns another list where the stop words have been removed.
    '''
    processed_text = [word for word in tokenized_text if word not in stopword_list]
    return processed_text

def lemmatize_text(tokenized_text):
    '''
    Takes in a list of text, and returns another list where each word has been lemmatized.
    '''

    lemmatized_text = [lemmatizer.lemmatize(word) for word in tokenized_text]
    return lemmatized_text

def process_text(text):
    '''
    Takes in a raw text document and performs the following steps in order:
    - punctuation removal
    - case normalization
    - tokenization
    - remove stopwords
    - lemmatization

    Then returns a string containing the processed text
    '''
    processed_text = remove_punctuation(text)
    processed_text = normalize_case(processed_text)
    processed_text = tokenize_text(processed_text)
    processed_text = remove_stopwords(processed_text)
    processed_text = lemmatize_text(processed_text)
    return ' '.join(processed_text)
